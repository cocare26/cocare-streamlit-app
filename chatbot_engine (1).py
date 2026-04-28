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


# =========================
# 🔔 Notification Engine
# =========================
def notification_engine(intent, sentiment, network_pred, history_count):

    notification = "none"
    escalation = False

    # 🟢 مشكلة بسيطة
    if intent in ["greeting", "thanks", "other"]:
        return notification, escalation

    # 🔴 حالة خطيرة (أولوية أعلى)
    if sentiment == "negative" and network_pred == 1:
        notification = "external_noti"

    # 🟡 مشكلة متكررة
    elif history_count >= 2:
        notification = "internal_noti"

    # 💣 escalation
    if sentiment == "negative" and history_count >= 3:
        escalation = True

    return notification, escalation


# =========================
# 📝 Logging
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
        "escalation": result.get("escalation"),
        "notification_type": result.get("notification_type"),
        "response": result.get("response")
    }

    try:
        old_logs = pd.read_csv(CHAT_LOG_PATH)
        new_logs = pd.concat([old_logs, pd.DataFrame([row])], ignore_index=True)
    except Exception:
        new_logs = pd.DataFrame([row])

    new_logs.to_csv(CHAT_LOG_PATH, index=False, encoding="utf-8-sig")


# =========================
# 🤖 Main Engine
# =========================
def process_message(user_message, metrics=None):

    lang = detect_language(user_message)

    intent, intent_confidence = predict_intent(user_message, lang)
    sentiment, sentiment_score = predict_sentiment(user_message, lang)
    prediction = predict_network_issue(metrics)

    # =========================
    # ❓ Low confidence
    # =========================
    if intent_confidence < 0.60:

        decision = {
            "rule_used": "clarification",
            "prediction": prediction
        }

        response = build_final_response(
            intent="other",
            sentiment=sentiment,
            decision=decision,
            lang=lang
        )

        result = {
            "language": lang,
            "intent": "unknown",
            "intent_confidence": intent_confidence,
            "sentiment": sentiment,
            "sentiment_score": sentiment_score,
            "prediction": prediction,
            "response": response,
            "escalation": False,
            "notification_type": "none"
        }

        log_chat(user_message, result)
        return result

    # =========================
    # 🔥 Notification + Escalation
    # =========================
    history_count = metrics.get("history_count", 0) if metrics else 0

    notification_type, escalation = notification_engine(
        intent,
        sentiment,
        prediction,
        history_count
    )

    # =========================
    # 🧠 Decision
    # =========================
    decision = {
        "prediction": prediction,
        "escalation": escalation,
        "notification": notification_type
    }

    if escalation and prediction == 1:
        decision["rule_used"] = "technical_high_risk"
    elif escalation and sentiment == "negative":
        decision["rule_used"] = "negative_escalation"
    else:
        decision["rule_used"] = "normal"

    # =========================
    # 💬 Response
    # =========================
    response = build_final_response(
        intent=intent,
        sentiment=sentiment,
        decision=decision,
        lang=lang
    )

    result = {
        "language": lang,
        "intent": intent,
        "intent_confidence": intent_confidence,
        "sentiment": sentiment,
        "sentiment_score": sentiment_score,
        "prediction": prediction,
        "response": response,
        "escalation": escalation,
        "notification_type": notification_type
    }

    # =========================
    # 📡 إرسال تنبيه
    # =========================
    if escalation:
        send_notification(notification_type, result)

    # =========================
    # 💾 Logging
    # =========================
    log_chat(user_message, result)

    return result
