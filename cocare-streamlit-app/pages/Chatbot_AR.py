import streamlit as st
import base64
import os
import sys
import html as html_lib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cocare import process_message

st.set_page_config(page_title="المساعد الذكي", layout="centered")

CHAT_KEY = "chat_ar_messages"
CONTEXT_KEY = "chat_context"

if "region" not in st.session_state:
    st.session_state["region"] = "عمان"

if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = [
        ("bot", "مرحبًا 👋 كيف أقدر أساعدك؟")
    ]

if CONTEXT_KEY not in st.session_state:
    st.session_state[CONTEXT_KEY] = {
        "last_intent": None,
        "awaiting_details": False,
        "last_network_problem": False
    }


def reset_context():
    st.session_state[CONTEXT_KEY] = {
        "last_intent": None,
        "awaiting_details": False,
        "last_network_problem": False
    }


def img_to_base64(path):
    try:
        full_path = os.path.join(os.path.dirname(__file__), "..", path)
        if os.path.exists(full_path):
            with open(full_path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    except Exception:
        pass
    return ""


robot = img_to_base64("robot_head.png") or img_to_base64("robot.png")


def is_thanks_or_close(text):
    t = str(text).strip().lower()
    return any(p in t for p in [
        "شكرا", "شكراً", "يسلمو", "مشكور", "يعطيك العافية",
        "تمام", "ماشي", "اوكي", "ok", "okay", "thanks", "thank you"
    ])


def is_goodbye(text):
    t = str(text).strip().lower()
    return any(p in t for p in ["باي", "مع السلامة", "سلام", "bye", "goodbye"])


def is_no_problem(text):
    t = str(text).strip().lower()
    return any(p in t for p in [
        "ما عندي مشكلة", "ما عندي مشكله",
        "لا ما عندي مشكلة", "لا ما عندي مشكله",
        "خلص ما عندي مشكلة", "خلص ما عندي مشكله",
        "ما في مشكلة", "مافي مشكلة",
        "ما عندي اشي", "ولا اشي"
    ])


def is_social_positive(text):
    t = str(text).strip().lower()
    return any(p in t for p in [
        "كفو", "غالي", "يا غالي", "حبيبي", "تسلم",
        "يسعدك", "يعطيك العافية", "نورت", "مشكور"
    ])


def is_short_followup(text):
    return len(str(text).strip().split()) <= 8


def looks_like_time_answer(text):
    t = str(text).lower()
    return any(w in t for w in [
        "ساعة", "الساعه", "الصبح", "المسا", "المساء",
        "اليوم", "امبارح", "من شوي", "دقيقة", "دقايق",
        "يوم", "يومين", "اسبوع", "أسبوع", "من 8", "من ٩", "من 9"
    ])


def looks_like_yes(text):
    return str(text).strip().lower() in [
        "اه", "آه", "نعم", "ايوه", "أيوه", "yes", "ok", "تمام", "مزبوط"
    ]


def looks_like_no(text):
    return str(text).strip().lower() in ["لا", "لأ", "no", "مش"]


def looks_like_location(text):
    t = str(text).strip().lower()
    locations = [
        "عمان", "عمّان", "الزرقاء", "اربد", "إربد", "البلقاء",
        "مادبا", "الكرك", "الطفيلة", "معان", "العقبة",
        "جرش", "عجلون", "المفرق"
    ]
    return any(loc in t for loc in locations)


def human_fallback_reply(text):
    t = str(text).strip().lower()

    if is_no_problem(t):
        reset_context()
        return "تمام، ولا يهمك 🌷 إذا احتجت أي مساعدة أنا موجود."

    if is_thanks_or_close(t):
        reset_context()
        return "على الرحب والسعة 🌷 أي وقت تحتاجني أنا موجود."

    if is_goodbye(t):
        reset_context()
        return "مع السلامة 👋 أي وقت تحتاجني أنا موجود."

    if is_social_positive(t):
        reset_context()
        return "الله يسعدك 🌷 أنا موجود بأي وقت تحتاج مساعدة."

    if "المكالمات الدولية" in t or "دولي" in t or "مكالمات" in t:
        return "خدمة المكالمات الدولية متاحة حسب نوع خطك. بدك تعرف الأسعار ولا طريقة التفعيل؟"

    if "استهلاك" in t or "جيجا" in t or "النت المتبقي" in t:
        return "بتقدر تعرف استهلاك الإنترنت من التطبيق من قسم الحساب أو الاستهلاك."

    if "تجديد" in t or "باقة" in t:
        return "أكيد، بتقدر تجدد الباقة من قسم الباقات داخل التطبيق."

    if "عرض" in t or "عروض" in t:
        return "العروض الحالية متاحة من قسم العروض 🎁 بدك عروض إنترنت ولا مكالمات؟"

    if any(w in t for w in ["مين انت", "انت مين", "شو بتعمل", "what are you", "who are you"]):
        return (
            "أنا مساعد CoCare الذكي 🤖\n\n"
            "بقدر أساعدك بالشبكة، الباقات، استهلاك الإنترنت، العروض، المكالمات الدولية، والدعم الفني."
        )

    if any(w in t for w in ["مساعدة", "ساعدني", "help", "بدي مساعدة"]):
        return (
            "أكيد، أنا معك خطوة بخطوة.\n\n"
            "احكيلي سؤالك عن شو: الشبكة، الباقة، الاستهلاك، العروض، المكالمات الدولية، أو الدعم الفني؟"
        )

    if any(w in t for w in ["كيف", "طريقة", "كيف اعمل", "كيف أعمل"]):
        return (
            "أكيد بساعدك. بس حدديلي الخدمة اللي بدك طريقتها:\n\n"
            "تجديد الباقة، معرفة الاستهلاك، فحص الشبكة، العروض، أو التواصل مع الدعم؟"
        )

    if any(w in t for w in ["وين", "أين", "مكان"]):
        return (
            "ممكن توضحيلي عن أي مكان بتحكي؟\n\n"
            "مكان الباقات، الاستهلاك، الدعم، العروض، أو إعدادات التطبيق؟"
        )

    return (
        "فهمت عليك، بس بدي تفاصيل أكثر شوي حتى أساعدك صح.\n\n"
        "هل سؤالك عن الشبكة، الباقة، الاستهلاك، العروض، المكالمات الدولية، أو الدعم الفني؟"
    )


def handle_context_followup(text):
    context = st.session_state[CONTEXT_KEY]
    msg = str(text).strip()

    if not context.get("awaiting_details"):
        return None

    if is_no_problem(msg):
        reset_context()
        return "تمام، ولا يهمك 🌷 ما رح أسجل مشكلة. إذا احتجت أي مساعدة أنا موجود."

    if is_thanks_or_close(msg):
        reset_context()
        return "على الرحب والسعة 🌷 أي وقت تحتاجني أنا موجود."

    if not is_short_followup(msg):
        return None

    reset_context()

    if looks_like_time_answer(msg):
        return (
            "تمام، هيك وضحت الصورة ✅\n\n"
            "سجلت مدة/وقت بداية المشكلة، ورح نتابع حالة الشبكة مع الفريق المختص."
        )

    if looks_like_location(msg):
        return (
            "تمام، وصلتني المنطقة ✅\n\n"
            "رح أضيفها على تفاصيل المشكلة وأتابعها مع الفريق المختص."
        )

    if looks_like_yes(msg):
        return (
            "تمام، خلينا نكمل خطوة خطوة.\n\n"
            "جرّب/ي إعادة تشغيل الراوتر أو تفعيل وضع الطيران لمدة 10 ثواني، وبعدها احكيلي إذا تحسّن الوضع."
        )

    if looks_like_no(msg):
        return (
            "تمام ولا يهمك.\n\n"
            "رح أسجل المشكلة بدون خطوات إضافية، وإذا استمرت رح يتم متابعتها من الفريق المختص."
        )

    return (
        "تمام، وصلتني التفاصيل ✅\n\n"
        "رح أضيفها على المشكلة المسجلة وأتابعها مع الفريق المختص."
    )


def direct_service_reply(text):
    t = str(text).strip().lower()
    region = st.session_state.get("region", "عمان")

    if t == "فحص الشبكة":
        reset_context()
        return (
            f"أكيد، أقدر أساعدك بفحص حالة الشبكة في منطقة {region}.\n\n"
            "هل عندك مشكلة فعلية مثل بطء، تقطيع، أو ضعف إشارة؟"
        )

    if t == "استهلاك الإنترنت":
        reset_context()
        return "بتقدر تعرف استهلاك الإنترنت من التطبيق من قسم الحساب أو الاستهلاك."

    if t == "تجديد الباقة":
        reset_context()
        return "أكيد، بتقدر تجدد الباقة من قسم الباقات داخل التطبيق. بدك خطوات التجديد؟"

    if t == "المكالمات الدولية":
        reset_context()
        return "خدمة المكالمات الدولية متاحة حسب نوع خطك. بدك تعرف الأسعار ولا طريقة التفعيل؟"

    if t == "العروض":
        reset_context()
        return "العروض الحالية متاحة من قسم العروض 🎁 بدك عروض إنترنت ولا مكالمات؟"

    if t == "الدعم":
        reset_context()
        return "أكيد، احكيلي تفاصيل المشكلة الفنية وسأساعدك خطوة بخطوة."

    return None


def get_bot_reply(user_text):
    msg = str(user_text).strip()

    if is_no_problem(msg):
        reset_context()
        return "تمام، ولا يهمك 🌷 إذا احتجت أي مساعدة أنا موجود."

    if is_thanks_or_close(msg):
        reset_context()
        return "على الرحب والسعة 🌷 أي وقت تحتاجني أنا موجود."

    if is_goodbye(msg):
        reset_context()
        return "مع السلامة 👋 أي وقت تحتاجني أنا موجود."

    if is_social_positive(msg):
        reset_context()
        return "الله يسعدك 🌷 أنا موجود بأي وقت تحتاج مساعدة."

    service_reply = direct_service_reply(msg)
    if service_reply:
        return service_reply

    context_reply = handle_context_followup(msg)
    if context_reply:
        return context_reply

    user_id = st.session_state.get("user_id", "customer_1")
    region = st.session_state.get("region", "عمان")

    try:
        result = process_message(
            msg,
            user_id=user_id,
            region=region
        )

        intent = result.get("intent", "")
        network_problem = result.get("network_problem", False)

        st.session_state[CONTEXT_KEY]["last_intent"] = intent
        st.session_state[CONTEXT_KEY]["last_network_problem"] = network_problem
        st.session_state[CONTEXT_KEY]["awaiting_details"] = bool(network_problem)

        if intent in ["clarification", "unknown", "other", "fallback"]:
            reset_context()
            return human_fallback_reply(msg)

        response = str(result.get("response", "")).strip()
        followup = str(result.get("followup_response", "")).strip()
        reply = f"{response}\n\n{followup}".strip()

        if not reply:
            return human_fallback_reply(msg)

        return reply

    except Exception as e:
        return f"صار خطأ بالربط: {e}"


def send_message(text):
    if not text:
        return

    st.session_state[CHAT_KEY].append(("user", text))
    bot_reply = get_bot_reply(text)
    st.session_state[CHAT_KEY].append(("bot", bot_reply))


st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    background:#eef2f7;
    direction:rtl;
}
header, footer, #MainMenu {
    visibility:hidden;
}
.block-container {
    max-width:430px;
    height:730px;
    margin:auto;
    padding:14px 16px 8px;
    border-radius:42px;
    background:linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
    box-shadow:0 12px 30px rgba(0,0,0,.15);
    overflow:hidden;
}
.topbar {
    height:58px;
    background:white;
    border-radius:18px;
    display:flex;
    align-items:center;
    gap:10px;
    padding:0 14px;
    box-shadow:0 3px 10px rgba(0,0,0,.12);
    margin-bottom:10px;
}
.avatar {
    width:42px;
    height:42px;
    border-radius:50%;
    object-fit:cover;
}
.dot {
    width:8px;
    height:8px;
    background:#36c06a;
    border-radius:50%;
}
.status {
    font-size:15px;
    font-weight:700;
    color:#222;
}
.region-label {
    margin-right:auto;
    font-size:11px;
    color:#436577;
    font-weight:700;
}
.quick-title {
    font-size:13px;
    font-weight:800;
    color:#102646;
    margin:4px 0 6px;
}
div[data-testid="stButton"] button {
    border-radius:18px;
    border:none;
    background:white;
    color:#102646;
    font-weight:800;
    font-size:12px;
    box-shadow:0 3px 8px rgba(0,0,0,.10);
    height:36px;
}
div[data-testid="stButton"] button:hover {
    background:#eef6ff;
    color:#1c6fa4;
}
.chat-area {
    height:350px;
    overflow-y:auto;
    padding:10px 4px;
    margin-top:10px;
    margin-bottom:8px;
}
.msg {
    max-width:75%;
    padding:9px 12px;
    border-radius:16px;
    margin-bottom:8px;
    font-size:13px;
    line-height:1.5;
    white-space:pre-wrap;
    text-align:right;
}
.bot {
    background:white;
    color:#222;
    margin-left:auto;
}
.user {
    background:#1c6fa4;
    color:white;
    margin-right:auto;
}
div[data-testid="stChatInput"] {
    position:relative !important;
    bottom:auto !important;
    background:transparent !important;
    padding:0 !important;
}
div[data-testid="stChatInput"] textarea {
    direction:rtl;
    border-radius:22px;
    border:none;
    background:white;
    font-size:13px;
}
</style>
""", unsafe_allow_html=True)


region = st.session_state.get("region", "عمان")

st.markdown(f"""
<div class="topbar">
    <img class="avatar" src="data:image/png;base64,{robot}">
    <div class="dot"></div>
    <div class="status">جاهز للمساعدة</div>
    <div class="region-label">📍 {html_lib.escape(region)}</div>
