import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "main"

if "lang" not in st.session_state:
    st.session_state.lang = "en"

def go(page):
    st.session_state.page = page
    st.rerun()

def set_lang(lang):
    st.session_state.lang = lang
    st.rerun()

is_ar = st.session_state.lang == "ar"

# ---------------- TEXT ----------------
T = {
    "settings": "الإعدادات" if is_ar else "Settings",
    "pass": "Change Password" if not is_ar else "تغيير كلمة المرور",
    "lang": "Change Language" if not is_ar else "تغيير اللغة",
    "rate": "Rate App" if not is_ar else "تقييم التطبيق",
    "logout": "Log Out" if not is_ar else "تسجيل الخروج",
    "report": "Report a Problem" if not is_ar else "الإبلاغ عن مشكلة",
    "contact": "Contact Us" if not is_ar else "تواصل معنا",
    "save": "Save" if not is_ar else "حفظ",
}

# ---------------- STYLE ----------------
st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background: linear-gradient(180deg,#dcefff,#cfe9ff,#eaf6ff);
}}

.block-container {{
    max-width:370px;
    margin:auto;
    padding:30px 20px;
    background: rgba(255,255,255,0.25);
    backdrop-filter: blur(10px);
    border-radius:40px;
}}

body {{
    direction: {"rtl" if is_ar else "ltr"};
}}

.header {{
    text-align:center;
    font-size:20px;
    font-weight:700;
    margin-bottom:25px;
    color:#0f2446;
}}

/* ===== BUTTON STYLE ===== */
.stButton > button {{
    width:100%;
    border:none;
    background:#ffffff;
    border-radius:50px;
    padding:16px 50px 16px 20px;
    margin-bottom:12px;
    font-size:14px;
    color:#0f2446;
    box-shadow:0 6px 15px rgba(0,0,0,0.08);
    text-align:left;
    position:relative;
}}

.stButton > button:hover {{
    transform:translateY(-2px);
}}

/* السهم */
.stButton > button::after {{
    content:"›";
    position:absolute;
    right:15px;
    font-size:18px;
    color:#0f2446;
}}

/* الأيقونة */
.stButton > button::before {{
    content: attr(data-icon);
    position:absolute;
    right:40px;
    font-size:16px;
}}

/* INPUT */
input {{
    border-radius:30px !important;
    padding:12px !important;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
}}

textarea {{
    border-radius:20px !important;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
}}

/* CARD */
.card {{
    background:white;
    padding:15px;
    border-radius:25px;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
    margin-bottom:15px;
}}
</style>
""", unsafe_allow_html=True)

# -------- ICON SCRIPT --------
st.markdown("""
<script>
const icons = ["🔒","🌐","⭐","🚪","⚠️","✉️"];

setTimeout(() => {
    const buttons = window.parent.document.querySelectorAll('button');
    buttons.forEach((btn, i) => {
        if(i < icons.length){
            btn.setAttribute("data-icon", icons[i]);
        }
    });
}, 300);
</script>
""", unsafe_allow_html=True)

# ================= MAIN =================
if st.session_state.page == "main":

    st.markdown(f"<div class='header'>{T['settings']}</div>", unsafe_allow_html=True)

    if st.button(T['pass']):
        go("pass")

    if st.button(T['lang']):
        go("lang")

    if st.button(T['rate']):
        go("rate")

    if st.button(T['logout']):
        go("logout")

    col1, col2 = st.columns(2)

    with col1:
        if st.button(T['report']):
            go("report")

    with col2:
        if st.button(T['contact']):
            go("contact")

# ================= SUB =================
else:

    col1, col2 = st.columns([1,4])

    with col1:
        if st.button("←"):
            go("main")

    with col2:
        st.markdown(f"<div class='header'>{T[st.session_state.page]}</div>", unsafe_allow_html=True)

    if st.session_state.page == "pass":

        st.text_input("", placeholder="Current Password")
        st.text_input("", placeholder="New Password")
        st.text_input("", placeholder="Re-write Password")

        st.button(T["save"])

    elif st.session_state.page == "lang":

        if st.button("English"):
            set_lang("en")

        if st.button("العربية"):
            set_lang("ar")

    elif st.session_state.page == "rate":

        st.button("Google Play Store")
        st.button("Apple App Store")
        st.button("Huawei AppGallery")

    elif st.session_state.page == "logout":

        st.warning("Are you sure?" if not is_ar else "هل أنت متأكد؟")
        st.button(T["logout"])

    elif st.session_state.page == "report":

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.text_area("", placeholder="I need help")
        st.markdown("</div>", unsafe_allow_html=True)

        st.button("Send Report")

    elif st.session_state.page == "contact":

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.write("📧 CoCare26@gmail.com")
        st.write("📞 +962 79 123 4567")
        st.markdown("</div>", unsafe_allow_html=True)
