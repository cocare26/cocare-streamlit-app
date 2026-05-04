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
    "current": "Current Password" if not is_ar else "كلمة المرور الحالية",
"new": "New Password" if not is_ar else "كلمة المرور الجديدة",
"rewrite": "Re-write New Password" if not is_ar else "إعادة كتابة كلمة المرور",
"report_pass": "Report Password" if not is_ar else "الإبلاغ عن كلمة المرور",
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
}}

input {{
    border-radius:30px !important;
    padding:12px !important;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
}}

textarea {{
    border-radius:20px !important;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
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

    # -------- PASSWORD -------- (بدون card)
    if st.session_state.page == "pass":

        import streamlit.components.v1 as components

        components.html("""
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
            <style>
                body {
                    font-family: 'Segoe UI', sans-serif;
                    background: transparent;
                    margin: 0;
                }

                .main-wrapper {
                    width: 100%;
                    max-width: 290px;
                    display: flex;
                    flex-direction: column;
                    height: 420px;
                }

                .input-capsule {
    background: white;
    border-radius: 100px;
    padding: 10px 18px;
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    transition: transform 0.2s ease;
}

.input-capsule:hover {
    transform: translateY(-4px);
}

                .input-capsule i.field-icon {
                    color: #0f2446;
                    margin-right: 12px;
                    font-size: 16px;
                }

                .input-capsule input {
                    border: none;
                    outline: none;
                    flex-grow: 1;
                    font-size: 14px;
                    color: #0f2446;
                    background: transparent;
                }

                .input-capsule input::placeholder {
                    color: #808080;
                }

                .input-capsule i.toggle-eye {
                    color: #ccc;
                    cursor: pointer;
                    margin-left: 10px;
                }

                .report-text {
                    text-align: center;
                    color: white;
                    font-size: 13px;
                    margin-top: 5px;
                    margin-bottom: 15px;
                    cursor: pointer;
                    font-weight: bold;
                }

                .save-btn-container {
                    margin-top: auto;
                    display: flex;
                    justify-content: center;
                    padding-bottom: 10px;
                }

                .save-box {
                    background: white;
                    border-radius: 100px;
                    width: 100%;
                    padding: 12px;
                    text-align: center;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
                    cursor: pointer;
                    transition: 0.3s;
                    border: none;
                }

                .save-box span {
                    color: #0f2446;
                    font-weight: bold;
                    font-size: 16px;
                }

                .save-box:hover {
                    transform: translateY(-2px);
                }
            </style>
        </head>

        <body>
            <div class="main-wrapper">

                <div class="input-capsule">
    <i class="fas fa-lock field-icon"></i>
    <input id="pass1" type="password" placeholder="Current Password">
    <i class="fas fa-eye-slash toggle-eye" onclick="togglePassword('pass1', this)"></i>
</div>

<div class="input-capsule">
    <i class="fas fa-lock field-icon"></i>
    <input id="pass2" type="password" placeholder="New Password">
  <i class="fas fa-eye-slash toggle-eye" onclick="togglePassword('pass1', this)"></i>
</div>

<div class="input-capsule">
    <i class="fas fa-lock field-icon"></i>
    <input id="pass3" type="password" placeholder="Re-write New Password">
    <i class="fas fa-eye-slash toggle-eye" onclick="togglePassword('pass1', this)"></i>
</div>

                <div class="report-text">
                    Report Password
                </div>

                <div class="save-btn-container">
                    <button class="save-box" onclick="alert('Password Saved!')">
                        <span>Save</span>
                    </button>
                </div>

            </div>
        </body>
        </html>
        """, height=420)

    # -------- LANGUAGE -------- (بدون card)
    elif st.session_state.page == "lang":

        if st.button("🌐 English"):
            set_lang("en")

        if st.button("🌐 العربية"):
            set_lang("ar")

    # -------- RATE -------- (بدون card)
    elif st.session_state.page == "rate":

        st.button("▶ Google Play Store")
        st.button("🍎 Apple App Store")
        st.button("📱 Huawei AppGallery")

    # -------- LOGOUT --------
    elif st.session_state.page == "logout":

        st.warning("Are you sure?" if not is_ar else "هل أنت متأكد؟")
        st.button(T["logout"])

    # -------- REPORT -------- (مع card)
    elif st.session_state.page == "report":

        import streamlit.components.v1 as components

        components.html("""
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
            <style>
                body {
                    font-family: 'Segoe UI', sans-serif;
                    background: transparent;
                    margin: 0;
                }

                .main-wrapper {
                    width: 100%;
                    max-width: 290px;
                    height: 430px;
                    display: flex;
                    flex-direction: column;
                }

                .report-textarea {
                    width: 100%;
                    height: 220px;
                    border-radius: 25px;
                    border: none;
                    outline: none;
                    padding: 18px;
                    background: white;
                    font-size: 16px;
                    color: #0f2446;
                    resize: none;
                    box-sizing: border-box;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
                    font-family: inherit;
                }

                .report-textarea::placeholder {
                    color: #808080;
                }

                .send-btn {
                    background: white;
                    border-radius: 100px;
                    width: 100%;
                    padding: 14px 22px;
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    border: none;
                    margin-top: 30px;
                    cursor: pointer;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
                    box-sizing: border-box;
                }

                .send-btn:hover {
                    transform: translateY(-2px);
                    background: #f7fbff;
                }

                .send-btn span {
                    color: #0f2446;
                    font-weight: 700;
                    font-size: 14px;
                    order: 2;
                }

                .main-icon {
                    color: #808080;
                    font-size: 18px;
                    order: 1;
                }
            </style>
        </head>

        <body>
            <div class="main-wrapper">
                <textarea class="report-textarea" placeholder="I need help"></textarea>

                <button class="send-btn" onclick="alert('Sent!')">
                    <i class="fas fa-paper-plane main-icon"></i>
                    <span>Send Report</span>
                </button>
            </div>
        </body>
        </html>
        """, height=360)

    # -------- CONTACT -------- (مع card)
    elif st.session_state.page == "contact":

        st.markdown("""
        <style>
        .contact-box {
            background: white;
            padding: 14px 18px;
            border-radius: 50px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.08);
            margin-bottom: 12px;
            color: #0f2446;
            font-weight: 600;
            cursor: pointer;
            transition: 0.2s;
        }

        .contact-box:hover {
            transform: translateY(-2px);
            background: #f7fbff;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("<div class='contact-box'>📧 CoCare26@gmail.com</div>", unsafe_allow_html=True)
        st.markdown("<div class='contact-box'>📞 +962 79 123 4567</div>", unsafe_allow_html=True)
