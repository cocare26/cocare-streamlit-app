from datetime import datetime
import pandas as pd

from utils.intent_utils import predict_intent
from utils.sentiment_utils import predict_sentiment
from utils.prediction_utils import predict_network_issue
from utils.response_logic import ArabicResponseManager


# =========================
# Paths
# =========================

RESPONSES_PATH = "data/responses_ar.csv"
FOLLOW_UP_PATH = "data/follow_up_ar.csv"
CHAT_LOG_PATH = "data/chat_logs.csv"


# =========================
# Response Manager
# =========================

response_manager = ArabicResponseManager(
    responses_path=RESPONSES_PATH,
    followup_path=FOLLOW_UP_PATH
)


# =========================
# Helpers
# =========================

def normalize_sentiment(sentiment):
    sentiment = str(sentiment).lower().strip()

    if sentiment in ["positive", "pos", "label_2", "2"]:
        return "positive"

    if sentiment in ["negative", "neg", "label_0", "0"]:
        return "negative"

    return "neutral"


def get_prediction_result(user_message=None):
    try:
        return int(predict_network_issue())
    except Exception:
        return 0


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


def get_notification_type(intent, sentiment, prediction, escalation):
    if not escalation:
        return "none"

    if prediction == 1:
        return "internal_technical_team"

    if sentiment == "negative":
        return "customer_support"

    return "internal_review"


def log_chat(user_message, result):
    row = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "user_message": user_message,
        "intent": result.get("intent"),
        "intent_confidence": result.get("intent_confidence"),
        "sentiment": result.get("sentiment"),
        "sentiment_score": result.get("sentiment_score"),
        "prediction": result.get("prediction"),
        "escalation": result.get("escalation"),
        "notification_type": result.get("notification_type"),
        "response": result.get("response"),
        "follow_up": result.get("follow_up")
    }

    try:
        old_logs = pd.read_csv(CHAT_LOG_PATH)
        new_logs = pd.concat([old_logs, pd.DataFrame([row])], ignore_index=True)
    except Exception:
        new_logs = pd.DataFrame([row])

    new_logs.to_csv(CHAT_LOG_PATH, index=False, encoding="utf-8-sig")


# =========================
# Main Chatbot Function
# =========================

def process_message(user_message):
    # 1. Intent
    intent, intent_confidence = predict_intent(user_message)

    # 2. Sentiment
    sentiment, sentiment_score = predict_sentiment(user_message)
    sentiment = normalize_sentiment(sentiment)

    if sentiment_score < 0.60:
        sentiment = "neutral"

    # 3. Network Prediction
    prediction = get_prediction_result(user_message)

    # 4. Low confidence fallback
    if intent_confidence < 0.60:
        result = {
            "intent": "unknown",
            "intent_confidence": intent_confidence,
            "sentiment": sentiment,
            "sentiment_score": sentiment_score,
            "prediction": prediction,
            "response": "لست متأكدًا أنني فهمت طلبك بشكل صحيح. هل يمكنك التوضيح أكثر؟",
            "follow_up": "هل تقصد مشكلة في الإنترنت أو الدفع أو الباقة؟",
            "escalation": False,
            "notification_type": "none"
        }

        log_chat(user_message, result)
        return result

    # 5. Response
    response = response_manager.get_response(
        intent=intent,
        sentiment=sentiment,
        prediction=prediction
    )

    follow_up = response_manager.get_follow_up(intent)

    # 6. Escalation + Notification
    escalation = should_escalate(
        intent=intent,
        sentiment=sentiment,
        prediction=prediction,
        intent_confidence=intent_confidence
    )

    notification_type = get_notification_type(
        intent=intent,
        sentiment=sentiment,
        prediction=prediction,
        escalation=escalation
    )

    # 7. Add escalation sentence if needed
    if escalation:
        response += " تم تحويل الحالة للفريق المختص لمتابعتها."

    # 8. Final result
    result = {
        "intent": intent,
        "intent_confidence": intent_confidence,
        "sentiment": sentiment,
        "sentiment_score": sentiment_score,
        "prediction": prediction,
        "response": response,
        "follow_up": follow_up,
        "escalation": escalation,
        "notification_type": notification_type
    }

    # 9. Save log for dashboard
    log_chat(user_message, result)

    return result
