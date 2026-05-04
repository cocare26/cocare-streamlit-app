import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Settings", layout="centered")

# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "main"

def go(page):
    st.session_state.page = page
    st.rerun()

# ---------------- STYLE ----------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}
.block-container{
    max-width:350px !important;
    margin:auto !important;
    padding:30px !important;
    background:linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
    border-radius:42px;
    box-shadow:0 15px 35px rgba(0,0,0,0.15);
}
button[kind="secondary"]{
    display:none;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HIDDEN BUTTONS ----------------
if st.button("pass", key="pass_btn"): go("pass")
if st.button("lang", key="lang_btn"): go("lang")
if st.button("rate", key="rate_btn"): go("rate")
if st.button("logout", key="logout_btn"): go("logout")
if st.button("report", key="report_btn"): go("report")
if st.button("contact", key="contact_btn"): go("contact")
if st.button("back", key="back_btn"): go("main")

# ================= MAIN =================
if st.session_state.page == "main":

    components.html("""
    <html>
    <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
    body{font-family:'Segoe UI';margin:0;display:flex;justify-content:center;background:transparent}

    .main-wrapper{
        width:100%;
        max-width:290px;
        display:flex;
        flex-direction:column;
        height:480px;
    }

    .header-container{
        display:flex;
        align-items:center;
        justify-content:center;
        margin-bottom:35px;
    }

    .title{
        font-weight:900;
        font-size:20px;
        color:#0f2446;
    }

    .setting-item{
        background:white;
        border-radius:100px;
        padding:14px 18px;
        margin-bottom:15px;
        display:flex;
        align-items:center;
        box-shadow:0 4px 12px rgba(0,0,0,0.08);
        cursor:pointer;
    }

    .setting-item i{margin-right:auto;color:#0f2446}
    .text{margin-right:10px;color:#0f2446;font-weight:600}
    .arrow{color:#0f2446;font-weight:bold}

    .bottom{
        margin-top:auto;
        display:flex;
        gap:10px;
    }

    .bottom .setting-item{
        flex:1;
        justify-content:space-between;
        font-size:13px;
    }

    </style>
    </head>

    <body>
    <div class="main-wrapper">

        <div class="header-container">
            <h2 class="title">Settings</h2>
        </div>

        <div class="setting-item" onclick="clickBtn('pass_btn')">
            <i class="fas fa-lock"></i>
            <span class="text">Change Password</span>
            <span class="arrow">›</span>
        </div>

        <div class="setting-item" onclick="clickBtn('lang_btn')">
            <i class="fas fa-globe"></i>
            <span class="text">Change Language</span>
            <span class="arrow">›</span>
        </div>

        <div class="setting-item" onclick="clickBtn('rate_btn')">
            <i class="fas fa-star"></i>
            <span class="text">Rate App</span>
            <span class="arrow">›</span>
        </div>

        <div class="setting-item" onclick="clickBtn('logout_btn')">
            <i class="fas fa-sign-out-alt"></i>
            <span class="text">Log Out</span>
            <span class="arrow">›</span>
        </div>

        <div class="bottom">
            <div class="setting-item" onclick="clickBtn('report_btn')">
                ⚠️ Report <span>›</span>
            </div>
            <div class="setting-item" onclick="clickBtn('contact_btn')">
                ✉️ Contact <span>›</span>
            </div>
        </div>

    </div>

    <script>
    function clickBtn(key){
        parent.document.querySelector('button[key="'+key+'"]').click();
    }
    </script>

    </body>
    </html>
    """, height=500)

# ================= SUB PAGES =================
else:

    titles = {
        "pass":"Change Password",
        "lang":"Language",
        "rate":"Rate App",
        "logout":"Log Out",
        "report":"Report",
        "contact":"Contact Us"
    }

    title = titles[st.session_state.page]

    components.html(f"""
    <html>
    <style>
    body{{font-family:'Segoe UI';margin:0;background:transparent}}

    .header{{
        display:flex;
        align-items:center;
        justify-content:center;
        position:relative;
        margin-bottom:30px;
    }}

    .back{{
        position:absolute;
        left:0;
        font-size:28px;
        cursor:pointer;
        color:#0f2446;
        font-weight:bold;
    }}

    h2{{
        font-size:20px;
        font-weight:900;
        color:#0f2446;
    }}
    </style>

    <div class="header">
        <div class="back" onclick="goBack()">&lt;</div>
        <h2>{title}</h2>
    </div>


<script>
function goBack(){{
    parent.document.querySelector('button[key="back_btn"]').click();
}}
</script>

    </html>
    """, height=150)
