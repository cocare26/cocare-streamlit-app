# =========================
# CoCare CLEAN VERSION (Jordan Regions Enabled)
# =========================

from datetime import datetime

# =========================
# JORDAN REGIONS
# =========================
JORDAN_GOVERNORATES = [
    "Amman", "Zarqa", "Irbid", "Balqa", "Madaba", "Karak",
    "Tafilah", "Maan", "Aqaba", "Jerash", "Ajloun", "Mafraq"
]

AR_TO_EN_REGION = {
    "عمان": "Amman",
    "الزرقاء": "Zarqa",
    "إربد": "Irbid",
    "اربد": "Irbid",
    "البلقاء": "Balqa",
    "السلط": "Balqa",
    "مادبا": "Madaba",
    "الكرك": "Karak",
    "الطفيلة": "Tafilah",
    "معان": "Maan",
    "العقبة": "Aqaba",
    "جرش": "Jerash",
    "عجلون": "Ajloun",
    "المفرق": "Mafraq"
}

def normalize_region(region):
    if not region:
        return "Unknown"

    region = str(region).strip()

    # عربي → إنجليزي
    if region in AR_TO_EN_REGION:
        return AR_TO_EN_REGION[region]

    # إنجليزي (case insensitive)
    for gov in JORDAN_GOVERNORATES:
        if region.lower() == gov.lower():
            return gov

    return region


# =========================
# LANGUAGE DETECTION
# =========================
def detect_language(text):
    if any("\u0600" <= c <= "\u06FF" for c in text):
        return "ar"
    return "en"


# =========================
# INTENT
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
# SENTIMENT
# =========================
def predict_sentiment(text, lang):
    t = text.lower()

    if any(w in t for w in ["خرا", "زفت", "سيء", "مشكلة"]):
        return "negative", 0.9

    if any(w in t for w in ["ممتاز", "تمام", "شكرا"]):
        return "positive", 0.9

    return "neutral", 0.5


# =========================
# RESPONSE
# =========================
def get_response(intent, lang, region):

    if intent == "greeting":
        return "هلا وغلا 👋 كيف فيني أساعدك؟", "شو حاب تعرف؟"

    if intent == "slow_internet":
        return f"واضح النت عندك بطيء 😅 في منطقة {region}", "بدك نحلها مع بعض؟"

    if intent == "no_signal":
        return f"واضح في مشكلة بالإشارة 📶 في {region}", "متى بلشت المشكلة؟"

    if intent == "technical_support":
        return "رح يتم تحويلك للدعم الفني 👨‍💻", "احكيلي شو المشكلة؟"

    return "ممكن توضح أكثر؟", "احكيلي تفاصيل أكثر"


# =========================
# MAIN FUNCTION
# =========================
def process_message(user_message, metrics=None, user_id="user_1", region="Unknown"):

    # تنظيف المنطقة
    region = normalize_region(region)

    # تحليل
    lang = detect_language(user_message)
    intent, intent_conf = predict_intent(user_message, lang)
    sentiment, sentiment_score = predict_sentiment(user_message, lang)

    # الرد
    response, followup = get_response(intent, lang, region)

    return {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "user_id": user_id,
        "region": region,
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
