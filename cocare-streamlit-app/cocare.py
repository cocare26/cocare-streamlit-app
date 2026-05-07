# =========================
# CoCare Engine - Final Version
# Model Intent + Sentiment + Smart Escalation + Logs
# =========================

from datetime import datetime
import os
import sys
import pandas as pd

# =========================
# SETTINGS
# =========================
INTENT_CONFIDENCE_THRESHOLD = 0.65
SENTIMENT_CONFIDENCE_THRESHOLD = 0.60
LOG_RETENTION_HOURS = 48
USER_REPEAT_THRESHOLD = 3
AREA_REPEAT_THRESHOLD = 3

# =========================
# PATHS
# =========================
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
UTILS_PATH = os.path.join(PROJECT_PATH, "utils")
DATA_PATH = os.path.join(PROJECT_PATH, "data")
CHAT_LOG_PATH = os.path.join(DATA_PATH, "chat_logs.csv")

os.makedirs(DATA_PATH, exist_ok=True)

sys.path.insert(0, PROJECT_PATH)
sys.path.insert(0, UTILS_PATH)

# =========================
# IMPORT UTILS
# =========================
try:
    from utils.language_utils import detect_language
except Exception:
    def detect_language(text):
        return "ar" if any("\u0600" <= c <= "\u06FF" for c in str(text)) else "en"

try:
    from utils.intent_utils import predict_intent as model_predict_intent
except Exception:
    model_predict_intent = None

try:
    from utils.sentiment_utils import predict_sentiment as model_predict_sentiment
except Exception:
    model_predict_sentiment = None

try:
    from utils.response_utils import build_final_response
except Exception:
    build_final_response = None

# =========================
# REGIONS
# =========================
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

JORDAN_GOVERNORATES = [
    "Amman", "Zarqa", "Irbid", "Balqa", "Madaba", "Karak",
    "Tafilah", "Maan", "Aqaba", "Jerash", "Ajloun", "Mafraq"
]


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
# NORMALIZATION
# =========================
def normalize_model_output(result, default_label="unknown"):
    try:
        if isinstance(result, tuple):
            label = result[0] if len(result) > 0 else default_label
            score = result[1] if len(result) > 1 else 1.0
            return str(label).strip().lower(), float(score)

        if isinstance(result, list) and result and isinstance(result[0], dict):
            label = result[0].get("label", default_label)
            score = result[0].get("score", 1.0)
            return str(label).strip().lower(), float(score)

        if isinstance(result, dict):
            label = result.get("label", result.get("intent", result.get("sentiment", default_label)))
            score = result.get("score", result.get("confidence", 1.0))
            return str(label).strip().lower(), float(score)

        return str(result).strip().lower(), 1.0

    except Exception:
        return default_label, 1.0


def normalize_intent(intent):
    intent = str(intent).strip().lower()

    mapping = {
        "slow internet": "slow_internet",
        "slow-internet": "slow_internet",
        "internet_slow": "slow_internet",

        "no signal": "no_signal",
        "no-signal": "no_signal",
        "weak_signal": "no_signal",

        "network complaint": "network_complaint",
        "network status": "network_status",

        "data usage": "check_data_usage",
        "check usage": "check_data_usage",
        "usage": "check_data_usage",

        "offers": "offer_inquiry",
        "offer": "offer_inquiry",

        "renew": "renew_package",
        "recharge": "renew_package",

        "support": "technical_support",
        "technical": "technical_support",

        "international calls": "international_calls",
        "international_calls": "international_calls",
        "calls": "international_calls",

        "unknown": "clarification",
        "other": "clarification",
        "fallback": "clarification",
    }

    return mapping.get(intent, intent)


def normalize_sentiment(sentiment):
    s = str(sentiment).strip().lower()

    if s in ["negative", "neg", "label_0", "0", "سلبي"]:
        return "negative"

    if s in ["positive", "pos", "label_2", "2", "ايجابي", "إيجابي"]:
        return "positive"

    return "neutral"


