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


def should_escalate(intent, sentiment, prediction, intent_confidence):
    if intent_confidence < 0.60:
        return False

    if prediction == 1 and intent in [
        "slow_internet",
        "no_signal",
        "network_status",
        "network_complaint",
        "technical_support"
    ]:
        return True

    if sentiment == "negative" and intent in [
        "network_complaint",
        "payment_issue",
        "technical_support",
        "no_signal",
        "slow_internet"
    ]:
        return True

    return False


def get_notification_type(sentiment, prediction, escalation):
    if not escalation:
        return "none"

    if prediction == 1:
        return "internal_technical_team"

    if sentiment == "negative":
        return "customer_support"

    return "internal_review"


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


def process_message(user_message, metrics=None):
    lang = detect_language(user_message)

    intent, intent_confidence = predict_intent(user_message, lang)
    sentiment, sentiment_score = predict_sentiment(user_message, lang)
    prediction = predict_network_issue(metrics)

    if intent_confidence < 0.60:
        decision = {"rule_used": "clarification", "prediction": prediction}

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

    escalation = should_escalate(intent, sentiment, prediction, intent_confidence)
    notification_type = get_notification_type(sentiment, prediction, escalation)

    decision = {
        "prediction": prediction,
        "escalation": escalation
    }

    if escalation and prediction == 1:
        decision["rule_used"] = "technical_high_risk"
    elif escalation and sentiment == "negative":
        decision["rule_used"] = "negative_escalation"
    else:
        decision["rule_used"] = "normal"

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

    if escalation:
        send_notification(notification_type, result)

    log_chat(user_message, result)

    return result