</div>
""", unsafe_allow_html=True)


st.markdown('<div class="quick-title">الخدمات السريعة</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
c4, c5, c6 = st.columns(3)

with c1:
    if st.button("فحص الشبكة"):
        send_message("فحص الشبكة")
        st.rerun()

with c2:
    if st.button("استهلاك الإنترنت"):
        send_message("استهلاك الإنترنت")
        st.rerun()

with c3:
    if st.button("تجديد الباقة"):
        send_message("تجديد الباقة")
        st.rerun()

with c4:
    if st.button("المكالمات الدولية"):
        send_message("المكالمات الدولية")
        st.rerun()

with c5:
    if st.button("العروض"):
        send_message("العروض")
        st.rerun()

with c6:
    if st.button("الدعم"):
        send_message("الدعم")
        st.rerun()


chat_html = '<div class="chat-area">'

for role, message in st.session_state[CHAT_KEY]:
    cls = "user" if role == "user" else "bot"
    safe_msg = html_lib.escape(str(message))
    chat_html += f'<div class="msg {cls}">{safe_msg}</div>'

chat_html += '</div>'

st.markdown(chat_html, unsafe_allow_html=True)

user_input = st.chat_input("اكتب سؤالك...")

if user_input:
    send_message(user_input)
    st.rerun()