# =========================
# INTENT / SENTIMENT
# =========================
def predict_intent_safe(text, lang):
    if model_predict_intent is not None:
        try:
            raw = model_predict_intent(text, lang)
            intent, conf = normalize_model_output(raw, "unknown")
            return normalize_intent(intent), conf
        except Exception as e:
            print("INTENT MODEL ERROR:", e)

    t = str(text).lower()

    if t.strip() in ["هاي", "هلا", "مرحبا", "hi", "hello", "كيفك", "كيفو"]:
        return "greeting", 0.8

    if any(w in t for w in ["بطيء", "بطئ", "ضعيف", "النت", "انترنت", "إنترنت", "تقطيع", "بقطع"]):
        return "slow_internet", 0.8

    if any(w in t for w in ["اشارة", "إشارة", "signal", "ما في شبكة", "no signal"]):
        return "no_signal", 0.8

    if any(w in t for w in ["افحص", "فحص", "حالة الشبكة", "وضع الشبكة"]):
        return "network_status", 0.8

    if any(w in t for w in ["استهلاك", "جيجا", "usage", "gb"]):
        return "check_data_usage", 0.8

    if any(w in t for w in ["باقة", "تجديد", "renew"]):
        return "renew_package", 0.8

    if any(w in t for w in ["عروض", "عرض", "offers"]):
        return "offer_inquiry", 0.8

    if any(w in t for w in ["مكالمات", "دولي", "الدولية", "international"]):
        return "international_calls", 0.8

    if any(w in t for w in ["دعم", "فني", "support"]):
        return "technical_support", 0.8

    return "clarification", 0.5


def predict_sentiment_safe(text, lang):
    if model_predict_sentiment is not None:
        try:
            raw = model_predict_sentiment(text, lang)
            sentiment, score = normalize_model_output(raw, "neutral")
            return normalize_sentiment(sentiment), score
        except Exception as e:
            print("SENTIMENT MODEL ERROR:", e)

    t = str(text).lower()

    if any(w in t for w in [
        "خرا", "زفت", "سيء", "سيئة", "مشكلة", "ضعيف",
        "بطيء", "تقطيع", "مش شغال", "ما بشتغل", "تعبت", "زهقت"
    ]):
        return "negative", 0.85

    if any(w in t for w in ["ممتاز", "تمام", "شكرا", "يسلمو", "رائع"]):
        return "positive", 0.85

    return "neutral", 0.5


# =========================
# NETWORK LOGIC
# =========================
def is_real_network_problem_intent(intent):
    return normalize_intent(intent) in [
        "slow_internet",
        "no_signal",
        "network_complaint"
    ]


def map_intent_to_issue_type(intent):
    intent = normalize_intent(intent)

    if intent == "slow_internet":
        return "high_latency"

    if intent == "no_signal":
        return "weak_signal"

    if intent == "network_complaint":
        return "unstable_connection"

    return "normal"

def cleanup_old_logs():
    if not os.path.exists(CHAT_LOG_PATH):
        return

    try:
        logs = pd.read_csv(CHAT_LOG_PATH, encoding="utf-8-sig")

        if logs.empty or "time" not in logs.columns:
            return

        logs["time"] = pd.to_datetime(logs["time"], errors="coerce")

        cutoff_time = datetime.now() - pd.Timedelta(hours=LOG_RETENTION_HOURS)

        logs = logs[
            logs["time"].notna() &
            (logs["time"] >= cutoff_time)
        ]

        logs.to_csv(CHAT_LOG_PATH, index=False, encoding="utf-8-sig")

    except Exception as e:
        print("CLEANUP LOG ERROR:", e)
        
def get_dynamic_metrics(user_id, region):
    cleanup_old_logs()
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


def predict_network_problem(intent):
    if is_real_network_problem_intent(intent):
        return 1
    return 0


def is_angry_customer(user_message, sentiment):
    t = str(user_message).lower()

    angry_words = [
        "خرا", "زفت", "بخزي", "بتخزي", "تعبت", "زهقت", "طفشت",
        "سيء", "سيئة", "مقرف", "مش راضي", "ما بشتغل", "مش شغال",
        "يلعن", "حل عن", "بعدين معك"
    ]

    return sentiment == "negative" or any(w in t for w in angry_words)


