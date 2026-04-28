from datetime import datetime
import os
import pandas as pd

from utils.language_utils import detect_language
from utils.intent_utils import predict_intent
from utils.sentiment_utils import predict_sentiment
from utils.prediction_utils import predict_network_issue
from utils.response_utils import build_final_response
from utils.notification_utils import send_notification


# =========================
# Paths
# =========================
CHAT_LOG_PATH = "data/chat_logs.csv"

NOTIFICATION_DIR = "/drive/MyDrive/CoCare/utils/Notifications"

INTERNAL_NOTIFICATIONS_AR_PATH = f"{NOTIFICATION_DIR}/internal_notifications.csv"
INTERNAL_NOTIFICATIONS_EN_PATH = f"{NOTIFICATION_DIR}/internal_notifications_en.csv"

EXTERNAL_NOTIFICATIONS_AR_PATH = f"{NOTIFICATION_DIR}/external_notifications.csv"
EXTERNAL_NOTIFICATIONS_EN_PATH = f"{NOTIFICATION_DIR}/external_notifications_en.csv"


# =========================
# Helpers
# =========================
def safe_int(value, default=0):
    try:
        if value == "" or pd.isna(value):
            return default
        return int(float(value))
    except Exception:
        return default


def safe_bool(value):
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in ["true", "1", "yes", "y"]


# =========================
# Load Notification Data
# =========================
def load_csv(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing required file: {path}")
    return pd.read_csv(path, encoding="utf-8-sig").fillna("")


def load_notification_tables():
    return {
        "internal_ar": load_csv(INTERNAL_NOTIFICATIONS_AR_PATH),
        "internal_en": load_csv(INTERNAL_NOTIFICATIONS_EN_PATH),
        "external_ar": load_csv(EXTERNAL_NOTIFICATIONS_AR_PATH),
        "external_en": load_csv(EXTERNAL_NOTIFICATIONS_EN_PATH),
    }


def get_row(df, issue_type):
    row = df[df["issue_type"].astype(str) == str(issue_type)]

    if row.empty:
        row = df[df["issue_type"].astype(str) == "normal"]

    if row.empty:
        raise ValueError("CSV must contain issue_type='normal' row")

    return row.iloc[0].to_dict()


# =========================
# Issue Type Detection
# =========================
def detect_issue_type(metrics=None, prediction=0):
    metrics = metrics or {}

    if safe_bool(metrics.get("maintenance")):
        return "maintenance"

    if safe_bool(metrics.get("outage")):
        return "outage"

    latency = metrics.get("latency")
    packet_loss = metrics.get("packet_loss")
    signal_strength = metrics.get("signal_strength")
    congestion = metrics.get("congestion")
    jitter = metrics.get("jitter")
    qos_score = metrics.get("qos_score")

    if latency is not None and float(latency) >= 250:
        return "high_latency"

    if packet_loss is not None and float(packet_loss) >= 5:
        return "packet_loss"

    if signal_strength is not None and float(signal_strength) <= -100:
        return "weak_signal"

    if congestion is not None and float(congestion) >= 80:
        return "network_congestion"

    if qos_score is not None and float(qos_score) <= 60:
        return "service_degradation"

    if jitter is not None and float(jitter) >= 50:
        return "unstable_connection"

    if prediction == 1:
        return "prediction_alert"

    return "normal"


# =========================
# Customer Notification Builder
# =========================
def build_customer_notification(issue_type, external_ar_row, external_en_row, metrics=None):
    metrics = metrics or {}

    start_time = metrics.get(
        "outage_started_at",
        datetime.now().strftime("%Y-%m-%d %H:%M")
    )

    duration = safe_int(
        metrics.get("estimated_resolution_minutes"),
        default=30
    )

    base_ar = external_ar_row.get("external_notification_ar", "")
    base_en = external_en_row.get("external_notification_en", "")

    message_ar = (
        f"نعتذر عن الإزعاج. {base_ar} "
        f"نوع العطل: {issue_type}. "
        f"وقت العطل: {start_time}. "
        f"المدة المتوقعة للحل: حوالي {duration} دقيقة. "
        f"نشكركم على تفهمكم."
    )

    message_en = (
        f"We apologize for the inconvenience. {base_en} "
        f"Issue type: {issue_type}. "
        f"Issue time: {start_time}. "
        f"Expected resolution time: about {duration} minutes. "
        f"Thank you for your understanding."
    )

    return message_ar, message_en


# =========================
# Notification Engine
# =========================
def notification_engine(intent, sentiment, prediction, history_count, metrics=None):
    metrics = metrics or {}
    tables = load_notification_tables()

    issue_type = detect_issue_type(metrics, prediction)

    internal_ar_row = get_row(tables["internal_ar"], issue_type)
    internal_en_row = get_row(tables["internal_en"], issue_type)
    external_ar_row = get_row(tables["external_ar"], issue_type)
    external_en_row = get_row(tables["external_en"], issue_type)

    if intent in ["greeting", "thanks", "other"] or issue_type == "normal":
        return {
            "issue_type": "normal",
            "notification_type": "none",
            "escalation": False,
            "severity": "low",
            "show_to_customer": 0,
            "internal_message_ar": None,
            "internal_message_en": None,
            "external_message_ar": None,
            "external_message_en": None,
            "display_channel": "none",
            "suggested_action_ar": None,
            "suggested_action_en": None,
            "priority": 0,
            "escalate_after_attempts": 0,
            "outage_started_at": None,
            "estimated_resolution_minutes": 0,
        }

    severity = str(
        internal_en_row.get(
            "severity",
            external_en_row.get("severity", "low")
        )
    ).lower()

    show_to_customer = safe_int(external_en_row.get("show_to_customer", 0))
    escalate_after = safe_int(internal_en_row.get("escalate_after_attempts", 0))
    priority = safe_int(internal_en_row.get("priority", 0))

    employee_attempts = safe_int(metrics.get("employee_attempts", history_count))
    employee_resolved = metrics.get("employee_resolved", None)

    escalation = False

    if severity == "critical":
        escalation = True

    if sentiment == "negative" and history_count >= 3:
        escalation = True

    if escalate_after > 0 and employee_attempts >= escalate_after:
        escalation = True

    if employee_resolved is False:
        escalation = True

    customer_ar, customer_en = build_customer_notification(
        issue_type=issue_type,
        external_ar_row=external_ar_row,
        external_en_row=external_en_row,
        metrics=metrics
    )

    notification_type = "internal_noti"
    display_channel = "employee_dashboard"
    external_message_ar = None
    external_message_en = None

    if escalation and show_to_customer == 1:
        notification_type = "external_noti"
        display_channel = "customer_app"
        external_message_ar = customer_ar
        external_message_en = customer_en

    return {
        "issue_type": issue_type,
        "notification_type": notification_type,
        "escalation": escalation,
        "severity": severity,
        "show_to_customer": show_to_customer,
        "internal_message_ar": internal_ar_row.get("internal_notification_ar"),
        "internal_message_en": internal_en_row.get("internal_notification_en"),
        "external_message_ar": external_message_ar,
        "external_message_en": external_message_en,
        "display_channel": display_channel,
        "suggested_action_ar": internal_ar_row.get("suggested_action_ar"),
        "suggested_action_en": internal_en_row.get("suggested_action"),
        "priority": priority,
        "escalate_after_attempts": escalate_after,
        "outage_started_at": metrics.get("outage_started_at"),
        "estimated_resolution_minutes": metrics.get("estimated_resolution_minutes"),
    }


# =========================
# Logging
# =========================
def log_chat(user_message, result):
    os.makedirs("data", exist_ok=True)

    row = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "user_message": user_message,
        "language": result.get("language"),
        "intent": result.get("intent"),
        "intent_confidence": result.get("intent_confidence"),
        "sentiment": result.get("sentiment"),
        "sentiment_score": result.get("sentiment_score"),
        "prediction": result.get("prediction"),
        "issue_type": result.get("issue_type"),
        "severity": result.get("severity"),
        "escalation": result.get("escalation"),
        "notification_type": result.get("notification_type"),
        "display_channel": result.get("display_channel"),
        "suggested_action_ar": result.get("suggested_action_ar"),
        "suggested_action_en": result.get("suggested_action_en"),
        "priority": result.get("priority"),
        "outage_started_at": result.get("outage_started_at"),
        "estimated_resolution_minutes": result.get("estimated_resolution_minutes"),
        "response": result.get("response"),
        "internal_message_ar": result.get("internal_message_ar"),
        "internal_message_en": result.get("internal_message_en"),
        "external_message_ar": result.get("external_message_ar"),
        "external_message_en": result.get("external_message_en"),
    }

    try:
        old_logs = pd.read_csv(CHAT_LOG_PATH, encoding="utf-8-sig")
        new_logs = pd.concat([old_logs, pd.DataFrame([row])], ignore_index=True)
    except Exception:
        new_logs = pd.DataFrame([row])

    new_logs.to_csv(CHAT_LOG_PATH, index=False, encoding="utf-8-sig")


# =========================
# Main Chatbot Engine
# =========================
def process_message(user_message, metrics=None):
    metrics = metrics or {}

    lang = detect_language(user_message)

    intent, intent_confidence = predict_intent(user_message, lang)
    sentiment, sentiment_score = predict_sentiment(user_message, lang)
    prediction = predict_network_issue(metrics)

    if intent_confidence < 0.60:
        decision = {
            "rule_used": "clarification",
            "prediction": prediction,
        }

        response = build_final_response(
            intent="other",
            sentiment=sentiment,
            decision=decision,
            lang=lang,
        )

        result = {
            "language": lang,
            "intent": "unknown",
            "intent_confidence": intent_confidence,
            "sentiment": sentiment,
            "sentiment_score": sentiment_score,
            "prediction": prediction,
            "issue_type": "unknown",
            "severity": None,
            "response": response,
            "escalation": False,
            "notification_type": "none",
            "display_channel": "none",
            "suggested_action_ar": None,
            "suggested_action_en": None,
            "priority": 0,
            "internal_message_ar": None,
            "internal_message_en": None,
            "external_message_ar": None,
            "external_message_en": None,
        }

        log_chat(user_message, result)
        return result

    history_count = safe_int(metrics.get("history_count", 0))

    notification_decision = notification_engine(
        intent=intent,
        sentiment=sentiment,
        prediction=prediction,
        history_count=history_count,
        metrics=metrics,
    )

    decision = {
        "prediction": prediction,
        "issue_type": notification_decision["issue_type"],
        "severity": notification_decision["severity"],
        "escalation": notification_decision["escalation"],
        "notification": notification_decision["notification_type"],
        "suggested_action": notification_decision["suggested_action_en"],
        "priority": notification_decision["priority"],
    }

    if notification_decision["severity"] == "critical":
        decision["rule_used"] = "critical_network_issue"
    elif notification_decision["escalation"] and prediction == 1:
        decision["rule_used"] = "technical_high_risk"
    elif notification_decision["escalation"] and sentiment == "negative":
        decision["rule_used"] = "negative_escalation"
    elif notification_decision["issue_type"] != "normal":
        decision["rule_used"] = "network_issue_detected"
    else:
        decision["rule_used"] = "normal"

    response = build_final_response(
        intent=intent,
        sentiment=sentiment,
        decision=decision,
        lang=lang,
    )

    result = {
        "language": lang,
        "intent": intent,
        "intent_confidence": intent_confidence,
        "sentiment": sentiment,
        "sentiment_score": sentiment_score,
        "prediction": prediction,
        "response": response,
        **notification_decision,
    }

    if result["notification_type"] != "none":
        send_notification(result["notification_type"], result)

    log_chat(user_message, result)

    return result
