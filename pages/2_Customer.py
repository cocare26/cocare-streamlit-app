import streamlit as st
import base64
import os

# 1. إعداد حالة الصفحة للتنقل
if 'page' not in st.session_state:
    st.session_state.page = "home"

def go_home():
    st.session_state.page = "home"
    st.rerun()

# استرجاع اسم المستخدم المخزن ديناميكياً
user_name = st.session_state.get('user_name', 'User Name')

# 2. إعداد الصفحة
st.set_page_config(page_title="CoCare Dashboard", page_icon="📱", layout="centered")

def get_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

# تحميل الصور
robot_full = get_base64("robot_full.png.jpeg")
robot_head = get_base64("robot_head.png")
icon_internet = get_base64("internet.png")
icon_renewals = get_base64("renewals.png")
icon_calls = get_base64("calls.png")
icon_notifications = get_base64("notifications.png")
icon_sitting = get_base64("sitting.png")
icon_spin = get_base64("spin.png")
icon_home = get_base64("home.png")
icon_game = get_base64("game.png")

# 3. التصميم (CSS)
st.markdown(f"""
<style>
* {{
    margin:0;
    padding:0;
    box-sizing:border-box;
}}

html, body, [data-testid="stAppViewContainer"] {{
    background:#f0f7ff;
    font-family:'Segoe UI', sans-serif;
}}

#MainMenu, header, footer {{
    visibility:hidden;
}}

.block-container {{
    max-width:430px;
    margin:auto;
    padding:12px 16px;
    background: linear-gradient(180deg, #FFFFFF 0%, #E3F2FD 30%, #BBDEFB 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
}}

.card {{
    background: white;
    border-radius: 20px;
    padding: 10px 14px;
    margin-bottom: 8px;
    box-shadow: 0 4px 15px rgba(0,0,0,.05);
}}

.title {{
    font-size:15px;
    font-weight:900;
    color:#102646;
    margin: 4px 0 4px 4px;
}}

.hover-effect {{
    transition: 0.3s ease-in-out;
    cursor: pointer;
}}

.hover-effect:hover {{
    transform: scale(1.15);
    filter: drop-shadow(0 5px 15px rgba(0,0,0,0.1));
}}

.nav-img-footer {{
    width: 35px;
    height: 35px;
    object-fit: contain;
    transition: 0.3s;
}}

.nav-img-footer:hover {{
    transform: scale(1.2);
}}

.bot-bg {{
    width:50px;
    height:50px;
    background:white;
    border-radius:12px;
    margin: 0 auto 4px;
    display:flex;
    align-items:center;
    justify-content:center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    transition: 0.3s;
}}

.bot-bg:hover {{
    transform: rotate(10deg) scale(1.15);
}}

div.stButton > button {{
    background: transparent;
    border: none;
    color: transparent;
    width: 100%;
    height: 80px;
    position: absolute;
    z-index: 10;
}}

div.stButton > button:hover {{
    color: transparent;
    background: transparent;
    border: none;
}}
</style>
""", unsafe_allow_html=True)

# =====================================
# الصفحة الرئيسية
# =====================================

if st.session_state.page == "home":

    # الملف الشخصي
    st.markdown(f'''
    <div class="card">
        <div style="display:flex; align-items:center;">
            <img src="data:image/png;base64,{robot_full}"
                 style="width:95px; height:95px; object-fit:contain;">

            <div style="margin-left:12px;">
                <div style="font-size:20px; font-weight:900; color:#102646;">
                    Welcome: {user_name}
                </div>

                <div style="font-size:12px; color:#555;">
                    +962 79 123 4567
                </div>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    # تقييم النجوم
    st.markdown(
        '<div class="card" style="text-align:center; padding:10px;">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="font-size:14px; margin-bottom:5px; color:#102646;">Rate your experience</div>',
        unsafe_allow_html=True
    )

    st.feedback("stars")

    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================
    # أيقونات الخدمات
    # =====================================

    st.markdown('<div class="title">Services</div>', unsafe_allow_html=True)

    cols = st.columns(4)

    # Internet Packages
    with cols[0]:

        st.markdown(
            f'''
            <div class="hover-effect" style="text-align:center;">
                <img src="data:image/png;base64,{icon_internet}" style="width:75px;">
            </div>
            ''',
            unsafe_allow_html=True
        )

        if st.button(" ", key="int"):
            st.switch_page("InternetPackages.py")

    # Renewals
    with cols[1]:

        st.markdown(
            f'''
            <div class="hover-effect" style="text-align:center;">
                <img src="data:image/png;base64,{icon_renewals}" style="width:75px;">
            </div>
            ''',
            unsafe_allow_html=True
        )

        if st.button(" ", key="ren"):
            st.switch_page("RenewalsTariff.py")

    # International Calls
    with cols[2]:

        st.markdown(
            f'''
            <div class="hover-effect" style="text-align:center;">
                <img src="data:image/png;base64,{icon_calls}" style="width:75px;">
            </div>
            ''',
            unsafe_allow_html=True
        )

        if st.button(" ", key="call"):
            st.switch_page("InternationalCalls.py")

    # Notifications
    with cols[3]:

        st.markdown(
            f'''
            <div class="hover-effect" style="text-align:center;">
                <img src="data:image/png;base64,{icon_notifications}" style="width:75px;">
            </div>
            ''',
            unsafe_allow_html=True
        )

        if st.button(" ", key="not"):
            st.switch_page("NetworkNotifications.py")

    # =====================================
    # الشريط السفلي
    # =====================================

    st.write("")

    nav_cols = st.columns(5)

    # Settings
    with nav_cols[0]:

        st.markdown(
            f'''
            <div class="nav-item">
                <img src="data:image/png;base64,{icon_sitting}"
                     class="nav-img-footer">
            </div>
            ''',
            unsafe_allow_html=True
        )

        if st.button(" ", key="nav_set"):
            st.switch_page("Settings.py")

    # Spin
    with nav_cols[1]:

        st.markdown(
            f'''
            <div class="nav-item">
                <img src="data:image/png;base64,{icon_spin}"
                     class="nav-img-footer">
            </div>
            ''',
            unsafe_allow_html=True
        )

    # Chatbot
    with nav_cols[2]:

        st.markdown(
            f'''
            <div class="nav-item">
                <div class="bot-bg">
                    <img src="data:image/png;base64,{robot_head}"
                         style="width:34px;">
                </div>
            </div>
            ''',
            unsafe_allow_html=True
        )

        if st.button(" ", key="nav_bot"):
            st.switch_page("ContactUs.py")

    # Home
    with nav_cols[3]:

        st.markdown(
            f'''
            <div class="nav-item">
                <img src="data:image/png;base64,{icon_home}"
                     class="nav-img-footer">
            </div>
            ''',
            unsafe_allow_html=True
        )

        if st.button(" ", key="nav_home"):
            go_home()

    # Games
    with nav_cols[4]:

        st.markdown(
            f'''
            <div class="nav-item">
                <img src="data:image/png;base64,{icon_game}"
                     class="nav-img-footer">
            </div>
            ''',
            unsafe_allow_html=True
        )

        if st.button(" ", key="nav_game"):
            st.switch_page("_Game_E.py")
