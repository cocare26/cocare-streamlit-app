import streamlit as st

# إعداد روابط الصفحات (استبدل الروابط بالصفحات الفعلية في تطبيقك)
links = {
    "change_password": "?page=password",
    "change_language": "?page=language",
    "rate_app": "?page=rate",
    "logout": "?page=logout",
    "report": "?page=report",
    "contact": "?page=contact"
}

st.markdown(f"""
    <style>
    /* 1. الخلفية بيبي بلو */
    .stApp {{
        background-color: #E0F7FA;
    }}

    .main-container {{
        max-width: 400px;
        margin: 0 auto;
        padding-top: 30px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}

    /* 2. سهم السيتنج العلوي أسود */
    .header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
    }}
    .back-arrow-top {{
        color: black; 
        font-size: 22px;
        text-decoration: none;
        font-weight: bold;
    }}
    .title {{
        color: black;
        font-size: 22px;
        font-weight: bold;
        margin-right: 10px;
    }}

    /* 3. تنسيق الأزرار كروابط */
    .menu-item-link {{
        text-decoration: none;
        color: inherit;
        display: block;
        margin-bottom: 12px;
    }}

    .menu-button {{
        background-color: white;
        border-radius: 50px;
        padding: 12px 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
        transition: 0.3s;
    }}
    
    .menu-button:hover {{
        transform: scale(1.02);
        background-color: #f8f9fa;
    }}

    .left-section {{
        display: flex;
        align-items: center;
        gap: 12px;
    }}

    .menu-text {{
        color: black;
        font-size: 15px;
        font-weight: 500;
    }}

    /* 4. الأسهم الجانبية بيضاء وعلى اليمين */
    .arrow-right {{
        background-color: white; /* لجعل السهم يظهر إذا كانت الخلفية بيضاء، نضع له حاوية أو نغير لونه */
        color: #FFFFFF; /* لون السهم أبيض */
        background: #f0f0f0; /* خلفية دائرية خفيفة للسهم ليظهر الأبيض بوضوح */
        width: 24px;
        height: 24px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 12px;
        font-weight: bold;
        text-shadow: 0px 0px 2px rgba(0,0,0,0.2); /* ظل خفيف للسهم الأبيض */
    }}

    .bottom-row {{
        display: flex;
        gap: 10px;
    }}
    .small-btn {{
        flex: 1;
        background-color: white;
        border-radius: 50px;
        padding: 10px 15px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }}
    </style>

    <div class="main-container">
        <div class="header">
            <a href="#" class="back-arrow-top"> &lt; </a>
            <div class="title">Settings</div>
            <div style="width:20px;"></div>
        </div>

        <a href="{links['change_password']}" class="menu-item-link">
            <div class="menu-button">
                <div class="left-section"><span>🔐</span> <span class="menu-text">Change Password</span></div>
                <div class="arrow-right"> &gt; </div>
            </div>
        </a>

        <a href="{links['change_language']}" class="menu-item-link">
            <div class="menu-button">
                <div class="left-section"><span>🌐</span> <span class="menu-text">Change Language</span></div>
                <div class="arrow-right"> &gt; </div>
            </div>
        </a>

        <a href="{links['rate_app']}" class="menu-item-link">
            <div class="menu-button">
                <div class="left-section"><span>⭐</span> <span class="menu-text">Rate App</span></div>
                <div class="arrow-right"> &gt; </div>
            </div>
        </a>

        <a href="{links['logout']}" class="menu-item-link">
            <div class="menu-button">
                <div class="left-section"><span>🚪</span> <span class="menu-text">Log Out</span></div>
                <div class="arrow-right"> &gt; </div>
            </div>
        </a>

        <div class="bottom-row">
            <a href="{links['report']}" class="menu-item-link" style="flex:1;">
                <div class="small-btn">
                    <div class="left-section" style="gap:5px;"><span>⚠️</span><span class="menu-text" style="font-size:12px;">Report</span></div>
                    <div class="arrow-right" style="width:18px; height:18px; font-size:10px;"> &gt; </div>
                </div>
            </a>
            <a href="{links['contact']}" class="menu-item-link" style="flex:1;">
                <div class="small-btn">
                    <div class="left-section" style="gap:5px;"><span>✉️</span><span class="menu-text" style="font-size:12px;">Contact</span></div>
                    <div class="arrow-right" style="width:18px; height:18px; font-size:10px;"> &gt; </div>
                </div>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
