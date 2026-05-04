import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
[data-testid="stAppViewContainer"] { background:#f0f7ff; }
.block-container {
    max-width:430px; margin:auto; padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100% );
    border-radius:42px; box-shadow:0 14px 35px rgba(0,0,0,.15);
    min-height: 600px;
}
#MainMenu, header, footer { visibility:hidden; }

.main-wrapper { width:100%; display:flex; flex-direction:column; height:550px; }
.header-container { display:flex; align-items:center; justify-content:center; margin-bottom:35px; position:relative; padding-top:10px; }
.back-btn { background:none; border:none; font-size:28px; font-weight:bold; color:#102646; cursor:pointer; padding:0; }
.title { margin:0; font-weight:900; font-size:20px; color:#102646; }

.setting-btn {
    width: 100%;
    background: white;
    border-radius: 100px;
    padding: 14px 22px;
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    border: none;
    cursor: pointer;
    transition: 0.3s;
    font-family: inherit;
}
.setting-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 15px rgba(0,0,0,0.12); }
.item-left { display: flex; align-items: center; gap: 12px; pointer-events: none; }
.item-left i { color: #102646; font-size: 16px; width: 20px; text-align: center; }
.item-text { color: #102646; font-weight: 800; font-size: 14px; }
.arrow { color: #102646; font-weight: bold; font-size: 18px; pointer-events: none; }

.bottom-row { display: flex; gap: 10px; margin-top: auto; padding-bottom: 10px; }
.bottom-btn {
    flex: 1;
    background: white;
    border-radius: 100px;
    padding: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    border: none;
    cursor: pointer;
    font-family: inherit;
}
.bottom-btn span { color: #102646; font-weight: 800; font-size: 12px; }
.bottom-btn i { color: #102646; font-size: 14px; }
</style>

<div class="main-wrapper">
    <div class="header-container">
        <form action="/" method="get" style="position:absolute; left:0;">
            <input type="hidden" name="page" value="customer">
            <button type="submit" class="back-btn">‹</button>
        </form>
        <h2 class="title">Settings</h2>
    </div>

    <form action="/" method="get">
        <input type="hidden" name="page" value="Change_password">
        <button type="submit" class="setting-btn">
            <div class="item-left"><i class="fas fa-lock"></i><span class="item-text">Change Password</span></div>
            <span class="arrow">›</span>
        </button>
    </form>

    <form action="/" method="get">
        <input type="hidden" name="page" value="Change_language">
        <button type="submit" class="setting-btn">
            <div class="item-left"><i class="fas fa-globe"></i><span class="item-text">Change Language</span></div>
            <span class="arrow">›</span>
        </button>
    </form>

    <form action="/" method="get">
        <input type="hidden" name="page" value="Rate_app">
        <button type="submit" class="setting-btn">
            <div class="item-left"><i class="fas fa-star"></i><span class="item-text">Rate App</span></div>
            <span class="arrow">›</span>
        </button>
    </form>

    <form action="/" method="get">
        <input type="hidden" name="page" value="logout">
        <button type="submit" class="setting-btn">
            <div class="item-left"><i class="fas fa-sign-out-alt"></i><span class="item-text">Log Out</span></div>
            <span class="arrow">›</span>
        </button>
    </form>

    <div class="bottom-row">
        <form action="/" method="get" style="flex:1;">
            <input type="hidden" name="page" value="Report_Problem">
            <button type="submit" class="bottom-btn">
                <i class="fas fa-exclamation-triangle"></i><span>Report Problem</span>
            </button>
        </form>
        <form action="/" method="get" style="flex:1;">
            <input type="hidden" name="page" value="Contact_Us">
            <button type="submit" class="bottom-btn">
                <i class="fas fa-envelope"></i><span>Contact Us</span>
            </button>
        </form>
    </div>
</div>
""", unsafe_allow_html=True)
