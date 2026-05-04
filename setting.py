import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Smart App Settings", layout="centered")

# =============================
# STATE
# =============================
if 'settings_sub_page' not in st.session_state:
    st.session_state.settings_sub_page = 'main_menu'

if 'lang' not in st.session_state:
    st.session_state.lang = 'en'

def nav_settings(target):
    st.session_state.settings_sub_page = target
    st.rerun()

def set_lang(l):
    st.session_state.lang = l
    st.rerun()

# =============================
# TRANSLATION
# =============================
TEXT = {
    "en": {
        "settings": "Settings",
        "change_password": "Change Password",
        "change_language": "Change Language",
        "rate": "Rate App",
        "logout": "Log Out",
        "report": "Report Problem",
        "contact": "Contact Us",
        "language": "Language",
        "back": "Back"
    },
    "ar": {
        "settings": "الإعدادات",
        "change_password": "تغيير كلمة المرور",
        "change_language": "تغيير اللغة",
        "rate": "تقييم التطبيق",
        "logout": "تسجيل الخروج",
        "report": "الإبلاغ عن مشكلة",
        "contact": "اتصل بنا",
        "language": "اللغة",
        "back": "رجوع"
    }
}

def t(k):
    return TEXT[st.session_state.lang][k]

# =============================
# STYLE
# =============================
st.markdown("""
<style>
[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}
.block-container{
    max-width:350px !important;
    margin:auto !important;
    padding:30px !important;
    background:linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
    border-radius:42px;
    box-shadow:0 15px 35px rgba(0,0,0,0.15);
}

/* hide hidden buttons */
button[kind="secondary"]{
    display:none !important;
}
</style>
""", unsafe_allow_html=True)

# =============================
# HIDDEN NAV BUTTONS
# =============================
if st.button("pass", key="pass_btn"):
    nav_settings('change_password_page')

if st.button("lang", key="lang_btn"):
    nav_settings('language_page')

if st.button("rate", key="rate_btn"):
    nav_settings('rate_page')

if st.button("logout", key="logout_btn"):
    nav_settings('logout_page')

if st.button("report", key="report_btn"):
    nav_settings('report_page')

if st.button("contact", key="contact_btn"):
    nav_settings('contact_page')

# =============================
# MAIN MENU (HTML DESIGN)
# =============================
if st.session_state.settings_sub_page == 'main_menu':

    components.html(f"""
    <!DOCTYPE html>
    <html dir="{ 'rtl' if st.session_state.lang == 'ar' else 'ltr' }">
    <head>
    <style>
    body {{
        font-family:'Segoe UI', sans-serif;
        margin:0;
        display:flex;
        justify-content:center;
        background:transparent;
    }}

    .main-wrapper {{
        width:100%;
        max-width:290px;
    }}

    .title {{
        text-align:center;
        font-weight:900;
        font-size:20px;
        color:#0f2446;
        margin-bottom:25px;
    }}

    .setting-item {{
        background:white;
        border-radius:100px;
        padding:14px 18px;
        margin-bottom:15px;
        display:flex;
        align-items:center;
        justify-content:space-between;
        box-shadow:0 4px 12px rgba(0,0,0,0.08);
        cursor:pointer;
    }}

    .icon {{
        font-size:16px;
    }}

    .text {{
        flex:1;
        text-align:{ 'right' if st.session_state.lang == 'ar' else 'left' };
        margin:0 10px;
        font-weight:600;
        color:#0f2446;
    }}

    .arrow {{
        font-size:18px;
        transform:{ 'rotate(180deg)' if st.session_state.lang == 'ar' else 'none' };
    }}

    .bottom-row {{
        display:flex;
        gap:10px;
    }}
    </style>
    </head>

    <body>

    <div class="main-wrapper">

        <div class="title">{t("settings")}</div>

        <div class="setting-item" onclick="go('pass')">
            <div class="icon">🔒</div>
            <div class="text">{t("change_password")}</div>
            <div class="arrow">›</div>
        </div>

        <div class="setting-item" onclick="go('lang')">
            <div class="icon">🌐</div>
            <div class="text">{t("change_language")}</div>
            <div class="arrow">›</div>
        </div>

        <div class="setting-item" onclick="go('rate')">
            <div class="icon">⭐</div>
            <div class="text">{t("rate")}</div>
            <div class="arrow">›</div>
        </div>

        <div class="setting-item" onclick="go('logout')">
            <div class="icon">🚪</div>
            <div class="text">{t("logout")}</div>
            <div class="arrow">›</div>
        </div>

        <div class="bottom-row">
            <div class="setting-item" style="flex:1;" onclick="go('report')">
                <div class="icon">⚠️</div>
                <div class="text">{t("report")}</div>
            </div>

            <div class="setting-item" style="flex:1;" onclick="go('contact')">
                <div class="icon">✉️</div>
                <div class="text">{t("contact")}</div>
            </div>
        </div>

    </div>

    <script>
    function go(p){
        const doc = window.parent.document;

        if(p === "pass") doc.querySelector('button[key="pass_btn"]').click();
        if(p === "lang") doc.querySelector('button[key="lang_btn"]').click();
        if(p === "rate") doc.querySelector('button[key="rate_btn"]').click();
        if(p === "logout") doc.querySelector('button[key="logout_btn"]').click();
        if(p === "report") doc.querySelector('button[key="report_btn"]').click();
        if(p === "contact") doc.querySelector('button[key="contact_btn"]').click();
    }
    </script>

    </body>
    </html>
    """, height=520)

# =============================
# LANGUAGE PAGE
# =============================
elif st.session_state.settings_sub_page == 'language_page':

    st.markdown(f"### {t('language')}")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("English"):
            set_lang("en")

    with col2:
        if st.button("العربية"):
            set_lang("ar")

    if st.button("⬅ " + t("back")):
        nav_settings('main_menu')

# =============================
# CHANGE PASSWORD
# =============================
elif st.session_state.settings_sub_page == 'change_password_page':

    st.markdown(f"### {t('change_password')}")

    st.text_input("Current Password", type="password")
    st.text_input("New Password", type="password")
    st.text_input("Confirm Password", type="password")

    if st.button("Save"):
        st.success("Saved!")

    if st.button("⬅ " + t("back")):
        nav_settings('main_menu')

# =============================
# REPORT
# =============================
elif st.session_state.settings_sub_page == 'report_page':

    st.markdown(f"### {t('report')}")

    st.text_area("Write your problem...")

    if st.button("Send"):
        st.success("Sent!")

    if st.button("⬅ " + t("back")):
        nav_settings('main_menu')

# =============================
# CONTACT
# =============================
elif st.session_state.settings_sub_page == 'contact_page':

    st.markdown(f"### {t('contact')}")

    st.write("📧 CoCare26@gmail.com")
    st.write("📞 +962 79 123 4567")

    if st.button("⬅ " + t("back")):
        nav_settings('main_menu')

# =============================
# RATE
# =============================
elif st.session_state.settings_sub_page == 'rate_page':

    st.markdown(f"### {t('rate')}")

    if st.button("Google Play"):
        st.write("Open Play Store")

    if st.button("App Store"):
        st.write("Open App Store")

    if st.button("⬅ " + t("back")):
        nav_settings('main_menu')

# =============================
# LOGOUT
# =============================
elif st.session_state.settings_sub_page == 'logout_page':

    st.markdown(f"### {t('logout')}")
    st.warning("Are you sure?")

    if st.button("Yes"):
        st.success("Logged out")

    if st.button("⬅ " + t("back")):
        nav_settings('main_menu')
