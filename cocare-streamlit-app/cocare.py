# =========================
# CoCare CLEAN VERSION (GitHub Ready)
# =========================

from datetime import datetime

# =========================
# SIMPLE LANGUAGE DETECTION
# =========================
def detect_language(text):
    if any("\u0600" <= c <= "\u06FF" for c in text):
        return "ar"
    return "en"


# =========================
# SIMPLE INTENT
# =========================
def predict_intent(text, lang):
    t = text.lower()

    if any(w in t for w in ["هاي", "هلا", "مرحبا", "hello", "hi"]):
        return "greeting", 0.9

    if any(w in t for w in ["بطيء", "ضعيف", "slow", "سرعة", "النت"]):
        return "slow_internet", 0.9

    if any(w in t for w in ["اشارة", "signal"]):
        return "no_signal", 0.9

    if any(w in t for w in ["دعم", "support"]):
        return "technical_support", 0.9

    return "unknown", 0.5


# =========================
# SIMPLE SENTIMENT
# =========================
def predict_sentiment(text, lang):
    t = text.lower()

    if any(w in t for w in ["خرا", "زفت", "سيء", "مشكلة"]):
        return "negative", 0.9

    if any(w in t for w in ["ممتاز", "تمام", "شكرا"]):
        return "positive", 0.9

    return "neutral", 0.5


# =========================
# RESPONSE LOGIC
# =========================
def get_response(intent, lang):

    if intent == "greeting":
        return "هلا وغلا 👋 كيف فيني أساعدك؟", "شو حاب تعرف؟"

    if intent == "slow_internet":
        return "واضح النت عندك بطيء 😅", "بدك نحلها مع بعض؟"

    if intent == "no_signal":
        return "واضح في مشكلة بالإشارة 📶", "وين موقعك تقريباً؟"

    if intent == "technical_support":
        return "رح يتم تحويلك للدعم الفني 👨‍💻", "احكيلي شو المشكلة؟"

    return "ممكن توضح أكثر؟", "احكيلي تفاصيل أكثر"


# =========================
# MAIN FUNCTION
# =========================
def process_message(user_message, metrics=None, user_id="user_1", region="Amman"):

    lang = detect_language(user_message)

    intent, intent_conf = predict_intent(user_message, lang)

    sentiment, sentiment_score = predict_sentiment(user_message, lang)

    response, followup = get_response(intent, lang)

    return {
        "language": lang,
        "intent": intent,
        "intent_confidence": intent_conf,
        "sentiment": sentiment,
        "sentiment_score": sentiment_score,
        "response": response,
        "followup_response": followup,
        "prediction": 0,
        "issue_type": "normal",
        "network_problem": False
    }