# =========================
# DECISION LOGIC
# =========================
def build_decision(
    intent,
    prediction,
    network_problem,
    repeat_count,
    area_issue_count,
    intent_conf,
    angry_customer
):
    if intent == "clarification" or intent_conf < INTENT_CONFIDENCE_THRESHOLD:
        return {"rule_used": "clarification"}

    if not network_problem:
        return {"rule_used": None}

    # المرحلة 3: مشكلة منطقة / تصعيد داخلي
    if area_issue_count >= AREA_REPEAT_THRESHOLD:
        return {"rule_used": "internal_escalation_area"}

    # المرحلة 2: نفس العميل اشتكى 3 مرات / إشعار خارجي
    if repeat_count >= USER_REPEAT_THRESHOLD:
        return {"rule_used": "external_customer_notice"}

    # المرحلة 1: أول/ثاني مرة / تسجيل فقط
    if angry_customer:
        return {"rule_used": "calm_angry_network_user"}

    return {"rule_used": "normal_network_issue"}


# =========================
# NOTIFICATION LOGIC
# =========================
def build_notification(issue_type, network_problem, repeat_count, area_issue_count, angry_customer):
    if not network_problem:
        return {
            "notification_type": "none",
            "display_channel": "none",
            "escalation": False,
            "reason": "No network problem",
            "show_to_customer": 0,
            "priority": None,
            "suggested_action": None
        }

    # المرحلة 1: تسجيل فقط
    if repeat_count < USER_REPEAT_THRESHOLD and area_issue_count < AREA_REPEAT_THRESHOLD:
        return {
            "notification_type": "none",
            "display_channel": "monitoring_log",
            "escalation": False,
            "reason": "Normal monitoring - first reports",
            "show_to_customer": 0,
            "priority": 1,
            "suggested_action": issue_type
        }

    # المرحلة 2: إشعار خارجي للعميل
    if repeat_count >= USER_REPEAT_THRESHOLD and area_issue_count < AREA_REPEAT_THRESHOLD:
        return {
            "notification_type": "external_noti",
            "display_channel": "customer_app",
            "escalation": False,
            "reason": "Repeated issue from same customer",
            "show_to_customer": 1,
            "priority": 2,
            "suggested_action": issue_type
        }

    # المرحلة 3: تصعيد داخلي للموظف + إظهار للعميل
    if area_issue_count >= AREA_REPEAT_THRESHOLD:
        return {
            "notification_type": "internal_noti",
            "display_channel": "employee_dashboard",
            "escalation": True,
            "reason": "Area-wide repeated issue",
            "show_to_customer": 1,
            "priority": 3,
            "suggested_action": issue_type
        }

    return {
        "notification_type": "none",
        "display_channel": "none",
        "escalation": False,
        "reason": "No rule matched",
        "show_to_customer": 0,
        "priority": None,
        "suggested_action": None
    }


# =========================
# RESPONSE LOGIC
# =========================
def get_smart_response(intent, sentiment, decision, lang, region, issue_type, network_problem):
    rule = decision.get("rule_used")

    if rule == "normal_network_issue":
        return (
            f"تم تسجيل ملاحظة بخصوص الشبكة في منطقة {region}، ورح نتابعها.",
            "من متى لاحظت المشكلة؟"
        )

    if rule == "calm_angry_network_user":
        return (
            f"آسفين جدًا على الإزعاج، وفاهمين إن المشكلة مزعجة بالنسبة إلك. "
            f"تم تسجيل ملاحظة الشبكة في منطقة {region} ورح نتابعها.",
            "من متى بدأت المشكلة؟"
        )

    if rule == "external_customer_notice":
        return (
            "لاحظنا إن المشكلة تكررت أكثر من مرة عندك، وتم إرسال تنبيه لمتابعة الحالة.",
            "رح نتابعها معك ونحاول نحلها بأسرع وقت."
        )

    if rule == "internal_escalation_area":
        return (
            f"تم رصد تكرار للمشكلة في منطقة {region}، وتم تصعيد الحالة للفريق المختص.",
            "نعتذر عن الإزعاج ورح تتم المتابعة بأولوية."
        )

    if intent == "network_status":
        return (
            f"أكيد، أقدر أساعدك بفحص حالة الشبكة في منطقة {region}.",
            "هل عندك مشكلة فعلية مثل بطء، تقطيع، أو ضعف إشارة؟"
        )

    if intent == "check_data_usage":
        return "بتقدر تعرف استهلاك الإنترنت من التطبيق من قسم الحساب أو الاستهلاك.", ""

    if intent == "international_calls":
        return "خدمة المكالمات الدولية متاحة حسب نوع خطك. بدك تعرف الأسعار ولا طريقة التفعيل؟", ""

    if intent in ["thanks", "feedback"]:
        return "على الرحب والسعة 🌷 أي وقت تحتاجني أنا موجود.", ""

    if intent == "goodbye":
        return "مع السلامة 👋 أي وقت تحتاجني أنا موجود.", ""

    if build_final_response is not None:
        try:
            final = build_final_response(
                intent=intent,
                sentiment=sentiment,
                decision=decision,
                lang="ar" if lang == "ar" else "en"
            )
            return final, ""
        except Exception as e:
            print("RESPONSE UTILS ERROR:", e)

    if intent == "greeting":
        return "هلا وغلا 👋 كيف فيني أساعدك؟", "شو حاب تعرف؟"

    if intent == "renew_package":
        return "أكيد، بقدر أساعدك بتجديد الباقة.", ""

    if intent == "offer_inquiry":
        return "أكيد، بقدر أوضح لك العروض الحالية.", ""

    if intent == "technical_support":
        return "تمام، احكيلي المشكلة بالتفصيل.", ""

    return "ممكن توضحي أكثر؟", ""


