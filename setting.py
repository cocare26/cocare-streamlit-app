import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(page_title="Settings UI", layout="centered")

# 2. Navigation Logic (Page Router)
# We read the 'page' parameter from the URL
query_params = st.query_params
if "page" in query_params:
    st.session_state.page = query_params["page"]
elif 'page' not in st.session_state:
    st.session_state.page = 'main'

# Function to return to the main settings menu
def go_back():
    st.query_params.clear()
    st.session_state.page = 'main'
    st.rerun()

# 3. Handle Sub-pages
if st.session_state.page == "Change_password":
    st.title("🔒 Change Password")
    st.info("The password reset form would go here.")
    if st.button("Back to Settings"):
        go_back()
    st.stop()

if st.session_state.page == "Change_language":
    st.title("🌐 Change Language")
    st.write("Select your preferred language.")
    if st.button("Back to Settings"):
        go_back()
    st.stop()

# 4. Main Settings UI
st.markdown("""
<style>
:root{
    --navy:#0f2446;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}
[data-testid="stAppViewContainer"]{ background:#eef2f7; }
.block-container{
    max-width:350px !important;
    margin:auto !important;
    padding:30px !important;
    background:linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius:42px;
    box-shadow:0 15px 35px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
body{ font-family:'Segoe UI', sans-serif; margin:0; display:flex; justify-content:center; background:transparent; }
.main-wrapper{ width:100%; max-width:290px; display:flex; flex-direction:column; height:480px; }
.header-container{ display:flex; align-items:center; justify-content:center; margin-bottom:35px; position:relative; }
.back-icon{ position:absolute; left:0; font-size:28px; font-weight:bold; color:#0f2446; cursor:pointer; }
.title{ margin:0; font-weight:900; font-size:20px; color:#0f2446; }
.setting-item{ background:white; border-radius:100px; padding:14px 18px; margin-bottom:15px; display:flex; align-items:center; justify-content:space-between; box-shadow:0 4px 12px rgba(0,0,0,0.08); cursor:pointer; transition:0.3s; text-decoration:none; }
.setting-item i{ color:#0f2446; font-size:16px; margin-right:15px; }
.setting-text{ flex:1; text-align:left; font-size:14px; font-weight:600; color:#0f2446; }
.setting-item .arrow{ margin-left:10px; color:#0f2446; font-weight:bold; }
.setting-item:hover{ transform:translateY(-2px); box-shadow:0 6px 15px rgba(0,0,0,0.12); }
.bottom-row{ margin-top:auto; display:flex; gap:10px; }
.bottom-row .setting-item{ flex:1; padding:12px 14px; flex-direction: column; border-radius: 20px; text-align: center; }
.bottom-row .setting-text{ font-size:12px; margin: 5px 0 0 0; text-align:center; }
</style>
</head>
<body>
<div class="main-wrapper">
    <div class="header-container">
        <div class="back-icon" onclick="goPage('customer')">&lt;</div>
        <h2 class="title">Settings</h2>
    </div>

    <div class="setting-item" onclick="goPage('Change_password')">
        <i class="fas fa-lock"></i>
        <span class="setting-text">Change Password</span>
        <span class="arrow">›</span>
    </div>

    <div class="setting-item" onclick="goPage('Change_language')">
        <i class="fas fa-globe"></i>
        <span class="setting-text">Change Language</span>
        <span class="arrow">›</span>
    </div>

    <div class="setting-item" onclick="goPage('Rate_app')">
        <i class="fas fa-star"></i>
        <span class="setting-text">Rate App</span>
        <span class="arrow">›</span>
    </div>

    <div class="setting-item" onclick="goPage('logout')">
        <i class="fas fa-sign-out-alt"></i>
        <span class="setting-text">Log Out</span>
        <span class="arrow">›</span>
    </div>

    <div class="bottom-row">
        <div class="setting-item" onclick="goPage('Report_Problem')">
            <i class="fas fa-exclamation-triangle"></i>
            <span class="setting-text">Report Problem</span>
        </div>
        <div class="setting-item" onclick="goPage('Contact_Us')">
            <i class="fas fa-envelope"></i>
            <span class="setting-text">Contact Us</span>
        </div>
    </div>
</div>

<script>
function goPage(p){
    // This updates the parent URL, triggering Streamlit to rerun and read the new query param
    window.top.location.href = window.top.location.pathname + "?page=" + p;
}
</script>
</body>
</html>
""", height=500)
