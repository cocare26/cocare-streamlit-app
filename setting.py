import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Settings", layout="centered")
st.markdown("<style>.block-container{max-width:350px !important;border-radius:42px;background:linear-gradient(160deg,#d6ecff 0%,#bfe3ff 45%,#eaf6ff 100%)} header,footer{visibility:hidden}</style>", unsafe_allow_html=True)

components.html("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<div style="width:290px;margin:auto;display:flex;flex-direction:column;height:480px;font-family:sans-serif">
    <div style="display:flex;align-items:center;justify-content:center;margin-bottom:35px;position:relative">
        <div onclick="window.top.location.href='/?page=logout'" style="position:absolute;left:0;font-size:28px;cursor:pointer">&lt;</div>
        <h2 style="color:#0f2446">Settings</h2>
    </div>
    <div onclick="window.top.location.href='/?page=change_password'" style="background:white;border-radius:100px;padding:14px;margin-bottom:15px;cursor:pointer;display:flex;align-items:center">
        <i class="fas fa-lock" style="color:#0f2446"></i><span style="flex:1;margin-left:15px;font-weight:600">Change Password</span><span>›</span>
    </div>
    <div onclick="window.top.location.href='/?page=change_language'" style="background:white;border-radius:100px;padding:14px;margin-bottom:15px;cursor:pointer;display:flex;align-items:center">
        <i class="fas fa-globe" style="color:#0f2446"></i><span style="flex:1;margin-left:15px;font-weight:600">Change Language</span><span>›</span>
    </div>
    <div onclick="window.top.location.href='/?page=rate_app'" style="background:white;border-radius:100px;padding:14px;margin-bottom:15px;cursor:pointer;display:flex;align-items:center">
        <i class="fas fa-star" style="color:#0f2446"></i><span style="flex:1;margin-left:15px;font-weight:600">Rate App</span><span>›</span>
    </div>
    <div onclick="window.top.location.href='/?page=logout'" style="background:white;border-radius:100px;padding:14px;cursor:pointer;display:flex;align-items:center">
        <i class="fas fa-sign-out-alt" style="color:#0f2446"></i><span style="flex:1;margin-left:15px;font-weight:600">Log Out</span><span>›</span>
    </div>
</div>
""", height=500 )
