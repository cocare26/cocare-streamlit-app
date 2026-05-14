import random


RESPONSES = {
    "ar": {
        "balance_transfer": {
            "negative": [
                "نعتذر إن واجهت مشكلة في تحويل الرصيد. يرجى التأكد من الرقم والرصيد المتاح.",
                "واضح أن عندك مشكلة بتحويل الرصيد. خلينا نتحقق من الرقم والرصيد خطوة بخطوة."
            ],
            "neutral": [
                "يمكنك تحويل الرصيد بعد التأكد من الرقم الصحيح وتوفر الرصيد الكافي.",
                "لتحويل الرصيد، تأكد من الرقم والمبلغ ثم أكمل العملية من خدمة تحويل الرصيد."
            ],
            "positive": [
                "يسعدني مساعدتك في تحويل الرصيد. يرجى التأكد من الرقم والمبلغ المطلوب.",
                "أكيد، أقدر أساعدك بتحويل الرصيد بكل سهولة."
            ]
        },

        "check_data_usage": {
            "negative": [
                "نعتذر إن كان استهلاك البيانات غير واضح. يمكنك التحقق من التفاصيل من التطبيق، وإذا ظهرت مشكلة سنساعدك.",
                "واضح أنك تواجه مشكلة بمعرفة استهلاك الإنترنت. خلينا نساعدك تتأكد من الاستهلاك."
            ],
            "neutral": [
                "يمكنك التحقق من استهلاك البيانات الحالي من خلال التطبيق أو صفحة الحساب.",
                "تقدر تعرف كم متبقي من الإنترنت من التطبيق بسهولة."
            ],
            "positive": [
                "أكيد، يمكنك متابعة استهلاك بياناتك بسهولة من التطبيق أو الحساب الشخصي.",
                "يسعدني مساعدتك. بإمكانك معرفة استهلاك البيانات من صفحة حسابك."
            ]
        },

        "goodbye": {
            "negative": [
                "نعتذر عن أي إزعاج، ونتمنى أن نكون قد ساعدناك.",
                "نأسف إن كانت تجربتك غير مرضية. نحن دائمًا جاهزون لمساعدتك."
            ],
            "neutral": [
                "شكرًا لتواصلك معنا. نتمنى لك يومًا سعيدًا.",
                "يعطيك العافية، إذا احتجت أي مساعدة نحن موجودون."
            ],
            "positive": [
                "سعدنا بخدمتك. نتمنى لك يومًا جميلًا.",
                "شكرًا لتواصلك، يسعدنا دائمًا مساعدتك."
            ]
        },

        "greeting": {
            "negative": [
                "أهلًا بك، نعتذر إن كنت تواجه مشكلة. كيف يمكنني مساعدتك؟",
                "مرحبًا، واضح أنك تحتاج مساعدة. احكيلي ما المشكلة؟"
            ],
            "neutral": [
                "أهلًا وسهلًا، كيف يمكنني مساعدتك اليوم؟",
                "مرحبًا، كيف أقدر أساعدك؟"
            ],
            "positive": [
                "أهلًا بك، يسعدني مساعدتك.",
                "مرحبًا، سعيد بتواصلك معنا. كيف أقدر أخدمك؟"
            ]
        },

        "how_are_you": {
            "negative": [
                "أنا بخير، ونعتذر إذا كنت تواجه مشكلة. كيف أقدر أساعدك؟"
            ],
            "neutral": [
                "أنا بخير، شكرًا لسؤالك. كيف يمكنني مساعدتك؟"
            ],
            "positive": [
                "أنا بخير، ويسعدني تواصلك. كيف أقدر أساعدك؟"
            ]
        },

        "network_complaint": {
            "negative": [
                "نعتذر عن تجربتك السيئة. يبدو أن هناك مشكلة شبكة تستدعي المتابعة والتصعيد.",
                "نأسف جدًا للمشكلة التي تواجهها. سيتم التعامل مع الشكوى بجدية ومتابعتها."
            ],
            "neutral": [
                "تم تسجيل ملاحظتك، وسنحتاج بعض التفاصيل الإضافية لمساعدتك بشكل أفضل.",
                "سنقوم بمتابعة شكوى الشبكة، يرجى تزويدنا بتفاصيل أكثر."
            ],
            "positive": [
                "شكرًا لتواصلك. سنقوم بمتابعة ملاحظتك وتحسين الخدمة قدر الإمكان.",
                "يسعدنا اهتمامك بتحسين الخدمة، وسنأخذ ملاحظتك بعين الاعتبار."
            ]
        },

        "network_status": {
            "negative": [
                "نعتذر، يبدو أن هناك خللًا أو ضغطًا محتملًا على الشبكة في الوقت الحالي.",
                "نأسف للإزعاج، قد تكون هناك مشكلة مؤقتة في الشبكة وسنقوم بمتابعتها."
            ],
            "neutral": [
                "يمكنك التحقق من حالة الشبكة في منطقتك من خلال التطبيق أو صفحة الخدمة.",
                "حالة الشبكة تبدو طبيعية حاليًا، وإذا استمرت المشكلة يمكننا متابعتها."
            ],
            "positive": [
                "الشبكة تبدو مستقرة حاليًا. يسعدنا تواصلك معنا.",
                "يسعدني مساعدتك في التحقق من حالة الشبكة."
            ]
        },

        "no_signal": {
            "negative": [
                "نعتذر عن انقطاع الإشارة. قد تكون هناك مشكلة تغطية أو عطل مؤقت في منطقتك، وسيتم تصعيد الحالة.",
                "نأسف لمشكلة الإشارة. يرجى إعادة تشغيل الجهاز وسنقوم بمتابعة الحالة إذا استمرت."
            ],
            "neutral": [
                "يرجى تجربة تغيير المكان أو إعادة تشغيل الهاتف للتأكد من عودة الإشارة.",
                "يبدو أن هناك مشكلة بالإشارة. جرّب إعادة تشغيل الجهاز أو الانتقال لمكان مفتوح."
            ],
            "positive": [
                "يسعدنا تواصلك. إذا واجهت ضعفًا في الإشارة، جرّب إعادة تشغيل الجهاز أو الانتقال لمكان مفتوح.",
                "أكيد، أقدر أساعدك في التحقق من مشكلة الإشارة."
            ]
        },

        "offer_inquiry": {
            "negative": [
                "نعتذر إن لم تكن العروض واضحة. يمكننا مساعدتك في معرفة العروض المتاحة لحسابك.",
                "نأسف إذا لم تجد العرض المناسب. يمكننا توضيح العروض المتاحة لك."
            ],
            "neutral": [
                "يمكنك الاطلاع على العروض المتاحة حاليًا من خلال التطبيق أو صفحة العروض.",
                "توجد عدة عروض متاحة، ويمكنك اختيار الأنسب حسب حاجتك."
            ],
            "positive": [
                "يسعدنا اهتمامك بالعروض. يمكنك مشاهدة أحدث العروض المناسبة لك من التطبيق.",
                "أكيد، أقدر أساعدك بمعرفة العروض المتاحة."
            ]
        },

        "payment_issue": {
            "negative": [
                "نعتذر عن مشكلة الدفع. يرجى التأكد من الرصيد أو البطاقة أو تجربة وسيلة دفع أخرى.",
                "نأسف لتعطل عملية الدفع. قد تكون هناك مشكلة مؤقتة، وسنساعدك بحلها."
            ],
            "neutral": [
                "يمكنك التأكد من بيانات الدفع والمحاولة مرة أخرى بعد قليل.",
                "يرجى التحقق من وسيلة الدفع والرصيد ثم إعادة المحاولة."
            ],
            "positive": [
                "يسعدنا مساعدتك في عملية الدفع. يرجى التأكد من صحة البيانات والمحاولة مرة أخرى.",
                "أكيد، أقدر أساعدك في إتمام عملية الدفع."
            ]
        },

        "renew_package": {
            "negative": [
                "نعتذر إن واجهت مشكلة في تجديد الباقة. يرجى التأكد من توفر الرصيد ثم المحاولة مرة أخرى.",
                "نأسف لتعطل تجديد الباقة. خلينا نتحقق من الرصيد وطريقة التجديد."
            ],
            "neutral": [
                "يمكنك تجديد الباقة من خلال التطبيق أو خدمة الدفع المتاحة لديك.",
                "لتجديد الباقة، تأكد من توفر الرصيد ثم اختر الباقة المطلوبة."
            ],
            "positive": [
                "يسعدنا مساعدتك في تجديد الباقة. يمكنك إتمام التجديد من التطبيق أو الحساب.",
                "أكيد، أقدر أساعدك بتجديد الباقة."
            ]
        },

        "slow_internet": {
            "negative": [
                "نعتذر عن بطء الإنترنت، واضح أنك تواجه مشكلة مزعجة. خلينا نساعدك خطوة بخطوة.",
                "نأسف للإزعاج بسبب بطء الإنترنت. يرجى تجربة إعادة تشغيل الراوتر، وإذا استمرت المشكلة سنقوم بمتابعتها."
            ],
            "neutral": [
                "يبدو أن الإنترنت بطيء. جرّب إعادة تشغيل الراوتر ثم أخبرني إذا استمرت المشكلة.",
                "يمكنك تجربة إغلاق التطبيقات التي تستهلك الإنترنت بكثرة ثم إعادة اختبار السرعة."
            ],
            "positive": [
                "يسعدني مساعدتك بخصوص سرعة الإنترنت. خلينا نتحقق من الاتصال.",
                "أكيد، أقدر أساعدك بتحسين سرعة الإنترنت."
            ]
        },

        "technical_support": {
            "negative": [
                "نعتذر عن المشكلة التي تواجهك. سيتم تصعيد الحالة للدعم الفني لمتابعتها بأسرع وقت.",
                "نأسف للإزعاج، يرجى تزويدنا بتفاصيل المشكلة حتى يتمكن الدعم الفني من مساعدتك."
            ],
            "neutral": [
                "يرجى تزويدنا بتفاصيل أكثر عن المشكلة حتى يتمكن الدعم الفني من مساعدتك.",
                "أرسل تفاصيل المشكلة الفنية وسنرشدك للحل المناسب."
            ],
            "positive": [
                "يسعدنا مساعدتك. أرسل لنا تفاصيل المشكلة وسنرشدك للحل المناسب.",
                "أكيد، فريق الدعم جاهز لمساعدتك."
            ]
        },

        "feedback": {
            "negative": [
                "نعتذر عن تجربتك غير المرضية، وسيتم أخذ ملاحظتك بجدية لتحسين الخدمة.",
                "نأسف لسماع ذلك. ملاحظتك مهمة وسيتم التعامل معها بجدية."
            ],
            "neutral": [
                "شكرًا لملاحظتك، سيتم أخذها بعين الاعتبار.",
                "نقدّر ملاحظتك وسنستخدمها لتحسين الخدمة."
            ],
            "positive": [
                "شكرًا لملاحظتك الإيجابية، يسعدنا رضاك عن الخدمة.",
                "يسعدنا أن تجربتك كانت جيدة، شكرًا لملاحظتك."
            ]
        },

        "thanks": {
            "negative": [
                "العفو، ونعتذر عن أي إزعاج واجهته.",
                "على الرحب والسعة، وإذا بقيت المشكلة مستمرة نحن جاهزون للمساعدة."
            ],
            "neutral": [
                "على الرحب والسعة.",
                "أهلاً بك، أنا جاهز للمساعدة."
            ],
            "positive": [
                "يسعدني مساعدتك.",
                "أهلًا وسهلًا، سعيد أني قدرت أساعدك."
            ]
        },

        "other": {
            "negative": [
                "نعتذر، لم أتمكن من فهم طلبك بشكل واضح. هل يمكنك توضيح المشكلة أكثر؟",
                "أعتذر، طلبك غير واضح بالنسبة لي. ممكن تشرح المشكلة بطريقة ثانية؟"
            ],
            "neutral": [
                "لم أفهم طلبك بدقة. هل يمكنك توضيح ما تحتاجه؟",
                "ممكن توضح طلبك أكثر حتى أساعدك بشكل صحيح؟"
            ],
            "positive": [
                "يسعدني مساعدتك، لكن أحتاج توضيحًا أكثر لطلبك.",
                "أكيد، أقدر أساعدك. ممكن توضح المطلوب أكثر؟"
            ]
        },

        "clarification": {
            "negative": [
                "نعتذر، طلبك غير واضح قليلًا. هل يمكنك توضيح المشكلة أكثر؟"
            ],
            "neutral": [
                "طلبك غير واضح قليلًا، ممكن توضحه أكثر؟",
                "أعطني تفاصيل أكثر حتى أساعدك بشكل أدق."
            ],
            "positive": [
                "يسعدني مساعدتك، فقط أحتاج توضيحًا أكثر."
            ]
        },

        "fallback": {
            "negative": [
                "نعتذر، لم أفهم طلبك بشكل واضح. هل يمكنك إعادة صياغته؟"
            ],
            "neutral": [
                "ممكن توضح طلبك أكثر؟",
                "لم أفهم طلبك بشكل واضح، هل يمكنك إعادة الصياغة؟"
            ],
            "positive": [
                "يسعدني مساعدتك، لكن أحتاج تفاصيل أكثر عن طلبك."
            ]
        },

        "critical_escalation": [
            "تم اكتشاف مشكلة حرجة، وتم تصعيد حالتك مباشرة إلى الفريق المختص."
        ],
        "technical_high_risk_reply": [
            "يوجد احتمال لمشكلة فنية عالية الخطورة، وتم تحويل حالتك إلى الفريق الفني."
        ],
        "negative_escalation_reply": [
            "تم تصعيد طلبك إلى خدمة العملاء بسبب وجود مؤشرات على عدم رضا أو مشكلة متكررة."
        ],
        "prediction_network_issue": [
            "توجد مؤشرات على وجود مشكلة في الشبكة حاليًا، وسيتم متابعة الحالة من قبل الفريق المختص."
        ]
    },

    "en": {
        "fallback": {
            "negative": [
                "I’m sorry, I could not clearly understand your request. Could you rephrase it?"
            ],
            "neutral": [
                "Could you please explain your request more clearly?"
            ],
            "positive": [
                "I’m happy to help, but I need a bit more detail."
            ]
        },
        "critical_escalation": [
            "A critical issue was detected and your case has been escalated immediately."
        ],
        "technical_high_risk_reply": [
            "A high-risk technical issue is likely, and your case has been sent to the technical team."
        ],
        "negative_escalation_reply": [
            "Your request has been escalated to customer support."
        ],
        "prediction_network_issue": [
            "There are signs of a network issue, and the case will be followed up by the technical team."
        ]
    }
}


