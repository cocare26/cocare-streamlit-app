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

arrow = "→" if not is_ar else "←"

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

.stButton > button {{
    width:100%;
    border:none;
    background:#ffffff;
    border-radius:50px;
    padding:16px;
    margin-bottom:12px;
    font-size:14px;
    color:#0f2446;
    box-shadow:0 6px 15px rgba(0,0,0,0.08);
    display:flex;
    align-items:center;
    justify-content:space-between;
}}

.stButton > button:hover {{
    transform:translateY(-2px);
}}

input {{
    border-radius:30px !important;
    padding:12px !important;
}}

textarea {{
    border-radius:20px !important;
}}

.card {{
    background:white;
    padding:15px;
    border-radius:25px;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
    margin-bottom:15px;
}}


.st-b7 {{
    background-color: rgb(255 255 255);
        color: black;
}}

.st.text_input{{
 color: black;
}}

.st-bc {{
   color: black;
}}

.block-container {{
    height: 600px;
}}

.st-emotion-cache-zh2fnc  {{
   width:100%;
    height: auto;
    max-width: 100%;
    min-width: 1rem;
    position: relative;
    overflow: visible;
}}



</style>
""", unsafe_allow_html=True)

# ---------------- BUTTON ----------------
def menu_button(label, icon, page_key):
    # الأيقونة يسار، النص + السهم يمين
    btn_label = f"{icon}   {label}   {arrow}"
    if st.button(btn_label, key=f"btn_{page_key}"):
        go(page_key)

# ================= MAIN =================
if st.session_state.page == "main":

    st.markdown(f"<div class='header'>{T['settings']}</div>", unsafe_allow_html=True)

    menu_button(T["pass"], "🔒", "pass")
    menu_button(T["lang"], "🌐", "lang")
    menu_button(T["rate"], "⭐", "rate")
    menu_button(T["logout"], "🚪", "logout")

    col1, col2 = st.columns(2)

    with col1:
        menu_button(T["report"], "⚠️", "report")

    with col2:
        menu_button(T["contact"], "✉️", "contact")

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
        st.text_input("", placeholder="Current Password")
        st.text_input("", placeholder="New Password")
        st.text_input("", placeholder="Re-write Password")
        st.button(T["save"])

    # -------- LANGUAGE --------
    elif st.session_state.page == "lang":
        if st.button("🌐 English"):
            set_lang("en")
        if st.button("🌐 العربية"):
            set_lang("ar")

    # -------- RATE --------
    elif st.session_state.page == "rate":
        st.button("▶ Google Play Store")
        st.button("🍎 Apple App Store")
        st.button("📱 Huawei AppGallery")

    # -------- LOGOUT --------
    elif st.session_state.page == "logout":
        st.warning("Are you sure?" if not is_ar else "هل أنت متأكد؟")
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
