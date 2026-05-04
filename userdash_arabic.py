import streamlit as st
import base64
import os

# =====================================
# إعداد الصفحة
# =====================================
st.set_page_config(
    page_title="لوحة تحكم CoCare",
    page_icon="📱",
    layout="centered"
)

# =====================================
# دالة معالجة الصور (Base64)
# =====================================
def get_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

# تحميل الصور (تأكدي من وجود الملفات بنفس الأسماء في GitHub)
robot_full = get_base64("robot_full.png")
robot_head = get_base64("robot_head.png")

# =====================================
# CSS المطور (دعم العربية والواجهة)
# =====================================
st.markdown(f"""
<style>
/* تفعيل الاتجاه من اليمين لليسار */
* {{ 
    margin:0; 
    padding:0; 
    box-sizing:border-box; 
    direction: rtl; 
    text-align: right;
}}
html, body, [data-testid="stAppViewContainer"] {{
    background:#f0f7ff;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}}
section.main > div {{ padding-top:8px; }}
div[data-testid="stVerticalBlock"] {{ gap:0rem; }}

#MainMenu, header, footer {{ visibility:hidden; }}

.block-container {{
    max-width:430px;
    margin:auto;
    padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
}}

.card {{
    background:white;
    border-radius:24px;
    padding:14px;
    margin-bottom:12px;
    box-shadow:0 6px 18px rgba(0,0,0,.08);
}}

.title {{
    font-size:17px;
    font-weight:900;
    color:#102646;
    margin: 8px 4px 8px 0;
}}

.clickable {{ cursor: pointer; transition: transform 0.2s ease; }}
.clickable:active {{ transform: scale(0.95); }}

/* العداد والمؤشر */
.needle {{
    position: absolute;
    bottom: 0;
    left: 50%;
    width: 2px;
    height: 30px;
    background: #333;
    transform-origin: bottom center;
}}

.grid4 {{ 
    display:grid; 
    grid-template-columns:repeat(4,1fr); 
    gap:8px; 
    margin: 20px 0 12px; 
}}

.mini {{
    background:white; border-radius:20px; min-height:105px;
    padding:12px 5px; text-align:center; box-shadow:0 6px 18px rgba(0,0,0,.08);
}}
.mini-text {{ font-size:11px; font-weight:800; line-height:1.2; text-align: center; }}

.robot-img-welcome {{
    width: 100px;
    height: auto;
    margin-left: 15px;
    filter: drop-shadow(0 8px 15px rgba(0,0,0,0.1));
}}

/* الشريط السفلي */
.nav {{
    margin-top:12px; display:grid; grid-template-columns:repeat(5,1fr);
    text-align:center; color:#6b6b6b; align-items: end;
}}
.nav-item {{ font-size: 22px; text-align: center; }}
.nav-text {{ font-size: 10px; display: block; text-align: center; }}
.bot-bg {{
    width:50px; height:50px; background:white; border-radius:14px;
    margin: 0 auto 5px; display:flex; align-items:center; justify-content:center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}}
.active {{ color:#0d69dd; }}
</style>
""", unsafe_allow_html=True)

