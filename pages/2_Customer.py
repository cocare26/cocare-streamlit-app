import streamlit as st
import base64
import os

# =====================================================
# إعداد الصفحة
# =====================================================

st.set_page_config(
    page_title="CoCare Dashboard",
    page_icon="📱",
    layout="centered"
)

# =====================================================
# دالة تحويل الصور إلى Base64
# =====================================================

def get_base64(file_name):

    paths_to_check = [
        file_name,
        os.path.join("pages", file_name)
    ]

    for path in paths_to_check:

        if os.path.exists(path):

            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()

    return ""

# =====================================================
# تحميل الصور
# =====================================================

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

# =====================================================
# CSS
# =====================================================

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
    background: linear-gradient(
        180deg,
        #FFFFFF 0%,
        #E3F2FD 30%,
        #BBDEFB 100%
    );
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
}}

.card {{
    background:white;
    border-radius:20px;
    padding:14px;
    margin-bottom:12px;
    box-shadow:0 4px 15px rgba(0,0,0,.05);
}}

.title {{
    font-size:18px;
    font-weight:900;
    color:#102646;
    margin:10px 0;
}}

.hover-effect {{
    transition:0.3s ease-in-out;
    cursor:pointer;
    text-align:center;
}}

.hover-effect:hover {{
    transform:scale(1.08);
}}

.service-img {{
    width:70px;
}}

.nav-img-footer {{
    width:35px;
    height:35px;
    object-fit:contain;
}}

div.stButton > button {{
    background:transparent !important;
    border:none !important;
    color:transparent !important;
    width:100%;
    height:90px;
    margin-top:-90px;
    position:relative;
    z-index:10;
    cursor:pointer;
}}

</style>
""", unsafe_allow_html=True)

# =====================================================
# كرت الترحيب
# =====================================================

st.markdown(f"""
<div class="card">

    <div style="display:flex; align-items:center;">

        <img src="data:image/png;base64,{robot_full}"
             style="width:90px;">

        <div style="margin-left:12px;">

            <div style="
                font-size:22px;
                font-weight:900;
                color:#102646;
            ">
                Welcome: Farah
            </div>

            <div style="
                font-size:13px;
                color:gray;
                margin-top:4px;
            ">
                +962 79 123 4567
            </div>

        </div>

    </div>

</div>
""", unsafe_allow_html=True)

# =====================================================
# الخدمات
# =====================================================

st.markdown(
    '<div class="title">Services</div>',
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

# ================= Internet =================

with c1:

    st.markdown(f"""
    <div class="hover-effect">
        <img src="data:image/png;base64,{icon_internet}"
             class="service-img">
        <br>
        <small>Internet</small>
    </div>
    """, unsafe_allow_html=True)

    if st.button(" ", key="internet_btn"):
        st.switch_page("internet_page.py")

# ================= Renew =================

with c2:

    st.markdown(f"""
    <div class="hover-effect">
        <img src="data:image/png;base64,{icon_renewals}"
             class="service-img">
        <br>
        <small>Renew</small>
    </div>
    """, unsafe_allow_html=True)

    if st.button(" ", key="renew_btn"):
        st.switch_page("renew_page.py")

# ================= Calls =================

with c3:

    st.markdown(f"""
    <div class="hover-effect">
        <img src="data:image/png;base64,{icon_calls}"
             class="service-img">
        <br>
        <small>Calls</small>
    </div>
    """, unsafe_allow_html=True)

    if st.button(" ", key="calls_btn"):
        st.switch_page("calls_page.py")

# ================= Notifications =================

with c4:

    st.markdown(f"""
    <div class="hover-effect">
        <img src="data:image/png;base64,{icon_notifications}"
             class="service-img">
        <br>
        <small>Notif</small>
    </div>
    """, unsafe_allow_html=True)

    if st.button(" ", key="notif_btn"):
        st.switch_page("notif_page.py")

# =====================================================
# Footer Navigation
# =====================================================

st.write("---")

n1, n2, n3, n4, n5 = st.columns(5)

# ================= Settings =================

with n1:

    st.markdown(f"""
    <div style="text-align:center;">
        <img src="data:image/png;base64,{icon_sitting}"
             class="nav-img-footer">
    </div>
    """, unsafe_allow_html=True)

    if st.button(" ", key="nav_settings"):
        st.switch_page("pages/Settings.py")

# ================= Spin =================

with n2:

    st.markdown(f"""
    <div style="text-align:center;">
        <img src="data:image/png;base64,{icon_spin}"
             class="nav-img-footer">
    </div>
    """, unsafe_allow_html=True)

# ================= Chatbot =================

with n3:

    st.markdown(f"""
    <div style="text-align:center;">
        <img src="data:image/png;base64,{robot_head}"
             class="nav-img-footer">
    </div>
    """, unsafe_allow_html=True)

    if st.button(" ", key="nav_bot"):
        st.switch_page("pages/Chatbot.py")

# ================= Home =================

with n4:

    st.markdown(f"""
    <div style="text-align:center;">
        <img src="data:image/png;base64,{icon_home}"
             class="nav-img-footer">
    </div>
    """, unsafe_allow_html=True)

    if st.button(" ", key="nav_home"):
        st.rerun()

# ================= Game =================

with n5:

    st.markdown(f"""
    <div style="text-align:center;">
        <img src="data:image/png;base64,{icon_game}"
             class="nav-img-footer">
    </div>
    """, unsafe_allow_html=True)

    if st.button(" ", key="nav_game"):
        st.switch_page("pages/_Game_E.py")
