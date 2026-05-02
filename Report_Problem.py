import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Report a Problem", layout="centered")

st.markdown("""
<style>

/* 🎯 ألوان أساسية */
:root{
    --navy:#0f2446;
    --accent:#2f80ed;
    --accent2:#1c6fa4;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}

/* 📱 خلفية الصفحة */
[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}

/* 📦 الكارد الرئيسي */
.block-container{
    max-width:420px;
    margin:auto;
    padding:25px 30px;

    background:linear-gradient(160deg,
        var(--bg1) 0%,
        var(--bg2) 45%,
        var(--bg3) 100%
    );

    border-radius:42px;
    box-shadow:0 10px 30px rgba(0,0,0,.15);
}

/* 🧠 العناوين */
h1, h2, h3{
    color:var(--navy);
    text-align:center;
    font-weight:900;
}

/* 🧾 Inputs */
div[data-testid="stTextInput"] input{
    border-radius:25px;
    height:44px;
    border:none !important;
    outline:none !important;
    padding-left:16px;
    background:rgba(255,255,255,0.95);
}

/* 📍 Select */
div[data-testid="stSelectbox"] div{
    border-radius:25px;
}

/* 🔘 الأزرار الأساسية */
div.stButton > button{
    width:100%;
    height:46px;
    border-radius:25px;
    border:none;

    background:linear-gradient(90deg,
        var(--accent),
        var(--accent2)
    );

    color:white;
    font-weight:bold;

    box-shadow:0 6px 14px rgba(47,128,237,.25);
}

/* ✨ hover */
div.stButton > button:hover{
    transform:translateY(-2px);
    box-shadow:0 8px 18px rgba(0,0,0,.2);
}

/* 🤍 زر ثانوي */
div.stButton:nth-of-type(1) > button{
    background:white;
    color:var(--navy);
    box-shadow:0 2px 8px rgba(0,0,0,.1);
}

.report-textarea {
    width: 100%;
    height: 150px;
    border-radius: 25px;
    border: none;
    outline: none;
    padding: 15px;
    background: rgba(255,255,255,0.95);
    font-size: 16px;
    color: var(--navy);
    resize: none;
    margin-bottom: 20px;
}
.send-report-button {
    width: 100%;
    height: 46px;
    border-radius: 25px;
    border: none;
    background: linear-gradient(90deg, var(--accent), var(--accent2));
    color: white;
    font-weight: bold;
    box-shadow: 0 6px 14px rgba(47,128,237,.25);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    transition: all 0.2s ease-in-out;
}
.send-report-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 18px rgba(0,0,0,.2);
}
</style>
""", unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html>
<head>
    <title>Report a Problem</title>
</head>
<body>
    <div class="block-container">
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <a href="/?page=settings" style="text-decoration: none; color: var(--navy); font-size: 24px; margin-right: 10px;">←</a>
            <h3 style="margin: 0;">Report a Problem</h3>
        </div>

        <textarea class="report-textarea" placeholder="I need help"></textarea>

        <button class="send-report-button" onclick="alert(\'Report Sent!\')">
            <span>Send Report</span>
            <span>✉️</span>
        </button>
    </div>
</body>
</html>
""", height=700)
