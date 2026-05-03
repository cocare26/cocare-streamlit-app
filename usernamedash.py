import streamlit as st
import base64
import os

# =====================================
# إعداد الصفحة
# =====================================
st.set_page_config(
    page_title="Telecom Dashboard",
    page_icon="📱",
    layout="centered"
)

# =====================================
# قراءة الصور
# =====================================
def get_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

robot_full = get_base64("robot_full.png")
robot_head = get_base64("robot_head.png")

# =====================================
# اسم المستخدم (مخفي برمجياً لتنظيف الواجهة)
# =====================================
user_name = "User Name" # يمكنكِ إرجاع st.text_input إذا أردتِ تغييره يدوياً

# =====================================
# CSS المطور لمطابقة التصميم الأصلي
# =====================================
st.markdown(f"""
<style>
/* إخفاء عناصر ستريمليت الافتراضية */
#MainMenu, header, footer {{visibility: hidden;}}

/* الخلفية العامة للموقع */
html, body, [data-testid="stAppViewContainer"] {{
    background-color: #f0f7ff;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}}

/* حاوية الموبايل الرئيسية */
.block-container {{
    max-width: 430px;
    margin: auto;
    padding: 20px 15px;
    background: linear-gradient(180deg, #e1f1ff 0%, #ffffff 100%);
    border-radius: 40px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
}}

/* العناوين الجانبية */
.section-title {{
    font-size: 18px;
    font-weight: 700;
    color: #000000;
    margin: 15px 0 10px 5px;
}}

/* تصميم الكروت البيضاء */
.card {{
    background: white;
    border-radius: 20px;
    padding: 15px;
    margin-bottom: 15px;
    box-shadow: 0 4px 15px rgba(0, 102, 204, 0.05);
    border: 1px solid #eef6ff;
}}

/* الملف الشخصي */
.profile-section {{
    display: flex;
    align-items: center;
    gap: 15px;
}}

.avatar-img {{
    width: 60px;
    height: 60px;
    object-fit: contain;
}}

.profile-info .welcome {{
    font-size: 20px;
    font-weight: 800;
    color: #1a1a1a;
}}

.profile-info .details {{
    font-size: 13px;
    color: #666;
    line-height: 1.4;
}}

.location-tag {{
    background: #eef5ff;
    color: #1a1a1a;
    padding: 8px 15px;
    border-radius: 12px;
    font-size: 14px;
    font-weight: 600;
    margin-top: 12px;
    display: flex;
    align-items: center;
    gap: 5px;
}}

/* معلومات البيانات (GB) */
.gb-title {{
    font-size: 15px;
    font-weight: 600;
    color: #444;
}}

.gb-main {{
    font-size: 38px;
    font-weight: 800;
    color: #003366;
    margin: 5px 0;
}}

.gb-unit {{ font-size: 18px; font-weight: 600; }}

.progress-container {{
    background: #e0eefc;
    height: 12px;
    border-radius: 10px;
    margin: 10px 0;
    overflow: hidden;
    position: relative;
}}

.progress-bar {{
    background: linear-gradient(90deg, #0052cc, #4ca1ff);
    width:
