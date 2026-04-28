from datetime import datetime
import os
import pandas as pd

from utils.language_utils import detect_language
from utils.intent_utils import predict_intent
from utils.sentiment_utils import predict_sentiment
from utils.prediction_utils import predict_network_issue
from utils.response_utils import build_final_response
from utils.notification_utils import send_notification

CHAT_LOG_PATH = "data/chat_logs.csv"

NOTIFICATIONS_PATH = "data/notifications.csv"
EXTERNAL_NOTIFICATIONS_PATH = "data/external_notifications.csv"
EXTERNAL_NOTIFICATIONS_EN_PATH = "data/external_notifications_en.csv"
INTERNAL_NOTIFICATIONS_EN_PATH = "data/internal_notifications_en.csv"


# =========================
# Load Notification Data
# =========================
def load_csv(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing required file: {path}")
    return pd.read_csv(path)


def load_notification_tables():
    return {
        "notifications": load_csv(NOTIFICATIONS_PATH),
        "external": load_csv(EXTERNAL_NOTIFICATIONS_PATH),
        "external_en": load_csv(EXTERNAL_NOTIFICATIONS_EN_PATH),
        "internal_en": load_csv(INTERNAL_NOTIFICATIONS_EN_PATH),
    }


def get_row(df, issue_type):
    row = df[df["issue_type"] == issue_type]
    if row.empty:
        row = df[df["issue_type"] == "normal"]
    return row.iloc[0].to_dict()


# =========================
# Issue Type Detection
# =========================
def detect_issue_type(metrics=None, prediction=0):
    if not metrics:
        return "prediction_alert" if prediction == 1 else "normal"

    if metrics.get("maintenance") is True:
        return "maintenance"

    if metrics.get("outage") is True:
        return "outage"

    latency = metrics.get("latency")
    packet_loss = metrics.get("packet_loss")
    signal_strength = metrics.get("signal_strength")
    congestion = metrics.get("congestion")
    jitter = metrics.get("jitter")
    qos_score = metrics.get("qos_score")

    if latency is not None and latency >= 250:
        return "high_latency"

    if packet_loss is not None and packet_loss >= 5:
        return "packet_loss"

    if signal_strength is not None and signal_strength <= -100:
        return "weak_signal"

    if congestion is not None and congestion >= 80:
        return "network_congestion"

    if qos_score is not None and qos_score <= 60:
        return "service_degradation"

    if jitter is not None and jitter >= 50:
        return "unstable_connection"

    if prediction == 1:
        return "prediction_alert"

    return "normal"


# =========================
# Notification Engine
# =========================
def notification_engine(intent, sentiment, prediction, history_count, metrics=None):
    tables = load_notification_tables()

    issue_type = detect_issue_type(metrics, prediction)

    main_row = get_row(tables["notifications"], issue_type)
    external_row = get_row(tables["external"], issue_type)
    internal_row = get_row(tables["internal_en"], issue_type)

    notification_type = "none"
    escalation = False

    if intent in ["greeting", "thanks", "other"]:
        issue_type = "normal"
        main_row = get_row(tables["notifications"], issue_type)
        external_row = get_row(tables["external"], issue_type)
        internal_row = get_row(tables["internal_en"], issue_type)

        return {
            "issue_type": issue_type,
            "notification_type": "none",
            "escalation": False,
            "severity": main_row.get("severity"),
            "show_to_customer": int(main_row.get("show_to_customer", 0)),
            "internal_message": internal_row.get("internal_notification_en"),
            "external_message_ar": external_row.get("external_notification_ar"),
            "external_message_en": external_row.get("external_notification_en"),
            "display_channel": external_row.get("display_channel"),
            "suggested_action": internal_row.get("suggested_action"),
            "priority": internal_row.get("priority", 0),
            "escalate_after_attempts": internal_row.get("escalate_after_attempts", 0),
        }

    escalate_after = int(internal_row.get("escalate_after_attempts", 0))
    show_to_customer = int(main_row.get("show_to_customer", 0))
    severity = main_row.get("severity")

    if issue_type != "normal":
        notification_type = "internal_noti"

    if show_to_customer == 1 and sentiment == "negative":
        notification_type = "external_noti"

    if severity in ["high", "critical"]:
        notification_type = "external_noti" if show_to_customer == 1 else "internal_noti"

    if escalate_after > 0 and history_count >= escalate_after:
        escalation = True

    if sentiment == "negative" and history_count >= 3:
        escalation = True

    if severity == "critical":
        escalation = True

    return {
        "issue_type": issue_type,
        "notification_type": notification_type,
        "escalation": escalation,
        "severity": severity,
        "show_to_customer": show_to_customer,
        "internal_message": internal_row.get("internal_notification_en"),
        "external_message_ar": external_row.get("external_notification_ar"),
        "external_message_en": external_row.get("external_notification_en"),
        "display_channel": external_row.get("display_channel"),
        "suggested_action": internal_row.get("suggested_action"),
        "priority": internal_row.get("priority", 0),
        "escalate_after_attempts": escalate_after,
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
        "suggested_action": result.get("suggested_action"),
        "priority": result.get("priority"),
        "response": result.get("response"),
    }

    try:
        old_logs = pd.read_csv(CHAT_LOG_PATH)
        new_logs = pd.concat([old_logs, pd.DataFrame([row])], ignore_index=True)
    except Exception:
        new_logs = pd.DataFrame([row])

    new_logs.to_csv(CHAT_LOG_PATH, index=False, encoding="utf-8-sig")


# =========================
# Main Engine
# =========================
def process_message(user_message, metrics=None):
    if metrics is None:
        metrics = {}

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
            "suggested_action": None,
            "priority": 0,
        }

        log_chat(user_message, result)
        return result

    history_count = metrics.get("history_count", 0)

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
        "suggested_action": notification_decision["suggested_action"],
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
