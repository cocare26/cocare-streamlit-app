# =========================
# CoCare - Business Logic & Decision Engine
# Arabic + English Supported Version
# =========================

import re


# -------------------------
# 1) TEXT NORMALIZATION
# -------------------------
def normalize_text(text):
    if text is None:
        return ""

    text = str(text).strip().lower()

    # Arabic normalization
    text = re.sub(r"[إأآا]", "ا", text)
    text = re.sub(r"ى", "ي", text)
    text = re.sub(r"ة", "ه", text)
    text = re.sub(r"ؤ", "و", text)
    text = re.sub(r"ئ", "ي", text)
    text = re.sub(r"ـ", "", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# -------------------------
# 2) THRESHOLDS
# -------------------------
THRESHOLDS = {
    "negative_sentiment": "negative",
    "high_risk_prediction": 1
}


# -------------------------
# 3) ARABIC/ENGLISH LABEL ALIASES
# Canonical labels are English
# -------------------------
INTENT_ALIASES = {
    # Complaint / Technical
    "network_complaint": "network_complaint",
    "شكوى_شبكه": "network_complaint",
    "شكوى شبكه": "network_complaint",
    "network complaint": "network_complaint",

    "slow_internet": "slow_internet",
    "بطء_الانترنت": "slow_internet",
    "بطء الانترنت": "slow_internet",
    "slow internet": "slow_internet",

    "no_signal": "no_signal",
    "لا_توجد_اشاره": "no_signal",
    "لا توجد اشاره": "no_signal",
    "ضعف_اشاره": "no_signal",
    "ضعف اشاره": "no_signal",
    "no signal": "no_signal",
    
    "how_are_you": "how_are_you",
    "كيفك": "how_are_you",
    "شلونك": "how_are_you",
    "كيف الحال": "how_are_you",
    "how are you": "how_are_you",
    
    "technical_support": "technical_support",
    "دعم_فني": "technical_support",
    "دعم فني": "technical_support",
    "technical support": "technical_support",

    # Service intents
    "offer_inquiry": "offer_inquiry",
    "استفسار_عن_العروض": "offer_inquiry",
    "استفسار عن العروض": "offer_inquiry",
    "offer inquiry": "offer_inquiry",

    "renew_package": "renew_package",
    "تجديد_الباقه": "renew_package",
    "تجديد الباقه": "renew_package",
    "تجديد_الباقة": "renew_package",
    "تجديد الباقة": "renew_package",
    "renew package": "renew_package",

    "check_data_usage": "check_data_usage",
    "فحص_استهلاك_البيانات": "check_data_usage",
    "فحص استهلاك البيانات": "check_data_usage",
    "استهلاك_الانترنت": "check_data_usage",
    "استهلاك الانترنت": "check_data_usage",
    "check data usage": "check_data_usage",

    "payment_issue": "payment_issue",
    "مشكله_دفع": "payment_issue",
    "مشكله دفع": "payment_issue",
    "مشكلة_دفع": "payment_issue",
    "مشكلة دفع": "payment_issue",
    "payment issue": "payment_issue",

    "balance_transfer": "balance_transfer",
    "تحويل_رصيد": "balance_transfer",
    "تحويل رصيد": "balance_transfer",
    "balance transfer": "balance_transfer",

    "network_status": "network_status",
    "حاله_الشبكه": "network_status",
    "حاله الشبكه": "network_status",
    "حالة_الشبكة": "network_status",
    "حالة الشبكة": "network_status",
    "network status": "network_status",

    # Normal conversation
    "greeting": "greeting",
    "تحيه": "greeting",
    "ترحيب": "greeting",
    "سلام": "greeting",
    "مرحبا": "greeting",
    "اهلا": "greeting",
    "hello": "greeting",
    "hi": "greeting",

    "goodbye": "goodbye",
    "وداع": "goodbye",
    "مع_السلامه": "goodbye",
    "مع السلامه": "goodbye",
    "bye": "goodbye",
    "goodbye": "goodbye",

    "thanks": "thanks",
    "شكر": "thanks",
    "شكرا": "thanks",
    "شكراً": "thanks",
    "thank you": "thanks",
    "thanks": "thanks",

    # Other
    "other": "other",
    "اخرى": "other",
    "اخرى_": "other",
    "غير_معروف": "other",
    "غير معروف": "other",
    "unknown": "other"
}


SENTIMENT_ALIASES = {
    "positive": "positive",
    "ايجابي": "positive",
    "إيجابي": "positive",

    "neutral": "neutral",
    "محايد": "neutral",

    "negative": "negative",
    "سلبي": "negative",
    "غاضب": "negative",
    "منزعج": "negative"
}


def canonical_intent(intent):
    intent = normalize_text(intent)
    return INTENT_ALIASES.get(intent, intent)


def canonical_sentiment(sentiment):
    sentiment = normalize_text(sentiment)
    return SENTIMENT_ALIASES.get(sentiment, "neutral")


# -------------------------
# 4) INTENT GROUPS
# -------------------------
COMPLAINT_INTENTS = {
    "network_complaint"
}

TECHNICAL_INTENTS = {
    "slow_internet",
    "no_signal",
    "technical_support"
}

SERVICE_INTENTS = {
    "offer_inquiry",
    "renew_package",
    "check_data_usage",
    "payment_issue",
    "balance_transfer",
    "network_status"
}

NORMAL_INTENTS = {
    "greeting",
    "goodbye",
    "thanks",
    "how_are_you"
}

VALID_INTENTS = (
    COMPLAINT_INTENTS
    | TECHNICAL_INTENTS
    | SERVICE_INTENTS
    | NORMAL_INTENTS
    | {"other"}
)


# -------------------------
# 5) RESPONSES
# Bilingual responses
# -------------------------
RESPONSES = {
    "critical_escalation": {
        "en": "We detected a critical issue. Your case has been escalated immediately.",
        "ar": "تم اكتشاف مشكلة حرجة، وتم تصعيد حالتك مباشرة إلى الفريق المختص."
    },
    "technical_escalation": {
        "en": "A technical issue is likely. Your case has been sent to the technical team.",
        "ar": "يوجد احتمال لمشكلة فنية، وتم تحويل حالتك إلى الفريق الفني."
    },
    "support_escalation": {
        "en": "We understand there is an issue. Your request has been escalated to customer support.",
        "ar": "تم فهم وجود مشكلة، وتم تصعيد طلبك إلى خدمة العملاء."
    },
    "technical_standard_reply": {
        "en": "We detected a technical/service issue. Basic support steps will be provided first.",
        "ar": "تم رصد مشكلة فنية أو خدمية، وسيتم تزويدك أولًا بخطوات دعم أساسية."
    },
    "service_reply": {
        "en": "Your request is a normal service request and can be handled automatically.",
        "ar": "طلبك يُعد طلب خدمة عادي ويمكن معالجته تلقائيًا."
    },
    "normal_reply": {
        "en": "Hello. How can I help you today?",
        "ar": "مرحبًا. كيف يمكنني مساعدتك اليوم؟"
    },
    "clarification_reply": {
        "en": "Your request is unclear. Please provide more details.",
        "ar": "طلبك غير واضح. يرجى تزويدي بتفاصيل أكثر."
    },
    "fallback_reply": {
        "en": "We could not classify your request clearly. Please rephrase your message.",
        "ar": "لم نتمكن من تصنيف طلبك بشكل واضح. يرجى إعادة صياغة الرسالة."
    }
}


# -------------------------
# 6) NOTIFICATIONS
# -------------------------
NOTIFICATIONS = {
    "critical": {
        "notify_customer": True,
        "notify_staff": True,
        "channel": "in_app_and_dashboard"
    },
    "technical_high_risk": {
        "notify_customer": True,
        "notify_staff": True,
        "channel": "dashboard"
    },
    "support_escalation": {
        "notify_customer": True,
        "notify_staff": True,
        "channel": "in_app_and_dashboard"
    },
    "standard_support": {
        "notify_customer": True,
        "notify_staff": False,
        "channel": "in_app"
    },
    "normal": {
        "notify_customer": False,
        "notify_staff": False,
        "channel": "none"
    },
    "clarification": {
        "notify_customer": True,
        "notify_staff": False,
        "channel": "in_app"
    }
}


# -------------------------
# 7) DECISION RULES
# -------------------------
DECISION_RULES = {
    "critical": {
        "description": "Negative sentiment + technical/complaint intent + high risk prediction",
        "decision_type": "critical",
        "severity": "critical",
        "escalation": True,
        "route_to": "technical_team",
        "response_key": "critical_escalation",
        "notification_key": "critical"
    },
    "technical_high_risk": {
        "description": "Technical/complaint intent + high risk prediction",
        "decision_type": "technical_issue",
        "severity": "high",
        "escalation": True,
        "route_to": "technical_team",
        "response_key": "technical_escalation",
        "notification_key": "technical_high_risk"
    },
    "negative_escalation": {
        "description": "Negative sentiment needs escalation",
        "decision_type": "customer_support",
        "severity": "high",
        "escalation": True,
        "route_to": "customer_support",
        "response_key": "support_escalation",
        "notification_key": "support_escalation"
    },
    "standard_technical": {
        "description": "Technical/complaint intent without high risk",
        "decision_type": "customer_support",
        "severity": "medium",
        "escalation": False,
        "route_to": "customer_support",
        "response_key": "technical_standard_reply",
        "notification_key": "standard_support"
    },
    "normal_service": {
        "description": "Normal service request",
        "decision_type": "normal",
        "severity": "low",
        "escalation": False,
        "route_to": "bot",
        "response_key": "service_reply",
        "notification_key": "normal"
    },
    "normal_conversation": {
        "description": "Greeting / goodbye / thanks",
        "decision_type": "normal",
        "severity": "low",
        "escalation": False,
        "route_to": "bot",
        "response_key": "normal_reply",
        "notification_key": "normal"
    },
    "clarification": {
        "description": "Unclear or unknown intent",
        "decision_type": "clarification",
        "severity": "low",
        "escalation": False,
        "route_to": "bot",
        "response_key": "clarification_reply",
        "notification_key": "clarification"
    }
}


# -------------------------
# 8) HELPERS
# -------------------------
def detect_response_language(original_intent=None, original_sentiment=None, preferred_lang=None):
    """
    Decide whether the final response should be Arabic or English.
    Priority:
    1) preferred_lang if passed
    2) detect Arabic from original labels
    """
    if preferred_lang in {"ar", "en"}:
        return preferred_lang

    raw_text = f"{original_intent or ''} {original_sentiment or ''}"
    raw_text = str(raw_text)

    arabic_chars = sum(1 for ch in raw_text if '\u0600' <= ch <= '\u06FF')
    return "ar" if arabic_chars > 0 else "en"


def apply_notification(notification_key):
    return NOTIFICATIONS.get(notification_key, {
        "notify_customer": False,
        "notify_staff": False,
        "channel": "none"
    })


def build_output(rule_name, lang="en"):
    rule = DECISION_RULES[rule_name]
    notification = apply_notification(rule["notification_key"])

    response_value = RESPONSES[rule["response_key"]]
    response_text = response_value.get(lang, response_value["en"])

    return {
        "rule_used": rule_name,
        "decision_type": rule["decision_type"],
        "severity": rule["severity"],
        "escalation": rule["escalation"],
        "route_to": rule["route_to"],
        "response": response_text,
        "notify_customer": notification["notify_customer"],
        "notify_staff": notification["notify_staff"],
        "notification_channel": notification["channel"]
    }


# -------------------------
# 9) MAIN DECISION ENGINE
# -------------------------
def decision_engine(intent, sentiment, prediction, preferred_lang=None):
    """
    CoCare Decision Engine

    Inputs:
    - intent: Arabic or English intent label
    - sentiment: Arabic or English sentiment label
    - prediction: 1 = high risk, 0 = not high risk
    - preferred_lang: optional, "ar" or "en" for output response language
    """

    # Handle empty intent
    if intent is None or str(intent).strip() == "":
        lang = detect_response_language(intent, sentiment, preferred_lang)
        return build_output("clarification", lang=lang)

    original_intent = intent
    original_sentiment = sentiment

    intent = canonical_intent(intent)
    sentiment = canonical_sentiment(sentiment)

    lang = detect_response_language(original_intent, original_sentiment, preferred_lang)

    try:
        prediction = int(prediction)
    except Exception:
        prediction = 0

    # Unknown intent -> clarification
    if intent not in VALID_INTENTS:
        return build_output("clarification", lang=lang)

    # Rule 1: Negative sentiment + technical/complaint + high risk
    if (
        sentiment == THRESHOLDS["negative_sentiment"]
        and prediction == THRESHOLDS["high_risk_prediction"]
        and (intent in COMPLAINT_INTENTS or intent in TECHNICAL_INTENTS)
    ):
        return build_output("critical", lang=lang)

    # Rule 2: Technical/complaint + high risk
    if (
        prediction == THRESHOLDS["high_risk_prediction"]
        and (intent in COMPLAINT_INTENTS or intent in TECHNICAL_INTENTS)
    ):
        return build_output("technical_high_risk", lang=lang)

    # Rule 3: Negative sentiment needs escalation
    if sentiment == THRESHOLDS["negative_sentiment"]:
        return build_output("negative_escalation", lang=lang)

    # Rule 4: Technical/complaint without high risk
    if intent in COMPLAINT_INTENTS or intent in TECHNICAL_INTENTS:
        return build_output("standard_technical", lang=lang)

    # Rule 5: Service request
    if intent in SERVICE_INTENTS:
        return build_output("normal_service", lang=lang)

    # Rule 6: Normal conversation
    if intent in NORMAL_INTENTS:
        return build_output("normal_conversation", lang=lang)

    # Rule 7: other / unclear
    return build_output("clarification", lang=lang)