FOLLOW_UPS = {
    "ar": {
        "balance_transfer": [
            "هل تريد خطوات تحويل الرصيد؟",
            "هل الرقم الذي تريد التحويل له صحيح؟"
        ],
        "check_data_usage": [
            "هل تريد معرفة الاستهلاك الحالي أم تفاصيل الاستهلاك؟",
            "هل تريد معرفة كم تبقى من الباقة؟"
        ],
        "goodbye": [
            "هل يوجد أي شيء آخر قبل إنهاء المحادثة؟"
        ],
        "greeting": [
            "كيف يمكنني مساعدتك اليوم؟"
        ],
        "how_are_you": [
            "كيف أقدر أساعدك اليوم؟"
        ],
        "network_complaint": [
            "هل المشكلة متكررة منذ فترة أم حدثت اليوم فقط؟",
            "هل تريد تسجيل الشكوى ومتابعتها؟"
        ],
        "network_status": [
            "هل تريد معرفة حالة الشبكة في منطقتك؟",
            "هل تواجه مشكلة حاليًا في الاتصال؟"
        ],
        "no_signal": [
            "هل المشكلة داخل المنزل فقط أم في كل الأماكن؟",
            "هل جربت إعادة تشغيل الجهاز؟"
        ],
        "offer_inquiry": [
            "هل تبحث عن عروض إنترنت أم مكالمات أم باقات شاملة؟",
            "هل تريد عرضًا شهريًا أم يوميًا؟"
        ],
        "other": [
            "هل تقصد مشكلة في الإنترنت أو الدفع أو الباقة؟"
        ],
        "payment_issue": [
            "هل ظهرت لك رسالة خطأ أثناء الدفع؟",
            "هل المشكلة من البطاقة أم من التطبيق؟"
        ],
        "renew_package": [
            "هل تريد تجديد نفس الباقة أم اختيار باقة جديدة؟",
            "هل يوجد رصيد كافٍ للتجديد؟"
        ],
        "slow_internet": [
            "هل البطء يحدث طوال الوقت أم في أوقات محددة؟",
            "هل جرّبت إعادة تشغيل الراوتر؟"
        ],
        "technical_support": [
            "هل يمكنك توضيح المشكلة التي تواجهك بشكل أكبر؟",
            "متى بدأت المشكلة بالضبط؟"
        ],
        "feedback": [
            "هل ترغب بإضافة تفاصيل أكثر حول ملاحظتك؟"
        ],
        "thanks": [
            "هل يوجد أي شيء آخر أستطيع مساعدتك به؟"
        ]
    },

    "en": {
        "other": [
            "Do you mean an internet, payment, or package issue?"
        ]
    }
}


