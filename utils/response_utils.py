import random


RESPONSES = {
    "ar": {
        "balance_transfer": [
            "بدك تحولي رصيد؟ تمام 👌 فيك تعملها من خدمة تحويل الرصيد"
        ],
        "check_data_usage": [
            "بدك تعرف كم ضايل عندك نت؟ 👀 فيك تشوفه من التطبيق بكل سهولة"
        ],
        "goodbye": [
            "يعطيك العافية 🤍 وإذا احتجت شي أنا موجود"
        ],
        "greeting": [
            "هلا وغلا 👋 كيف فيني أساعدك؟",
            "مرحبًا 👋 كيف يمكنني مساعدتك اليوم؟",
            "أهلًا وسهلًا 🌷 كيف أقدر أساعدك؟"
        ],
        "how_are_you": [
            "أنا بخير 😊 كيف أقدر أساعدك؟",
            "تمام، شكرًا لسؤالك 🌷 كيف يمكنني مساعدتك؟"
        ],
        "network_complaint": [
            "تمام، فينا نسجل شكوى ونحل المشكلة مع بعض 👍"
        ],
        "network_status": [
            "بدك تعرف وضع الشبكة؟ 👀 فيك تشوفه من التطبيق"
        ],
        "no_signal": [
            "واضح الشبكة مش راضية تزبط 😅 جرب تطفي الجهاز وتشغله",
            "يبدو أن هناك مشكلة بالإشارة، سأساعدك نتحقق منها."
        ],
        "offer_inquiry": [
            "بدك تشوف العروض؟ 🔥 في كذا عرض حلو، خبرني شو بدك بالزبط",
            "أكيد،أقدر أوضح لك العروض الحالية."
        ],
        "other": [
            "مش واضح عليّ شو قصدك 😅 ممكن توضحلي أكثر؟"
        ],
        "payment_issue": [
            "شكل العملية ما زبطت معك 😕 تأكد من بيانات الدفع وجرب مرة ثانية",
            "واضح أن عندك مشكلة بالدفع، خلينا نحلها."
        ],
        "renew_package": [
            "بدك تشحن؟ 😎 بتقدر تعملها من التطبيق أو بطاقة شحن",
            "أكيد 👍 أقدر أساعدك بتجديد الباقة. أي باقة حابة تجددي؟"
        ],
        "slow_internet": [
            "شكله النت عندك شوي تعبان 😅 جرب تعمل إعادة تشغيل للجهاز وخبرني شو بصير",
            "واضح إن الإنترنت بطيء. جربي أولًا تعملي restart للراوتر."
        ],
        "technical_support": [
            "تمام خلينا نحلها سوا 💪 احكيلي شو المشكلة بالزبط",
            "أكيد، احكيلي تفاصيل المشكلة الفنية وسأساعدك."
        ],
        "feedback": [
            "ولا يهمك 🤍 يسعدني تعليقك، وإذا عندك أي ملاحظة ثانية احكيلي"
        ],
        "thanks": [
            "على الرحب والسعة 🌷",
            "أهلاً فيك، أنا جاهز للمساعدة.",
            "يسعدني مساعدتك 🤍"
        ],
        "clarification": [
           "طلبك غير واضح قليلًا، ممكن توضحه أكثر؟",
           "ممكن توضح أكثر؟",
          "أعطني تفاصيل أكثر حتى أساعدك بشكل أدق."
        ],
        "fallback": [
          "ممكن توضحي طلبك أكثر؟ 🌷",
          "مش واضح عليّ شو قصدك 😅 ممكن توضحلي أكثر؟",
        "لم أفهم طلبك بشكل واضح، هل يمكنك إعادة الصياغة؟"
],

        # decision-based replies
        "critical_escalation": [
            "تم اكتشاف مشكلة حرجة، وتم تصعيد حالتك مباشرة إلى الفريق المختص."
        ],
        "technical_high_risk_reply": [
            "يوجد احتمال لمشكلة فنية عالية الخطورة، وتم تحويل حالتك إلى الفريق الفني."
        ],
        "negative_escalation_reply": [
            "تم تصعيد طلبك إلى خدمة العملاء."
        ]
    },

    "en": {
        "balance_transfer": [
            "Would you like to transfer balance? 👌 You can do that through the balance transfer service."
        ],
        "check_data_usage": [
            "Want to know how much data you have left? 👀 You can check it easily from the app."
        ],
        "goodbye": [
            "Take care 🤍 If you need anything, I’m here."
        ],
        "greeting": [
            "Hello 👋 How can I help you today?",
            "Hi there 👋 What can I help you with today?",
            "Welcome 🌷 How can I assist you?"
        ],
        "how_are_you": [
            "I’m doing well 😊 How can I help you?",
            "I’m good, thanks for asking 🌷 How can I assist you?"
        ],
        "network_complaint": [
            "Sure 👍 We can register a complaint and work on the issue together."
        ],
        "network_status": [
            "Want to check the network status? 👀 You can view it from the app."
        ],
        "no_signal": [
            "Looks like the signal is unstable 😅 Try restarting your device.",
            "There seems to be a signal issue. I can help you check it."
        ],
        "offer_inquiry": [
            "Want to check the offers? 🔥 We have several great options available.",
            "Sure 👍 I can show you the available offers."
        ],
        "other": [
            "I’m not sure I understood 😅 Could you explain more?"
        ],
        "payment_issue": [
            "It looks like the payment did not go through 😕 Please check your payment details and try again.",
            "It seems you’re facing a payment issue. Let’s solve it together."
        ],
        "renew_package": [
            "Want to recharge? 😎 You can do it through the app or a recharge card.",
            "Sure 👍 I can help you renew your package. Which package would you like to renew?"
        ],
        "slow_internet": [
            "Your internet seems a bit slow 😅 Try restarting the router and let me know what happens.",
            "It looks like there is a slow internet issue. Let’s start by checking the connection."
        ],
        "technical_support": [
            "Let’s solve it together 💪 Tell me exactly what issue you’re facing.",
            "Sure, tell me the technical issue and I’ll help you."
        ],
        "feedback": [
            "Thank you 🤍 I appreciate your feedback. Let me know if there’s anything else."
        ],
        "thanks": [
            "You’re welcome 🌷",
            "Glad to help.",
            "Happy to assist 🤍"
        ],
        "clarification": [
            "Your request is a bit unclear. Could you explain more?",
            "Could you clarify your request?",
            "Please give me a bit more detail so I can help better."
        ],
        "fallback": [
            "Could you please explain more?",
            "I didn’t fully understand your request. Could you rephrase it?",
            "Please share a bit more detail so I can help."
        ],

        # decision-based replies
        "critical_escalation": [
            "A critical issue was detected and your case has been escalated immediately."
        ],
        "technical_high_risk_reply": [
            "A high-risk technical issue is likely, and your case has been sent to the technical team."
        ],
        "negative_escalation_reply": [
            "Your request has been escalated to customer support."
        ]
    }
}


