from utils.text_preprocessing import clean_text
from utils.language_utils import detect_language
from utils.intent_utils import predict_intent
from utils.sentiment_utils import predict_sentiment
from utils.prediction_utils import predict_network_issue
from utils.notification_utils import send_notification
from utils.response_utils import build_final_response
from engine.decision_engine import decision_engine


NETWORK_INTENTS = {
    "network_complaint",
    "slow_internet",
    "no_signal",
    "technical_support",
    "weak_signal",
    "network_status"
}


def chatbot_engine(message, metrics=None):
    """
    Main chatbot orchestration engine.

    Steps:
    1) Clean text
    2) Detect language
    3) Predict intent
    4) Predict sentiment
    5) Run network prediction if needed
    6) Apply decision engine
    7) Build final response
    8) Send notifications if needed
    9) Return final response package
    """

    # 1) Validate input
    if message is None or str(message).strip() == "":
        empty_decision = {
            "rule_used": "clarification",
            "decision_type": "clarification",
            "severity": "low",
            "escalation": False,
            "route_to": "bot",
            "notify_customer": True,
            "notify_staff": False,
            "notification_channel": "in_app"
        }

        return {
            "language": "ar",
            "intent": "other",
            "sentiment": "neutral",
            "prediction": 0,
            "decision": empty_decision,
            "response": "الرسالة فارغة. يرجى كتابة طلبك."
        }

    # 2) Clean message
    cleaned_message = clean_text(message)

    # إذا أصبح النص فارغًا بعد التنظيف
    if not cleaned_message:
        empty_decision = {
            "rule_used": "clarification",
            "decision_type": "clarification",
            "severity": "low",
            "escalation": False,
            "route_to": "bot",
            "notify_customer": True,
            "notify_staff": False,
            "notification_channel": "in_app"
        }

        return {
            "language": "ar",
            "intent": "other",
            "sentiment": "neutral",
            "prediction": 0,
            "decision": empty_decision,
            "response": "الرسالة غير واضحة. يرجى كتابة طلبك بشكل أوضح."
        }

    # 3) Detect language
    lang = detect_language(cleaned_message)
    print("DEBUG lang:", lang)

    # 4) Predict intent
    try:
        intent = predict_intent(cleaned_message, lang)
        print("DEBUG intent:", intent)
    except Exception as e:
        print("⚠️ Intent prediction error:", e)
        intent = "other"

    # Manual intent rules for short conversational phrases
    message_lower = cleaned_message.lower().strip()

    MANUAL_INTENT_RULES = {
    # Arabic
    "مرحبا": "greeting",
    "اهلا": "greeting",
    "أهلا": "greeting",
    "هلا": "greeting",
    "السلام عليكم": "greeting",
    "كيفك": "how_are_you",
    "شلونك": "how_are_you",
    "كيف الحال": "how_are_you",
    "شكرا": "thanks",
    "شكراً": "thanks",
    "مع السلامة": "goodbye",
    "باي": "goodbye",

    # English
    "hello": "greeting",
    "hi": "greeting",
    "hey": "greeting",
    "how are you": "how_are_you",
    "how r u": "how_are_you",
    "how are u": "how_are_you",
    "thank you": "thanks",
    "thanks": "thanks",
    "bye": "goodbye",
    "goodbye": "goodbye"
}

    if intent in ["unknown", "other", None, ""]:

    # greeting
      if any(x in message_lower for x in ["مرحبا", "اهلا", "هلا", "السلام"]):
        intent = "greeting"

    # how are you
      elif any(x in message_lower for x in ["كيفك", "شلونك", "كيف الحال"]):
        intent = "how_are_you"

    # balance
      elif any(x in message_lower for x in ["رصيدي", "الرصيد", "كم معي"]):
        intent = "balance_transfer"

    # offers
      elif any(x in message_lower for x in ["عروض", "العروض"]):
        intent = "offer_inquiry"

    # data usage
      elif any(x in message_lower for x in ["استهلاك", "البيانات"]):
        intent = "check_data_usage"

    # recharge
      elif any(x in message_lower for x in ["شحن", "اجدد", "تجديد"]):
        intent = "renew_package"

    # payment
      elif any(x in message_lower for x in ["دفع", "ما زبط الدفع"]):
        intent = "payment_issue"

    # internet issues
      elif any(x in message_lower for x in ["النت", "الانترنت", "بطيء", "بعلق", "سيء", "ضعيف"]):
        intent = "slow_internet"

    # signal
      elif any(x in message_lower for x in ["اشاره", "إشارة", "مافي اشاره"]):
        intent = "no_signal"

    # network status
      elif any(x in message_lower for x in ["وضع الشبكه", "حالة الشبكه"]):
        intent = "network_status"

    # 5) Predict sentiment
    try:
        sentiment = predict_sentiment(cleaned_message, lang)
        print("DEBUG sentiment:", sentiment)
    except Exception as e:
        print("⚠️ Sentiment prediction error:", e)
        sentiment = "neutral"

    # 6) Network prediction only if intent is technical/network-related
    prediction = 0
    if intent in NETWORK_INTENTS:
        try:
            prediction_result = predict_network_issue(metrics or {})
            prediction = prediction_result if prediction_result is not None else 0
        except Exception as e:
            print("⚠️ Network prediction error:", e)
            prediction = 0

    # 7) Run decision engine
    try:
        decision = decision_engine(
            intent=intent,
            sentiment=sentiment,
            prediction=prediction,
            preferred_lang=lang
        )
    except Exception as e:
        print("⚠️ Decision engine error:", e)
        decision = {
            "rule_used": "clarification",
            "decision_type": "clarification",
            "severity": "low",
            "escalation": False,
            "route_to": "bot",
            "notify_customer": True,
            "notify_staff": False,
            "notification_channel": "in_app"
        }

    # 8) Build final response from response_utils
    try:
        response_text = build_final_response(
            intent=intent,
            sentiment=sentiment,
            decision=decision,
            lang=lang
        )
    except Exception as e:
        print(" Response builder error:", e)
        response_text = "نعتذر، حدث خطأ أثناء توليد الرد."

    # 9) Send notification if needed
    if decision.get("notify_customer") or decision.get("notify_staff"):
        try:
            send_notification(
                notification_type=decision.get("decision_type", "normal"),
                payload={
                    "message": cleaned_message,
                    "language": lang,
                    "intent": intent,
                    "sentiment": sentiment,
                    "prediction": prediction,
                    "severity": decision.get("severity"),
                    "route_to": decision.get("route_to"),
                    "response": response_text,
                    "notify_customer": decision.get("notify_customer"),
                    "notify_staff": decision.get("notify_staff"),
                    "notification_channel": decision.get("notification_channel")
                }
            )
        except Exception as e:
            print("Notification error:", e)

    # 10) Final output
    return {
        "language": lang,
        "intent": intent,
        "sentiment": sentiment,
        "prediction": prediction,
        "decision": decision,
        "response": response_text
    }

