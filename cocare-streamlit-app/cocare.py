# =========================
# CoCare CLEAN VERSION
# Jordan Regions + Smart Prediction + Chat Logs
# =========================

from datetime import datetime
import os
import pandas as pd

# =========================
# PATHS
# =========================
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(PROJECT_PATH, "data")
CHAT_LOG_PATH = os.path.join(DATA_PATH, "chat_logs.csv")

os.makedirs(DATA_PATH, exist_ok=True)

# =========================
# JORDAN REGIONS
# =========================
JORDAN_GOVERNORATES = [
    "Amman", "Zarqa", "Irbid", "Balqa", "Madaba", "Karak",
    "Tafilah", "Maan", "Aqaba", "Jerash", "Ajloun", "Mafraq"
]

AR_TO_EN_REGION = {
    "عمان": "Amman",
    "عمّان": "Amman",
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

    if region in AR_TO_EN_REGION:
        return AR_TO_EN_REGION[region]

    for gov in JORDAN_GOVERNORATES:
        if region.lower() == gov.lower():
            return gov

    return region

# =========================
# LANGUAGE DETECTION
# =========================
def detect_language(text):
    text = str(text)
    if any("\u0600" <= c <= "\u06FF" for c in text):
        return "ar"
    return "en"

# =========================
# INTENT
# =========================
def predict_intent(text, lang):
    t = str(text).lower()

    if any(w in t for w in ["هاي", "هلا", "مرحبا", "hello", "hi", "كيفك", "كيفو"]):
        return "greeting", 0.9

    if any(w in t for w in [
        "بطيء", "بطئ", "ضعيف", "ضعيفة", "slow", "سرعة", "النت",
        "انترنت", "إنترنت", "تقطيع", "علق", "بفصل", "يفصل"
    ]):
        return "slow_internet", 0.9

    if any(w in t for w in [
        "اشارة", "إشارة", "signal", "شبكة ضعيفة", "ما في شبكة",
        "فاصل", "لا يوجد شبكة", "no signal"
    ]):
        return "no_signal", 0.9

    if any(w in t for w in ["مشكلة شبكة", "الشبكة", "network problem", "network issue"]):
        return "network_complaint", 0.85

    if any(w in t for w in ["دعم", "support", "فني", "مساعدة"]):
        return "technical_support", 0.9

    if any(w in t for w in ["باقة", "تجديد", "bundle", "renew"]):
        return "renew_package", 0.85

    if any(w in t for w in ["استهلاك", "usage", "جيجا", "gb"]):
        return "check_data_usage", 0.85

    if any(w in t for w in ["عروض", "عرض", "offers"]):
        return "offer_inquiry", 0.85

    return "unknown", 0.5

# =========================
# SENTIMENT
# =========================
def predict_sentiment(text, lang):
    t = str(text).lower()

    if any(w in t for w in [
        "خرا", "زفت", "سيء", "سيئة", "مشكلة", "تعبت", "غلط",
        "مش شغال", "ما بشتغل", "بطيء", "ضعيف", "تقطيع", "سيئ"
    ]):
        return "negative", 0.9

    if any(w in t for w in ["ممتاز", "تمام", "شكرا", "يسلمو", "رائع", "good", "great"]):
        return "positive", 0.9

    return "neutral", 0.5

# =========================
# ISSUE TYPE
# =========================
def get_issue_type(intent):
    if intent == "slow_internet":
        return "high_latency"

    if intent == "no_signal":
        return "weak_signal"

    if intent == "network_complaint":
        return "unstable_connection"

    return "normal"

# =========================
# DYNAMIC METRICS
# =========================
def get_dynamic_metrics(user_id, region):
    try:
        logs = pd.read_csv(CHAT_LOG_PATH, encoding="utf-8-sig")
    except Exception:
        return 1, 1

    if logs.empty:
        return 1, 1

    for col in ["user_id", "region", "network_problem"]:
        if col not in logs.columns:
            logs[col] = ""

    network_logs = logs[
        logs["network_problem"].astype(str).str.lower().isin(["true", "1", "yes"])
    ]

    repeat_count = len(
        network_logs[network_logs["user_id"].astype(str) == str(user_id)]
    ) + 1

    area_issue_count = len(
        network_logs[network_logs["region"].astype(str) == str(region)]
    ) + 1

    return repeat_count, area_issue_count

# =========================
# SMART PREDICTION
# =========================
def predict_network_problem(intent, sentiment, repeat_count, area_issue_count):
    network_intents = ["slow_internet", "no_signal", "network_complaint"]

    if intent not in network_intents:
        return 0

    if sentiment == "negative":
        return 1

    if repeat_count >= 2:
        return 1

    if area_issue_count >= 3:
        return 1

    if intent in network_intents:
        return 1

    return 0

# =========================
# RESPONSE
# =========================
def get_response(intent, lang, region, network_problem=False, issue_type="normal"):

    if intent == "greeting":
        return "هلا وغلا 👋 كيف فيني أساعدك؟", "شو حاب تعرف؟"

    if intent == "slow_internet":
        return (
            f"واضح إن في بطء بالإنترنت عندك في منطقة {region} 😅",
            "رح نسجل المشكلة ونشيك حالة الشبكة."
        )

    if intent == "no_signal":
        return (
            f"واضح في مشكلة بالإشارة في منطقة {region} 📶",
            "تم تسجيل المشكلة، ممكن تحكيلي من متى بلشت؟"
        )

    if intent == "network_complaint":
        return (
            f"آسفين على الإزعاج، تم تسجيل مشكلة شبكة في منطقة {region}.",
            "رح يتم متابعة الحالة من فريق الدعم."
        )

    if intent == "technical_support":
        return "رح يتم تحويلك للدعم الفني 👨‍💻", "احكيلي شو المشكلة بالتفصيل؟"

    if intent == "renew_package":
        return "أكيد، بتقدر تجددي الباقة من قسم الباقات.", "بدك أساعدك بخطوات التجديد؟"

    if intent == "check_data_usage":
        return "بتقدري تشوفي استهلاك الإنترنت من لوحة الحساب.", "بدك أعرفك وين مكانها؟"

    if intent == "offer_inquiry":
        return "العروض الحالية متاحة من قسم العروض 🎁", "بدك عروض إنترنت ولا مكالمات؟"

    return "ممكن توضحي أكثر؟", "احكيلي تفاصيل أكثر"

# =========================
# NOTIFICATION
# =========================
def build_notification(intent, issue_type, network_problem, repeat_count, area_issue_count):
    if not network_problem:
        return {
            "notification_type": "none",
            "display_channel": "none",
            "escalation": False,
            "reason": None,
            "show_to_customer": 0,
            "priority": None,
            "suggested_action": None
        }

    escalation = repeat_count >= 3 or area_issue_count >= 3

    if area_issue_count >= 3:
        reason = "Area-wide issue"
    elif repeat_count >= 3:
        reason = "Repeated user issue"
    else:
        reason = "Network problem detected"

    return {
        "notification_type": "internal_noti" if not escalation else "external_noti",
        "display_channel": "employee_dashboard" if not escalation else "customer_app",
        "escalation": escalation,
        "reason": reason,
        "show_to_customer": 1 if escalation else 0,
        "priority": 2 if escalation else 1,
        "suggested_action": issue_type
    }

# =========================
# LOG CHAT
# =========================
def log_chat(user_message, result):
    row = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "user_id": result.get("user_id"),
        "region": result.get("region"),
        "message": user_message,
        "bot_response": result.get("response"),
        "followup_response": result.get("followup_response"),
        "language": result.get("language"),
        "intent": result.get("intent"),
        "intent_confidence": result.get("intent_confidence"),
        "sentiment": result.get("sentiment"),
        "sentiment_score": result.get("sentiment_score"),
        "prediction": result.get("prediction"),
        "issue_type": result.get("issue_type"),
        "network_problem": result.get("network_problem"),
        "notification_type": result.get("notification_type"),
        "display_channel": result.get("display_channel"),
        "escalation": result.get("escalation"),
        "reason": result.get("reason"),
        "repeat_count": result.get("repeat_count"),
        "area_issue_count": result.get("area_issue_count"),
        "show_to_customer": result.get("show_to_customer"),
        "priority": result.get("priority"),
        "suggested_action": result.get("suggested_action")
    }

    df = pd.DataFrame([row])

    if os.path.exists(CHAT_LOG_PATH):
        df.to_csv(CHAT_LOG_PATH, mode="a", header=False, index=False, encoding="utf-8-sig")
    else:
        df.to_csv(CHAT_LOG_PATH, index=False, encoding="utf-8-sig")

