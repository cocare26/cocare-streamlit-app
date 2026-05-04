import streamlit as st
import base64
import os

# =====================================
# إعداد الصفحة
# =====================================
st.set_page_config(
    page_title="لوحة تحكم الاتصالات",
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

# تحميل الصور بناءً على الأسماء في مستودعك
robot_full = get_base64("robot_full.png.jpeg") 
robot_head = get_base64("robot_head.png")

# =====================================
# CSS المطور (عربي بالكامل وتفاعلي)
# =====================================
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');

* {{ 
    margin:0; padding:0; box-sizing:border-box; 
    direction: rtl; 
    font-family: 'Cairo', sans-serif;
}}

html, body, [data-testid="stAppViewContainer"] {{
    background:#f0f7ff;
}}

section.main > div {{ padding-top:10px; }}
div[data-testid="stVerticalBlock"] {{ gap:0rem; }}

#MainMenu, header, footer {{ visibility:hidden; }}

.block-container {{
    max-width:430px;
    margin:auto;
    padding:15px;
    background: linear-gradient(180deg, #bde4ff 0%, #e1f2ff 100%);
    border-radius:30px;
}}

.card {{
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(10px);
    border-radius: 25px;
    padding: 18px;
    margin-bottom: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}}

.title {{
    font-size: 16px;
    font-weight: 800;
    color: #0b2d5e;
    margin: 15px 5px 10px 0;
}}

/* تكبير صورة الروبوت */
.robot-welcome {{
    width: 90px; 
    height: 90px;
    object-fit: contain;
    filter: drop-shadow(0 4px 8px rgba(0,0,0,0.1));
}}

/* تفاعل أيقونات الخدمات */
.service-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin: 25px 0; /* مساحة إضافية */
}}

.service-item {{
    background: rgba(255, 255, 255, 0.8);
    border-radius: 20px;
    padding: 15px 5px;
    text-align: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}}

.service-item:hover {{
    transform: scale(1.15) translateY(-5px);
    background: #ffffff;
    box-shadow: 0 10px 20px rgba(0,0,0,0.12);
}}

.service-icon {{
    font-size: 32px; 
    margin-bottom: 8px;
    display: block;
}}

/* النجوم التفاعلية */
.rating-stars {{
    display: flex;
    flex-direction: row-reverse;
    justify-content: center;
    gap: 8px;
}}
.rating-stars input {{ display: none; }}
.rating-stars label {{
    font-size: 38px;
    color: #ddd;
    cursor: pointer;
    transition: 0.2s;
}}
.rating-stars label:hover,
.rating-stars label:hover ~ label,
.rating-stars input:checked ~ label {{
    color: #ffc107;
    transform: scale(1.1);
}}

/* الشريط السفلي المكبر */
.bottom-nav {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    padding: 20px 0;
    text-align: center;
    align-items: end;
}}

.nav-btn {{
    color: #7a8ba3;
    font-size: 13px;
    font-weight: 700;
    cursor: pointer;
}}

.nav-icon-large {{
    font-size: 30px; 
    display: block;
    margin-bottom: 5px;
    transition: 0.3s;
}}

.nav-btn:hover .nav-icon-large {{
    transform: scale(1.2);
    color: #0d69dd;
}}

.chat-bot-btn {{
    background: white;
    width: 65px; 
    height: 65px;
    border-radius: 20px;
    margin: 0 auto 5px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 6px 15px rgba(0,0,0,0.15);
    transition: 0.3s;
}}

.chat-bot-btn:hover {{
    transform: scale(1.1) rotate(-8deg);
}}
</style>
""", unsafe_allow_html=True)

# =====================================
# الواجهة البرمجية
# =====================================

# 1. الترحيب (بدون خانة إدخال)
st.markdown(f"""
<div class="card">
    <div style="display: flex; align-items: center; justify-content: space-between;">
        <div style="text-align: right;">
            <div style="font-size: 28px; font-weight: 900; color: #0b2d5e; margin-bottom: 5px;">أهلاً بك</div>
            <div style="font-size: 14px; color: #555; direction: ltr;">+962 79 123 4567</div>
            <div style="font-size: 14px; color: #777;">صالح لغاية: 25 مايو، 2026</div>
        </div>
        <img src="data:image/png;base64,{robot_full}" class="robot-welcome">
    </div>
</div>
""", unsafe_allow_html=True)

# 2. معلومات الرصيد
st.markdown('<div class="title">معلومات رقمك</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="card">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div style="text-align: center;">
            <div style="font-size: 14px; font-weight: 900; color: #0b2d5e;">6 جيجا</div>
            <div style="font-size: 24px;">📊</div>
        </div>
        <div style="text-align: left;">
            <div style="font-size: 13px; font-weight: 700; color: #666;">الرصيد المتبقي</div>
            <div style="font-size: 42px; font-weight: 900; color: #0b2d5e; line-height: 1;">4.7 <span style="font-size: 18px;">GB</span></div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 3. أيقونات الخدمات (تفاعلية وتحركها عند التأشير)
st.markdown(f"""
<div class="service-grid">
    <div class="service-item">
        <span class="service-icon">📡</span>
        <span class="service-text">حزم<br>الإنترنت</span>
    </div>
    <div class="service-item">
        <span class="service-icon">🔄</span>
        <span class="service-text">تجديد +<br>تغيير</span>
    </div>
    <div class="service-item">
        <span class="service-icon">💰</span>
        <span class="service-text">اتصالات<br>دولية</span>
    </div>
    <div class="service-item">
        <span class="service-icon">🔔</span>
        <span class="service-text">تنبيهات<br>الشبكة</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. التقييم التفاعلي
st.markdown('<div class="title">تقييم الخدمة</div>', unsafe_allow_html=True)
st.markdown("""
<div class="card">
    <div style="text-align: center;">
        <div style="font-size: 14px; font-weight: 700; color: #333; margin-bottom: 10px;">قيم تجربتك معنا</div>
        <div class="rating-stars">
            <input type="radio" name="star" id="s5"><label for="s5">★</label>
            <input type="radio" name="star" id="s4"><label for="s4">★</label>
            <input type="radio" name="star" id="s3"><label for="s3">★</label>
            <input type="radio" name="star" id="s2"><label for="s2">★</label>
            <input type="radio" name="star" id="s1"><label for="s1">★</label>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 5. الشريط السفلي المكبر
st.markdown(f"""
<div class="bottom-nav">
    <div class="nav-btn"><span class="nav-icon-large">⚙️</span>الإعدادات</div>
    <div class="nav-btn"><span class="nav-icon-large">🎡</span>اربح</div>
    <div class="nav-btn">
        <div class="chat-bot-btn">
            <img src="data:image/png;base64,{robot_head}" style="width: 45px;">
        </div>
        المساعد
    </div>
    <div class="nav-btn" style="color:#0d69dd;"><span class="nav-icon-large">🏠</span>الرئيسية</div>
    <div class="nav-btn"><span class="nav-icon-large">🎁</span>الألعاب</div>
</div>
""", unsafe_allow_html=True)
