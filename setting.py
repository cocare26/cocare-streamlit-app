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

def toggle_lang(lang):
    st.session_state.lang = lang
    st.rerun()

# ---------------- LANGUAGE ----------------
is_ar = st.session_state.lang == "ar"

txt = {
    "settings": "الإعدادات" if is_ar else "Settings",
    "pass": "تغيير كلمة المرور" if is_ar else "Change Password",
    "lang": "تغيير اللغة" if is_ar else "Change Language",
    "rate": "تقييم التطبيق" if is_ar else "Rate App",
    "logout": "تسجيل الخروج" if is_ar else "Log Out",
    "report": "الإبلاغ عن مشكلة" if is_ar else "Report a Problem",
    "contact": "تواصل معنا" if is_ar else "Contact Us",
    "save": "حفظ" if is_ar else "Save",
    "back": "←",
}

# ---------------- STYLE ----------------
st.markdown(f"""
<style>
body {{
    direction: {"rtl" if is_ar else "ltr"};
}}

.block-container {{
    max-width:360px;
    margin:auto;
    padding:20px;
    background:linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
    border-radius:35px;
    box-shadow:0 10px 30px rgba(0,0,0,0.15);
}}

/* header */
.header {{
    text-align:center;
    font-size:20px;
    font-weight:700;
    margin-bottom:25px;
}}

/* button card */
.stButton > button {{
    width:100%;
    border:none;
    background:white;
    border-radius:50px;
    padding:14px 16px;
    margin-bottom:12px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    font-weight:500;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
}}

.stButton > button:hover {{
    transform:translateY(-2px);
}}

/* inner cards */
.card {{
    background:white;
    padding:15px;
    border-radius:20px;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
    margin-bottom:15px;
}}

input, textarea {{
    border-radius:12px !important;
}}
</style>
""", unsafe_allow_html=True)

# ================= MAIN =================
if st.session_state.page == "main":

    st.markdown(f"<div class='header'>{txt['settings']}</div>", unsafe_allow_html=True)

    if st.button(f"🔒 {txt['pass']}"):
        go("pass")

    if st.button(f"🌐 {txt['lang']}"):
        go("lang")

    if st.button(f"⭐ {txt['rate']}"):
        go("rate")

    if st.button(f"🚪 {txt['logout']}"):
        go("logout")

    col1, col2 = st.columns(2)

    with col1:
        if st.button(f"⚠️ {txt['report']}"):
            go("report")

    with col2:
        if st.button(f"✉️ {txt['contact']}"):
            go("contact")

# ================= SUB =================
else:

    col1, col2 = st.columns([1,4])

    with col1:
        if st.button(txt["back"]):
            go("main")

    with col2:
        st.markdown(f"<div class='header'>{txt[st.session_state.page]}</div>", unsafe_allow_html=True)

    # -------- PASSWORD --------
    if st.session_state.page == "pass":

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.text_input("••••••••", placeholder="Current Password")
        st.text_input("••••••••", placeholder="New Password")
        st.text_input("••••••••", placeholder="Rewrite Password")
        st.markdown("</div>", unsafe_allow_html=True)

        st.button(txt["save"])

    # -------- LANGUAGE --------
    elif st.session_state.page == "lang":

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        if st.button("🇬🇧 English"):
            toggle_lang("en")

        if st.button("🇸🇦 العربية"):
            toggle_lang("ar")

        st.markdown("</div>", unsafe_allow_html=True)

    # -------- RATE --------
    elif st.session_state.page == "rate":

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.button("▶ Google Play")
        st.button("🍎 App Store")
        st.button("📱 Huawei Store")

        st.markdown("</div>", unsafe_allow_html=True)

    # -------- LOGOUT --------
    elif st.session_state.page == "logout":

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.warning("Are you sure?" if not is_ar else "هل أنت متأكد؟")
        st.markdown("</div>", unsafe_allow_html=True)

        st.button(txt["logout"])

    # -------- REPORT --------
    elif st.session_state.page == "report":

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.text_area("...", placeholder="I need help")
        st.markdown("</div>", unsafe_allow_html=True)

        st.button("Send Report")

    # -------- CONTACT --------
    elif st.session_state.page == "contact":

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.write("📧 CoCare26@gmail.com")
        st.write("📞 +962 79 123 4567")

        st.markdown("</div>", unsafe_allow_html=True)
