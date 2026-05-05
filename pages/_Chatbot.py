def get_bot_reply(user_text):
    text = str(user_text).strip().lower()

    # ردود عربية ثابتة للكويك/التحية إذا الموديل ما رجّع صح
    arabic_fallbacks = {
        "هاي": "هلا وغلا 👋 كيف فيني أساعدك؟\n\nشو حاب تعرف؟",
        "هلا": "هلا وغلا 👋 كيف فيني أساعدك؟\n\nشو حاب تعرف؟",
        "مرحبا": "أهلاً وسهلاً 👋 كيف أقدر أساعدك؟",
        "كيفك": "تمام الحمدلله 👋 كيف أقدر أساعدك؟",
        "افحص حالة الشبكة عندي": "خليني أشيك حالة الشبكة عندك.\n\nأي منطقة موجود فيها؟",
        "بدي أجدد الباقة": "أكيد، بتقدري تجددي الباقة من قسم الباقات.\n\nبدك أساعدك بخطوات التجديد؟",
        "بدي أعرف استهلاك الإنترنت": "بتقدري تشوفي استهلاك الإنترنت من لوحة الحساب.\n\nبدك أشرحلك وين تلاقيه؟",
        "شو العروض المتاحة؟": "العروض الحالية موجودة في قسم العروض والألعاب.\n\nبدك عروض الإنترنت ولا الألعاب؟",
        "بدي أعرف عن المكالمات الدولية": "خيارات المكالمات الدولية متاحة حسب نوع خطك.\n\nبدك تعرفي الأسعار ولا طريقة التفعيل؟",
        "بدي أتواصل مع الدعم الفني": "تمام، رح يتم تحويل طلبك للدعم الفني.\n\nاحكيلي شو المشكلة بالتفصيل؟"
    }

    try:
        result = process_message(
            user_text,
            user_id="customer_1",
            region="Amman"
        )

        response = str(result.get("response", "")).strip()
        followup = str(result.get("followup_response", "")).strip()

        reply = f"{response}\n\n{followup}".strip()

        # إذا الرد طلع عام أو فاضي، استخدم الرد العربي الصح
        bad_replies = [
            "",
            "تم استلام طلبك",
            "تم استلام طلبك.",
            "your request has been received",
            "i received your request."
        ]

        if reply.lower() in bad_replies or "تم استلام طلبك" in reply:
            return arabic_fallbacks.get(text, "ممكن توضحيلي أكثر؟")

        return reply

    except Exception as e:
        return arabic_fallbacks.get(text, f"صار خطأ بالربط:\n{e}")
