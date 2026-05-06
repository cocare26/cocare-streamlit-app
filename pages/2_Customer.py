import streamlit as st
import base64
import os

# استيراد الصفحات الفرعية
import internet_page, renew_page, calls_page, notif_page

# إعداد الحالة للتنقل
if 'page' not in st.session_state:
    st.session_state.page = "home"

def go_home():
    st.session_state.page = "home"
    st.rerun()

# =====================================
# واجهة الصفحة الرئيسية
# =====================================
if st.session_state.page == "home":
    st.set_page_config(page_title="Telecom Dashboard", page_icon="📱", layout="centered")

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

    st.markdown(f"""
    <style>
    * {{ margin:0; padding:0; box-sizing:border-box; }}
    html, body, [data-testid="stAppViewContainer"] {{ background:#f0f7ff; font-family:'Segoe UI', sans-serif; }}
    #MainMenu, header, footer {{ visibility:hidden; }}
    .block-container {{ max-width:430px; margin:auto; padding:12px 16px; background: linear-gradient(180deg, #FFFFFF 0%, #E3F2FD 30%, #BBDEFB 100%); border-radius:42px; box-shadow:0 14px 35px rgba(0,0,0,.15); }}
    .card {{ background: white; border-radius: 20px; padding: 10px 14px; margin-bottom: 8px; box-shadow: 0 4px 15px rgba(0,0,0,.05); }}
    .title {{ font-size:15px; font-weight:900; color:#102646; margin: 4px 0 4px 4px; }}
    .grid4 {{ display:grid; grid-template-columns:repeat(4,1fr); gap:6px; margin: 8px 0 6px; }}
    .mini-no-border {{ background: transparent; min-height: 85px; display: flex; align-items: center; justify-content: center; }}
    .mini-img-large {{ width: 85px; height: 85px; object-fit: contain; }}
    .nav {{ margin-top:8px; display:grid; grid-template-columns:repeat(5,1fr); text-align:center; align-items: center; }}
    .nav-img-footer {{ width: 35px; height: 35px; object-fit: contain; }}
    .bot-bg {{ width:50px; height:50px; background:white; border-radius:12px; margin: 0 auto 4px; display:flex; align-items:center; justify-content:center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }}
    
    /* جعل أزرار ستريمليت شفافة وفوق الأيقونات تماماً */
    div.stButton > button {{
        background: transparent;
        border: none;
        color: transparent;
        width: 100%;
        height: 85px;
        position: absolute;
        z-index: 10;
    }}
    div.stButton > button:hover {{ color: transparent; background: rgba(0,0,0,0.05); }}
    </style>
    """, unsafe_allow_html=True)

    # 1. الملف الشخصي
    st.markdown(f'<div class="card"><div style="display:flex; align-items:center;"><img src="data:image/png;base64,{robot_full}" style="width:95px; height:95px; object-fit:contain;"><div style="margin-left:12px;"><div style="font-size:20px; font-weight:900; color:#102646;">Welcome: User Name</div><div style="font-size:12px; color:#555;">+962 79 123 4567</div></div></div></div>', unsafe_allow_html=True)

    # 2. الرصيد
    st.markdown('<div class="title">Your Number Info</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">... Balance Info ...</div>', unsafe_allow_html=True)

    # 3. أيقونات الخدمات مع الأزرار الشفافة للتنقل
    st.markdown('<div class="grid4">', unsafe_allow_html=True)
    cols = st.columns(4)
    with cols[0]:
        st.markdown(f'<div class="mini-no-border"><img src="data:image/png;base64,{icon_internet}" class="mini-img-large"></div>', unsafe_allow_html=True)
        if st.button("btn_int", key="int"): st.session_state.page = "internet"; st.rerun()
    with cols[1]:
        st.markdown(f'<div class="mini-no-border"><img src="data:image/png;base64,{icon_renewals}" class="mini-img-large"></div>', unsafe_allow_html=True)
        if st.button("btn_ren", key="ren"): st.session_state.page = "renew"; st.rerun()
    with cols[2]:
        st.markdown(f'<div class="mini-no-border"><img src="data:image/png;base64,{icon_calls}" class="mini-img-large"></div>', unsafe_allow_html=True)
        if st.button("btn_call", key="call"): st.session_state.page = "calls"; st.rerun()
    with cols[3]:
        st.markdown(f'<div class="mini-no-border"><img src="data:image/png;base64,{icon_notifications}" class="mini-img-large"></div>', unsafe_allow_html=True)
        if st.button("btn_not", key="not"): st.session_state.page = "notif"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # 4 & 5 (التقييم والشبكة - نفس كودك الأصلي)
    st.write("... (Rest of your code) ...")

    # 6. الشريط السفلي
    st.markdown(f"""
    <div class="nav">
    <div class="nav-item"><img src="data:image/png;base64,{icon_sitting}" class="nav-img-footer"></div>
    <div class="nav-item"><img src="data:image/png;base64,{icon_spin}" class="nav-img-footer"></div>
    <div class="nav-item"><div class="bot-bg"><img src="data:image/png;base64,{robot_head}" style="width:34px;"></div></div>
    <div class="nav-item"><img src="data:image/png;base64,{icon_home}" class="nav-img-footer"></div>
    <div class="nav-item"><img src="data:image/png;base64,{icon_game}" class="nav-img-footer"></div>
    </div>
    """, unsafe_allow_html=True)

# =====================================
# توجيه الصفحات
# =====================================
elif st.session_state.page == "internet":
    internet_page.show()
elif st.session_state.page == "renew":
    renew_page.show()
elif st.session_state.page == "calls":
    calls_page.show()
elif st.session_state.page == "notif":
    notif_page.show()
