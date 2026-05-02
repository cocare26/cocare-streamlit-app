import streamlit as st

# إضافة CSS مخصص مع التعديلات الجديدة للألوان
st.markdown("""
    <style>
    /* تغيير خلفية التطبيق لـ بيبي بلو */
    .stApp {
        background-color: #E0F7FA; /* بيبي بلو هادئ */
    }

    /* تنسيق العنوان والسهم */
    .header-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 10px 0;
        margin-bottom: 20px;
    }
    .back-arrow {
        font-size: 24px;
        font-weight: bold;
        cursor: pointer;
        color: white; /* سهم أبيض */
    }
    .settings-title {
        font-size: 28px;
        font-weight: bold;
        margin-right: 20px;
        color: black; /* عنوان أسود */
    }

    /* تنسيق الأزرار والقوائم */
    .menu-item {
        background-color: white;
        border-radius: 15px;
        padding: 12px 20px;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.05);
    }
    
    /* تصغير الخط للنصوص الأساسية + لون أسود */
    .menu-text {
        font-size: 14px; 
        font-weight: 600;
        margin-left: 15px;
        flex-grow: 1;
        text-align: right;
        color: black; /* نص أسود */
    }

    .emoji {
        font-size: 20px;
    }

    /* تنسيق قسم التقرير والتواصل (جنب بعض) */
    .bottom-row {
        display: flex;
        gap: 10px;
    }
    .small-button {
        flex: 1;
        background-color: white;
        border-radius: 15px;
        padding: 10px;
        display: flex;
        align-items: center;
    }
    .small-text {
        font-size: 12px;
        font-weight: bold;
        margin-left: 5px;
        color: black; /* نص أسود */
    }
    </style>
    """, unsafe_allow_html=True)

# --- بناء واجهة المستخدم ---

# الهيدر: سهم على أقصى الشمال وكلمة Settings لليمين
st.markdown("""
    <div class="header-container">
        <div class="back-arrow"> &lt; </div>
        <div class="settings-title">Settings</div>
        <div></div> <!-- موازن للمساحة -->
    </div>
    """, unsafe_allow_html=True)

# الأزرار الرئيسية بخط أصغر ولون أسود
menu_items = [
    ("🔐", "Change Password"),
    ("🌐", "Change Language"),
    ("⭐", "Rate App"),
    ("🚪", "Log Out")
]

for emoji, text in menu_items:
    st.markdown(f"""
        <div class="menu-item">
            <span class="emoji">{emoji}</span>
            <span class="menu-text">{text}</span>
        </div>
        """, unsafe_allow_html=True)

# الصف الأخير: Report a Problem و Contact Us (لون أسود)
st.markdown("""
    <div class="bottom-row">
        <div class="small-button">
            <span class="emoji">⚠️</span>
            <span class="small-text">Report a Problem</span>
        </div>
        <div class="small-button">
            <span class="emoji">✉️</span>
            <span class="small-text">Contact Us</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