ALIASES = {
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


def normalize_sentiment(sentiment: str) -> str:
    sentiment = normalize_text(sentiment)

    if sentiment in ["positive", "pos", "label_2", "2"]:
        return "positive"

    if sentiment in ["negative", "neg", "label_0", "0"]:
        return "negative"

    return "neutral"


def apply_alias(intent: str) -> str:
    intent = normalize_text(intent)
    return ALIASES.get(intent, intent)


def choose_from_block(block, sentiment="neutral"):
    sentiment = normalize_sentiment(sentiment)

    if isinstance(block, dict):
        responses = block.get(sentiment)

        if not responses:
            responses = block.get("neutral")

        if not responses:
            responses = []

        return random.choice(responses) if responses else ""

    if isinstance(block, list):
        return random.choice(block) if block else ""

    return ""


def random_response(intent: str, sentiment: str = "neutral", lang: str = "ar") -> str:
    lang = get_language_bucket(lang)
    intent = apply_alias(intent)
    sentiment = normalize_sentiment(sentiment)

    lang_responses = RESPONSES.get(lang, RESPONSES["ar"])

    intent_block = lang_responses.get(intent)

    if intent_block is None:
        intent_block = lang_responses.get("fallback", RESPONSES["ar"]["fallback"])

    response = choose_from_block(intent_block, sentiment)

    if not response:
        response = choose_from_block(RESPONSES["ar"]["fallback"], sentiment)

    return response


def get_follow_up(intent: str, sentiment: str = "neutral", lang: str = "ar") -> str:
    lang = get_language_bucket(lang)
    intent = apply_alias(intent)
    sentiment = normalize_sentiment(sentiment)

    if sentiment == "negative":
        if lang == "ar":
            negative_followups = {
                "slow_internet": "هل المشكلة مستمرة الآن؟ خلينا نساعدك بحلها بأسرع وقت.",
                "no_signal": "هل انقطاع الإشارة مستمر في نفس المكان؟",
                "payment_issue": "هل ظهرت لك رسالة خطأ أثناء محاولة الدفع؟",
                "network_complaint": "هل المشكلة متكررة منذ فترة طويلة؟",
                "technical_support": "هل يمكنك إرسال تفاصيل أكثر حتى يتم تصعيد الحالة بشكل صحيح؟",
                "renew_package": "هل فشلت عملية التجديد أم لم يظهر الرصيد؟",
                "other": "هل تقصد مشكلة في الإنترنت أو الدفع أو الباقة؟"
            }
            return negative_followups.get(
                intent,
                "هل المشكلة مستمرة؟ خلينا نساعدك بحلها بأسرع وقت."
            )

        return "Is the issue still happening? Let’s help you solve it as soon as possible."

    follow_ups = FOLLOW_UPS.get(lang, FOLLOW_UPS["ar"]).get(intent, [])

    return random.choice(follow_ups) if follow_ups else ""


def sentiment_prefix(sentiment: str, lang: str = "ar") -> str:
    sentiment = normalize_sentiment(sentiment)
    lang = get_language_bucket(lang)

    if lang == "en":
        if sentiment == "negative":
            return "I understand you're facing an issue. "
        if sentiment == "positive":
            return "Happy to help. "
        return ""

    if sentiment == "negative":
        return "واضح أنك تواجه مشكلة. "
    if sentiment == "positive":
        return "يسعدني مساعدتك. "
    return ""


def extract_prediction_from_decision(decision):
    if not decision or not isinstance(decision, dict):
        return 0

    for key in ["prediction", "network_prediction", "prediction_result", "has_network_issue"]:
        if key in decision:
            try:
                return int(decision.get(key))
            except Exception:
                return 0

    return 0


def build_final_response(intent=None, sentiment=None, decision=None, lang="ar") -> str:
    lang = get_language_bucket(lang)
    sentiment = normalize_sentiment(sentiment)
    intent = apply_alias(intent)

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
            main_reply = random_response("clarification", sentiment, lang)
            follow_up = get_follow_up("other", sentiment, lang)
            return f"{main_reply}\n\n{follow_up}" if follow_up else main_reply

    # 2) prediction-based reply
    prediction_flag = extract_prediction_from_decision(decision)

    if prediction_flag == 1 and intent in [
        "slow_internet",
        "network_complaint",
        "network_status",
        "no_signal",
        "technical_support"
    ]:
        main_reply = random.choice(RESPONSES[lang]["prediction_network_issue"])
        follow_up = get_follow_up(intent, sentiment, lang)
        return f"{main_reply}\n\n{follow_up}" if follow_up else main_reply

    # 3) normal intent-based reply
    response_text = random_response(intent, sentiment, lang)

    # لأن الردود نفسها صارت حسب sentiment، ما بدنا نكرر prefix كثير
    main_reply = response_text

    follow_up = get_follow_up(intent, sentiment, lang)

    if follow_up:
        return f"{main_reply}\n\n{follow_up}"

    return main_reply