# =========================
# LOGGING
# =========================
def log_chat(user_message, result):
    cleanup_old_logs()
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
        "angry_customer": result.get("angry_customer"),
        "notification_type": result.get("notification_type"),
        "display_channel": result.get("display_channel"),
        "escalation": result.get("escalation"),
        "reason": result.get("reason"),
        "repeat_count": result.get("repeat_count"),
        "area_issue_count": result.get("area_issue_count"),
        "show_to_customer": result.get("show_to_customer"),
        "priority": result.get("priority"),
        "suggested_action": result.get("suggested_action"),
        "decision_rule": result.get("decision_rule")
    }

    df = pd.DataFrame([row])

    if os.path.exists(CHAT_LOG_PATH):
        df.to_csv(CHAT_LOG_PATH, mode="a", header=False, index=False, encoding="utf-8-sig")
    else:
        df.to_csv(CHAT_LOG_PATH, index=False, encoding="utf-8-sig")


# =========================
# MAIN FUNCTION
# =========================
def process_message(user_message, metrics=None, user_id="customer_1", region="Unknown"):
    region = normalize_region(region)
    lang = detect_language(user_message)

    intent, intent_conf = predict_intent_safe(user_message, lang)

    if intent_conf < INTENT_CONFIDENCE_THRESHOLD:
        intent = "clarification"

    sentiment, sentiment_score = predict_sentiment_safe(user_message, lang)

    if sentiment_score < SENTIMENT_CONFIDENCE_THRESHOLD:
        sentiment = "neutral"

    angry_customer = is_angry_customer(user_message, sentiment)

    issue_type = map_intent_to_issue_type(intent)

    repeat_count, area_issue_count = get_dynamic_metrics(user_id, region)

    prediction = predict_network_problem(intent)

    network_problem = prediction != 0

    if not network_problem:
        issue_type = "normal"
        repeat_count = 0
        area_issue_count = 0

    decision = build_decision(
        intent=intent,
        prediction=prediction,
        network_problem=network_problem,
        repeat_count=repeat_count,
        area_issue_count=area_issue_count,
        intent_conf=intent_conf,
        angry_customer=angry_customer
    )

    response, followup = get_smart_response(
        intent=intent,
        sentiment=sentiment,
        decision=decision,
        lang=lang,
        region=region,
        issue_type=issue_type,
        network_problem=network_problem
    )

    notification = build_notification(
        issue_type=issue_type,
        network_problem=network_problem,
        repeat_count=repeat_count,
        area_issue_count=area_issue_count,
        angry_customer=angry_customer
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
        "angry_customer": angry_customer,
        "response": response,
        "followup_response": followup,
        "prediction": prediction,
        "issue_type": issue_type,
        "network_problem": network_problem,
        "repeat_count": repeat_count,
        "area_issue_count": area_issue_count,
        "decision_rule": decision.get("rule_used"),
        **notification
    }

    log_chat(user_message, result)

    return result
