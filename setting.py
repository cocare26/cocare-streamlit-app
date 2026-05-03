import streamlit as st
import streamlit.components.v1 as components

# 1. Page Config
st.set_page_config(page_title="Settings", layout="centered")

# 2. Initialize Session State
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# Function to switch pages
def set_page(page_name):
    st.session_state.page = page_name

# 3. Page Router
if st.session_state.page == "Change_password":
    st.title("🔒 Change Password")
    # Your password form here
    st.text_input("New Password", type="password")
    if st.button("Back to Settings"):
        st.session_state.page = 'main'
        st.rerun()
    st.stop()

elif st.session_state.page == "Change_language":
    st.title("🌐 Change Language")
    st.selectbox("Select Language", ["English", "Arabic"])
    if st.button("Back"):
        st.session_state.page = 'main'
        st.rerun()
    st.stop()

# 4. Main Settings UI Styles
st.markdown("""
<style>
:root{ --navy:#0f2446; --bg1:#d6ecff; --bg2:#bfe3ff; --bg3:#eaf6ff; }
[data-testid="stAppViewContainer"]{ background:#eef2f7; }
.block-container{
    max-width:350px !important; margin:auto !important; padding:30px !important;
    background:linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius:42px; box-shadow:0 15px 35px rgba(0,0,0,0.15);
}
/* Hide the actual Streamlit widgets we use for syncing */
.hidden-btn { display: none; }
</style>
""", unsafe_allow_html=True)

# 5. The "Magic" Link
# We use a simple component that sends data back to Streamlit
res = components.html(f"""
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
body{{ font-family:'Segoe UI', sans-serif; margin:0; display:flex; justify-content:center; background:transparent; overflow:hidden; }}
.main-wrapper{{ width:100%; max-width:290px; display:flex; flex-direction:column; }}
.header-container{{ display:flex; align-items:center; justify-content:center; margin-bottom:35px; position:relative; }}
.title{{ margin:0; font-weight:900; font-size:20px; color:#0f2446; }}

.setting-item{{
    background:white; border-radius:100px; padding:14px 18px; margin-bottom:15px;
    display:flex; align-items:center; box-shadow:0 4px 12px rgba(0,0,0,0.08);
    cursor:pointer; transition:0.3s;
}}
.setting-item i.left-icon{{ color:#0f2446; font-size:16px; margin-right: auto; }}
.setting-text-right{{ font-size:14px; font-weight:600; color:#0f2446; margin-right: 10px; }}
.setting-item .arrow{{ color:#0f2446; font-weight:bold; font-size: 18px; }}

.bottom-row{{ margin-top:20px; display:flex; gap:10px; }}
.bottom-row .setting-item{{ flex:1; padding:12px 14px; justify-content: space-between; }}
.bottom-row .setting-text{{ flex:1; text-align:left; margin-left:15px; font-size:13px; font-weight:600; color:#0f2446; }}
.setting-item:hover{{ transform:translateY(-2px); box-shadow:0 6px 15px rgba(0,0,0,0.12); }}
</style>
</head>
<body>
<div class="main-wrapper">
    <div class="header-container"><h2 class="title">Settings</h2></div>

    <div class="setting-item" onclick="sendToStreamlit('Change_password')">
        <i class="fas fa-lock left-icon"></i>
        <span class="setting-text-right">Change Password</span>
        <span class="arrow">›</span>
    </div>

    <div class="setting-item" onclick="sendToStreamlit('Change_language')">
        <i class="fas fa-globe left-icon"></i>
        <span class="setting-text-right">Change Language</span>
        <span class="arrow">›</span>
    </div>

    <div class="setting-item" onclick="sendToStreamlit('logout')">
        <i class="fas fa-sign-out-alt left-icon"></i>
        <span class="setting-text-right">Log Out</span>
        <span class="arrow">›</span>
    </div>

    <div class="bottom-row">
        <div class="setting-item" onclick="sendToStreamlit('Report_Problem')">
            <i class="fas fa-exclamation-triangle"></i>
            <span class="setting-text">Report</span>
            <span class="arrow">›</span>
        </div>
        <div class="setting-item" onclick="sendToStreamlit('Contact_Us')">
            <i class="fas fa-envelope"></i>
            <span class="setting-text">Contact</span>
            <span class="arrow">›</span>
        </div>
    </div>
</div>

<script>
function sendToStreamlit(page) {{
    // This sends the page name to the iframe's parent (Streamlit)
    window.parent.postMessage({{
        type: 'streamlit:setComponentValue',
        value: page
    }}, '*');
}}
</script>
</body>
</html>
""", height=450)

# 6. Final Logic: Check if the component sent a value
if res:
    st.session_state.page = res
    st.rerun()