# =====================================
# 1. قسم الملف الشخصي
# =====================================
st.markdown(f"""
<div class="card clickable">
    <div style="display:flex; align-items:center;">
        <img src="data:image/png;base64,{robot_full}" class="robot-img-welcome">
        <div>
            <div style="font-size:22px; font-weight:900; color:#102646;">أهلاً بك</div>
            <div style="font-size:14px; color:#555; direction: ltr; text-align: right;">+962 79 123 4567</div>
            <div style="font-size:14px; color:#555;">صالح لغاية: 25 مايو 2026</div>
        </div>
    </div>
    <div style="margin-top:12px; background:#eef5ff; padding:8px 12px; border-radius:15px; font-size:13px; font-weight:700;">
    📍 الموقع الحالي: عمان
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 2. معلومات الرصيد
# =====================================
st.markdown(f"""
<div class="title">معلومات الاشتراك</div>
<div class="card clickable">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <div style="font-size:12px; font-weight:700; color:#666;">الإنترنت المتبقي</div>
            <div style="font-size:35px; font-weight:900; color:#102646;">4.7 <span style="font-size:16px;">جيجابايت</span></div>
        </div>
        <div style="text-align: center;">
            <div style="position: relative; width: 70px; height: 35px;">
                <div style="width: 70px; height: 35px; border-radius: 70px 70px 0 0; background: linear-gradient(90deg, #0d69dd 60%, #e0e0e0 60%); position: relative; overflow: hidden;">
                    <div style="position: absolute; bottom: 0; left: 7px; width: 56px; height: 28px; background: white; border-radius: 56px 56px 0 0;"></div>
                    <div class="needle" style="transform: rotate(45deg);"></div>
                </div>
            </div>
            <div style="font-size:12px; font-weight:900; text-align: center;">إجمالي: 6 جيجابايت</div>
        </div>
    </div>
    <div style="margin-top:10px; height:8px; border-radius:10px; background:#dce8f7; overflow:hidden; position: relative;">
        <div style="width:78%; height:100%; background:#1567e0; position: absolute; right: 0;"></div>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 3. أيقونات الخدمات
# =====================================
st.markdown("""
<div class="grid4">
    <div class="mini clickable"><div style="font-size:25px;">📡</div><div class="mini-text">حزم<br>الإنترنت</div></div>
    <div class="mini clickable"><div style="font-size:25px;">🌍</div><div class="mini-text">تجديد +<br>تغيير</div></div>
    <div class="mini clickable"><div style="font-size:25px;">💰</div><div class="mini-text">اتصالات<br>دولية</div></div>
    <div class="mini clickable"><div style="font-size:25px;">🔔</div><div class="mini-text">تنبيهات<br>الشبكة</div></div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 4. التقييم وقوة الشبكة
# =====================================
st.markdown("""
<div class="title">تقييم الخدمات</div>
<div class="card">
    <div style="font-weight:900; font-size:13px;">⭐ مستوى أمان الخدمة</div>
    <div style="margin-top:8px; height:18px; border-radius:10px; background:linear-gradient(90deg,#0047ba,#27a4ff,#ff8c00,#df4126);"></div>
    <div style="text-align:center; margin-top:10px; font-size:13px; text-align: center;">قيم خدمتنا: ★ ★ ★ ★ ☆</div>
</div>

<div class="title">حالة الشبكة في منطقتك</div>
<div class="card">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <div style="font-weight:900;">📍 عمان</div>
            <div style="font-size:12px; color:green;">الإشارة: قوية جداً</div>
            <div style="display:flex; gap:5px; margin-top:5px; direction:ltr;">
                <div style="background:#f1f7ff; padding:5px; border-radius:8px; font-size:10px;">التذبذب: 19ms</div>
                <div style="background:#f1f7ff; padding:5px; border-radius:8px; font-size:10px;">الفقد: 0%</div>
            </div>
        </div>
        <div style="text-align: center;">
            <div style="width: 80px; height: 40px; border-radius: 80px 80px 0 0; background: #4caf50; position: relative;">
                <div style="position: absolute; bottom: 0; left: 10px; width: 60px; height: 30px; background: white; border-radius: 60px 60px 0 0;"></div>
            </div>
            <div style="font-size: 10px; font-weight: 700; text-align: center;">ممتاز (-68dBm)</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 5. الشريط السفلي
# =====================================
st.markdown(f"""
<div class="nav">
    <div class="nav-item">⚙️<span class="nav-text">الإعدادات</span></div>
    <div class="nav-item">🎡<span class="nav-text">اربح</span></div>
    <div class="nav-item">
        <div class="bot-bg"><img src="data:image/png;base64,{robot_head}" style="width:30px;"></div>
        <span class="nav-text">المساعد</span>
    </div>
    <div class="nav-item active">🏠<span class="nav-text">الرئيسية</span></div>
    <div class="nav-item">🎁<span class="nav-text">العروض</span></div>
</div>
""", unsafe_allow_html=True)
