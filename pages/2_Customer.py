import streamlit as st
import base64
import os

# 1. إعداد الصفحة الأساسي (يجب أن يكون أول أمر في ستريم ليت)
st.set_page_config(page_title="CoCare Dashboard", page_icon="📱", layout="centered")

# دالة لتحويل الصور لـ Base64 (تم تحديث المسار للبحث في pages لأن صورك هناك)
def get_base64(file_name):
    # نبحث عن الصورة في المجلد الرئيسي أو داخل مجلد pages بناءً على صورك
    paths_to_check = [file_name, os.path.join("pages", file_name)]
    for path in paths_to_check:
        if os.path.exists(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    return ""

# تحميل الصور (تأكدي من مطابقة الأسماء تماماً لما في GitHub)
robot_full = get_base64("robot_full.png.jpeg")
robot_head = get_base64("robot_head.png")
icon_internet = get_base64("internet.png")
icon_renewals = get_base64("renewals.png")
icon_calls = get_base64("calls.png")
icon_notifications = get_base64("notifications.png")
icon_sitting = get_base64("sitting.png")
icon_spin = get_base64("spin.png")
icon_home = get_base64("home.png.jpeg") # أضفت .jpeg بناءً على صورتك
icon_game = get_base64("game.png.jpeg") # أضفت .jpeg بناءً على صورتك

# 2. تصميم الواجهة (CSS)
st.markdown(f"""
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body, [data-testid="stAppViewContainer"] {{ background:#f0f7ff; font-family:'Segoe UI', sans-serif; }}
#MainMenu, header, footer {{ visibility:hidden; }}
.block-container {{ max-width:430px; margin:auto; padding:12px 16px; background: linear-gradient(180deg, #FFFFFF 0%, #E3F2FD 30%, #BBDEFB 100%); border-radius:42px; box-shadow:0 14px 35px rgba(0,0,0,.15); }}
.card {{ background: white; border-radius: 20px; padding: 10px 14px; margin-bottom: 8px; box-shadow: 0 4px 15px rgba(0,0,0,.05); }}
.title {{ font-size:15px; font-weight:900; color:#102646; margin: 4px 0 4px 4px; }}
.hover-effect {{ transition: 0.3s ease-in-out; cursor: pointer; text-align:center; }}
.hover-effect:hover {{ transform: scale(1.1); }}
.nav-img-footer {{ width: 35px; height: 35px; object-fit: contain; }}

/* جعل أزرار ستريم ليت شفافة تماماً فوق الأيقونات */
div.stButton > button {{
    background: transparent !important;
    border: none !important;
    color: transparent !important;
    width: 100%;
    height: 90px;
    position: absolute;
    top: 0;
    z-index: 10;
}}
</style>
""", unsafe_allow_html=True)

# 3. محتوى الصفحة الرئيسية
# كارت الترحيب
st.markdown(f'''<div class="card"><div style="display:flex; align-items:center;"><img src="data:image/png;base64,{robot_full}" style="width:90px;"><div style="margin-left:12px;"><div style="font-size:18px; font-weight:900;">Welcome: Farah</div><div style="font-size:12px; color:gray;">+962 79 123 4567</div></div></div></div>''', unsafe_allow_html=True)

# الخدمات (الأيقونات الأربعة في الوسط)
st.markdown('<div class="title">Services</div>', unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f'<div class="hover-effect"><img src="data:image/png;base64,{icon_internet}" style="width:70px;"><br><small>Internet</small></div>', unsafe_allow_html=True)
    if st.button(" ", key="btn_int"): st.switch_page("pages/internet_page.py")
with c2:
    st.markdown(f'<div class="hover-effect"><img src="data:image/png;base64,{icon_renewals}" style="width:70px;"><br><small>Renew</small></div>', unsafe_allow_html=True)
    if st.button(" ", key="btn_ren"): st.switch_page("pages/renew_page.py")
with c3:
    st.markdown(f'<div class="hover-effect"><img src="data:image/png;base64,{icon_calls}" style="width:70px;"><br><small>Calls</small></div>', unsafe_allow_html=True)
    if st.button(" ", key="btn_call"): st.switch_page("pages/calls_page.py")
with c4:
    st.markdown(f'<div class="hover-effect"><img src="data:image/png;base64,{icon_notifications}" style="width:70px;"><br><small>Notif</small></div>', unsafe_allow_html=True)
    if st.button(" ", key="btn_not"): st.switch_page("pages/notif_page.py")

# الشريط السفلي (Navigation)
st.write("---")
n1, n2, n3, n4, n5 = st.columns(5)

with n1:
    st.markdown(f'<div style="text-align:center;"><img src="data:image/png;base64,{icon_sitting}" class="nav-img-footer"></div>', unsafe_allow_html=True)
    if st.button(" ", key="nav_set"): st.switch_page("pages/Settings.py")
with n2:
    st.markdown(f'<div style="text-align:center;"><img src="data:image/png;base64,{icon_spin}" class="nav-img-footer"></div>', unsafe_allow_html=True)
with n3:
    st.markdown(f'<div style="text-align:center;"><img src="data:image/png;base64,{robot_head}" style="width:35px;"></div>', unsafe_allow_html=True)
    if st.button(" ", key="nav_bot"): st.switch_page("pages/Chatbot.py") # تأكدي من اسم الملف
with n4:
    st.markdown(f'<div style="text-align:center;"><img src="data:image/png;base64,{icon_home}" class="nav-img-footer"></div>', unsafe_allow_html=True)
    if st.button(" ", key="nav_home"): st.rerun()
with n5:
    st.markdown(f'<div style="text-align:center;"><img src="data:image/png;base64,{icon_game}" class="nav-img-footer"></div>', unsafe_allow_html=True)
    if st.button(" ", key="nav_game"): st.switch_page("pages/_Game_E.py")