FOLLOW_UPS = {
    "ar": {
        "balance_transfer": [
            "بدك خطوات التحويل؟"
        ],
        "check_data_usage": [
        "بدك تعرف كم ضايل عندك نت؟ 👀 فيك تشوفه من التطبيق بكل سهولة",
        "فيك تشوف استهلاكك من التطبيق بسهولة 👍"
],
        "goodbye": [
            "في شي ثاني قبل ما تروح؟ 👀"
        ],
        "greeting": [
            "شو حاب تعرف؟ 😄"
        ],
        "how_are_you": [
            "كيف أقدر أساعدك اليوم؟"
        ],
        "network_complaint": [
            "بدك نكمل تسجيل الشكوى؟"
        ],
        "network_status": [
            "بدك أتحقق لك من الشبكة؟"
        ],
        "no_signal": [
            "بدك نجرب حلول ثانية؟"
        ],
        "offer_inquiry": [
            "بدك أشرح لك العروض المتاحة؟"
        ],
        "other": [
            "ممكن توضح أكثر؟"
        ],
        "payment_issue": [
            "بدك أساعدك نحل المشكلة خطوة خطوة؟"
        ],
        "renew_package": [
            "بدك خطوات الشحن بالتفصيل؟"
        ],
        "slow_internet": [
            "بدك خطوات نحل المشكلة مع بعض؟"
        ],
        "technical_support": [
            "احكيلي شو صاير معك بالزبط 👀"
        ],
        "feedback": [
            "في شي ثاني أقدر أساعدك فيه؟"
        ],
        "thanks": [
            "في شي ثاني أقدر أساعدك فيه؟"
        ]
    },

    "en": {
        "balance_transfer": [
            "Would you like the transfer steps?"
        ],
        "check_data_usage": [
            "Would you like me to show you how to check the details?"
        ],
        "goodbye": [
            "Anything else before you go? 👀"
        ],
        "greeting": [
            "What would you like to know? 😄"
        ],
        "how_are_you": [
            "How can I help you today?"
        ],
        "network_complaint": [
            "Would you like to continue registering the complaint?"
        ],
        "network_status": [
            "Would you like me to check the network for you?"
        ],
        "no_signal": [
            "Would you like to try other solutions?"
        ],
        "offer_inquiry": [
            "Would you like me to explain the available offers?"
        ],
        "other": [
            "Could you explain more?"
        ],
        "payment_issue": [
            "Would you like me to help solve it step by step?"
        ],
        "renew_package": [
            "Would you like the recharge steps in detail?"
        ],
        "slow_internet": [
            "Would you like troubleshooting steps?"
        ],
        "technical_support": [
            "Tell me exactly what’s happening 👀"
        ],
        "feedback": [
            "Anything else I can help you with?"
        ],
        "thanks": [
            "Is there anything else I can help you with?"
        ]
    }
}