# =========================
# MAIN FUNCTION
# =========================
def process_message(user_message, metrics=None, user_id="user_1", region="Unknown"):

    region = normalize_region(region)

    lang = detect_language(user_message)

    intent, intent_conf = predict_intent(user_message, lang)

    sentiment, sentiment_score = predict_sentiment(user_message, lang)

    issue_type = get_issue_type(intent)

    repeat_count, area_issue_count = get_dynamic_metrics(user_id, region)

    prediction = predict_network_problem(
        intent=intent,
        sentiment=sentiment,
        repeat_count=repeat_count,
        area_issue_count=area_issue_count
    )

    network_problem = prediction != 0

    if not network_problem:
        issue_type = "normal"
        repeat_count = 0
        area_issue_count = 0

    response, followup = get_response(
        intent=intent,
        lang=lang,
        region=region,
        network_problem=network_problem,
        issue_type=issue_type
    )

    notification = build_notification(
        intent=intent,
        issue_type=issue_type,
        network_problem=network_problem,
        repeat_count=repeat_count,
        area_issue_count=area_issue_count
    )

    result = {
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
        "prediction": prediction,
        "issue_type": issue_type,
        "network_problem": network_problem,
        "repeat_count": repeat_count,
        "area_issue_count": area_issue_count,
        **notification
    }

    log_chat(user_message, result)

    return result
