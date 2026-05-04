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

/* App background */
[data-testid="stAppViewContainer"] {{
    background: linear-gradient(180deg,#dcefff,#cfe9ff,#eaf6ff);
}}

/* Main container */
.block-container {{
    max-width:370px;
    margin:auto;
    padding:30px 20px;
    background: rgba(255,255,255,0.25);
    backdrop-filter: blur(10px);
    border-radius:40px;
}}

/* Direction */
body {{
    direction: {"rtl" if is_ar else "ltr"};
}}

/* Header */
.header {{
    text-align:center;
    font-size:20px;
    font-weight:700;
    margin-bottom:25px;
    color:#0f2446;
}}

/* Button Card */
.stButton > button {{
    width:100%;
    border:none;
    background:#ffffff;
    border-radius:50px;
    padding:16px;
    margin-bottom:12px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    font-size:14px;
    color:#0f2446;
    box-shadow:0 6px 15px rgba(0,0,0,0.08);
}}

.stButton > button:hover {{
    transform:translateY(-2px);
    box-shadow:0 8px 18px rgba(0,0,0,0.12);
}}

/* Inputs like iOS */
input {{
    background:#fff !important;
    border:none !important;
    border-radius:30px !important;
    padding:12px !important;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
}}

textarea {{
    border-radius:20px !important;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
}}

/* Save Button */
.primary button {{
    background:#ffffff !important;
    border-radius:40px !important;
    box-shadow:0 6px 12px rgba(0,0,0,0.1);
}}

/* Section Card */
.card {{
    background:white;
    padding:15px;
    border-radius:25px;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
    margin-bottom:15px;
}}

</style>
""", unsafe_allow_html=True)

# ================= MAIN =================
if st.session_state.page == "main":

    st.markdown(f"<div class='header'>{T['settings']}</div>", unsafe_allow_html=True)

    if st.button(f"🔒 {T['pass']}"):
        go("pass")

    if st.button(f"🌐 {T['lang']}"):
        go("lang")

    if st.button(f"⭐ {T['rate']}"):
        go("rate")

    if st.button(f"🚪 {T['logout']}"):
        go("logout")

    col1, col2 = st.columns(2)

    with col1:
        if st.button(f"⚠️ {T['report']}"):
            go("report")

    with col2:
        if st.button(f"✉️ {T['contact']}"):
            go("contact")

# ================= SUB =================
else:

    col1, col2 = st.columns([1,4])

    with col1:
        if st.button("←"):
            go("main")

    with col2:
        st.markdown(f"<div class='header'>{T[st.session_state.page]}</div>", unsafe_allow_html=True)

    # -------- PASSWORD --------
    if st.session_state.page == "pass":

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.text_input("", placeholder="Current Password")
        st.text_input("", placeholder="New Password")
        st.text_input("", placeholder="Re-write Password")
        st.markdown("</div>", unsafe_allow_html=True)

        st.button(T["save"])

    # -------- LANGUAGE --------
    elif st.session_state.page == "lang":

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        if st.button("🌐 English"):
            set_lang("en")

        if st.button("🌐 العربية"):
            set_lang("ar")

        st.markdown("</div>", unsafe_allow_html=True)

    # -------- RATE --------
    elif st.session_state.page == "rate":

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.button("▶ Google Play Store")
        st.button("🍎 Apple App Store")
        st.button("📱 Huawei AppGallery")

        st.markdown("</div>", unsafe_allow_html=True)

    # -------- LOGOUT --------
    elif st.session_state.page == "logout":

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.warning("Are you sure?" if not is_ar else "هل أنت متأكد؟")
        st.markdown("</div>", unsafe_allow_html=True)

        st.button(T["logout"])

    # -------- REPORT --------
    elif st.session_state.page == "report":

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.text_area("", placeholder="I need help")
        st.markdown("</div>", unsafe_allow_html=True)

        st.button("Send Report")

    # -------- CONTACT --------
    elif st.session_state.page == "contact":

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.write("📧 CoCare26@gmail.com")
        st.write("📞 +962 79 123 4567")
        st.markdown("</div>", unsafe_allow_html=True)