ALIASES = {
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
    "thanks": "thanks",
    "thank you": "thanks",
    "bye": "goodbye",
    "goodbye": "goodbye"
}


def normalize_text(text: str) -> str:
    if text is None:
        return ""
    return str(text).strip().lower()


def get_language_bucket(lang: str) -> str:
    return "en" if str(lang).strip().lower() == "en" else "ar"


def apply_alias(intent: str) -> str:
    intent = normalize_text(intent)
    return ALIASES.get(intent, intent)


def random_response(intent: str, lang: str = "ar") -> str:
    lang = get_language_bucket(lang)
    intent = apply_alias(intent)

    responses = RESPONSES[lang].get(intent, RESPONSES[lang]["fallback"])
    return random.choice(responses)


def get_follow_up(intent: str, lang: str = "ar") -> str:
    lang = get_language_bucket(lang)
    intent = apply_alias(intent)

    follow_ups = FOLLOW_UPS[lang].get(intent, [])
    return random.choice(follow_ups) if follow_ups else ""


def sentiment_prefix(sentiment: str, lang: str = "ar") -> str:
    sentiment = normalize_text(sentiment)
    lang = get_language_bucket(lang)

    if lang == "en":
        if sentiment == "negative":
            return "I understand you're facing an issue, "
        if sentiment == "positive":
            return "Happy to help, "
        return ""

    if sentiment == "negative":
        return "واضح أنك تواجه مشكلة، "
    if sentiment == "positive":
        return "يسعدني مساعدتك، "
    return ""


def build_final_response(intent=None, sentiment=None, decision=None, lang="ar") -> str:
    lang = get_language_bucket(lang)

    # 1) decision-based replies first
    if decision and isinstance(decision, dict):
        rule_used = decision.get("rule_used")

        if rule_used == "critical":
            return random.choice(RESPONSES[lang]["critical_escalation"])

        if rule_used == "technical_high_risk":
            return random.choice(RESPONSES[lang]["technical_high_risk_reply"])

        if rule_used == "negative_escalation":
            return random.choice(RESPONSES[lang]["negative_escalation_reply"])

        if rule_used == "clarification":
            main_reply = random.choice(RESPONSES[lang]["clarification"])
            follow_up = get_follow_up("other", lang)
            return f"{main_reply}\n\n{follow_up}" if follow_up else main_reply

    # 2) normal intent-based reply
    intent = apply_alias(intent)
    response_text = random_response(intent, lang)

    print("DEBUG RESPONSE SOURCE:", response_text)

    main_reply = sentiment_prefix(sentiment, lang) + response_text
    follow_up = get_follow_up(intent, lang)

    if follow_up:
        return f"{main_reply}\n\n{follow_up}"

    return main_reply

