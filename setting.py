import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Settings", layout="centered")

# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "main"

# ---------------- NAV HANDLER ----------------
nav = st.query_params.get("nav")
if nav:
    st.session_state.page = nav

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
button{display:none;}
</style>
""", unsafe_allow_html=True)

# ================= MAIN =================
if st.session_state.page == "main":

    components.html("""
    <!DOCTYPE html>
    <html>
    <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>

    body{
        font-family:'Segoe UI', sans-serif;
        margin:0;
        display:flex;
        justify-content:center;
        background:transparent;
    }

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
        margin:0;
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
        transition:0.3s;
    }

    .setting-item i{
        margin-right:auto;
        color:#0f2446;
    }

    .text{
        margin-right:10px;
        font-weight:600;
        color:#0f2446;
    }

    .arrow{
        font-weight:bold;
        color:#0f2446;
    }

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

    .setting-item:hover{
        transform:translateY(-2px);
        box-shadow:0 6px 15px rgba(0,0,0,0.12);
    }

    </style>
    </head>

    <body>

    <div class="main-wrapper">

        <div class="header-container">
            <h2 class="title">Settings</h2>
        </div>

        <div class="setting-item" onclick="nav('pass')">
            <i class="fas fa-lock"></i>
            <span class="text">Change Password</span>
            <span class="arrow">›</span>
        </div>

        <div class="setting-item" onclick="nav('lang')">
            <i class="fas fa-globe"></i>
            <span class="text">Change Language</span>
            <span class="arrow">›</span>
        </div>

        <div class="setting-item" onclick="nav('rate')">
            <i class="fas fa-star"></i>
            <span class="text">Rate App</span>
            <span class="arrow">›</span>
        </div>

        <div class="setting-item" onclick="nav('logout')">
            <i class="fas fa-sign-out-alt"></i>
            <span class="text">Log Out</span>
            <span class="arrow">›</span>
        </div>

        <div class="bottom">
            <div class="setting-item" onclick="nav('report')">
                <span>⚠️ Report</span><span>›</span>
            </div>
            <div class="setting-item" onclick="nav('contact')">
                <span>✉️ Contact</span><span>›</span>
            </div>
        </div>

    </div>

    <script>
    function nav(page){
        const url = new URL(window.parent.location);
        url.searchParams.set("nav", page);
        window.parent.location.href = url.toString();
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
    body {{
        font-family:'Segoe UI';
        margin:0;
        display:flex;
        justify-content:center;
        background:transparent;
    }}

    .wrap {{
        width:100%;
        max-width:290px;
    }}

    .header {{
        display:flex;
        align-items:center;
        justify-content:center;
        margin-bottom:40px;
        position:relative;
    }}

    .back {{
        position:absolute;
        left:0;
        font-size:28px;
        font-weight:bold;
        cursor:pointer;
        color:#0f2446;
    }}

    h2 {{
        margin:0;
        font-size:20px;
        font-weight:900;
        color:#0f2446;
    }}
    </style>

    <div class="wrap">
        <div class="header">
            <div class="back" onclick="goBack()">&lt;</div>
            <h2>{title}</h2>
        </div>
    </div>

    <script>
    function goBack(){{
        const url = new URL(window.parent.location);
        url.searchParams.set("nav", "main");
        window.parent.location.href = url.toString();
    }}
    </script>
    </html>
    """, height=350)
