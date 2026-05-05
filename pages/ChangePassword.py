import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Change Password", layout="centered")

st.markdown("""
<style>
* { margin:0; padding:0; box-sizing:border-box; direction:ltr; }

html, body, [data-testid="stAppViewContainer"] {
    background:#f0f7ff;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

#MainMenu, header, footer { visibility:hidden; }

.block-container {
    max-width:430px;
    margin:auto;
    padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
    min-height:600px;
}

.back-style .stButton > button {
    background:white !important;
    color:black !important;
    border-radius:50% !important;
    width:40px !important;
    height:40px !important;
    padding:0 !important;
    font-size:20px !important;
    box-shadow:0 4px 10px rgba(0,0,0,0.08) !important;
}

.title-text {
    font-size:20px;
    font-weight:900;
    color:#102646;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 8])

with col1:
    st.markdown('<div class="back-style">', unsafe_allow_html=True)
    if st.button("‹"):
        st.switch_page("pages/Settings.py")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="title-text">Change Password</div>', unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<style>
body {
    margin:0;
    font-family:'Segoe UI';
    background:transparent;
    display:flex;
    justify-content:center;
}

.main-wrapper {
    width:100%;
    max-width:380px;
    display:flex;
    flex-direction:column;
}

.input {
    background:white;
    border-radius:100px;
    padding:12px 18px;
    margin-bottom:15px;
    display:flex;
    align-items:center;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

.input:hover {
    transform: translateY(-5px);
}
.input i {
    margin-right:10px;
    color:#102646;
}

.input input {
    border:none;
    outline:none;
    flex:1;
}

.save {
    margin-top:20px;
}

.save button {
    width:100%;
    border-radius:100px;
    padding:16px;
    border:none;
    background:white;
    font-weight:900;
    cursor:pointer;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    transition: transform 0.25s ease;
}
.save button:hover {
    transform: translateY(-5px);
}
</style>
</head>

<body>

<div class="main-wrapper">

<div class="input">
    <i class="fas fa-lock"></i>
    <input type="password" id="old" placeholder="Current Password">
</div>

<div class="input">
    <i class="fas fa-lock"></i>
    <input type="password" id="new1" placeholder="New Password">
</div>

<div class="input">
    <i class="fas fa-lock"></i>
    <input type="password" id="new2" placeholder="Rewrite New Password">
</div>

<div class="save">
    <button onclick="save()">Save</button>
</div>

</div>

<script>
function save(){
    let oldPass = document.getElementById("old").value;
    let p1 = document.getElementById("new1").value;
    let p2 = document.getElementById("new2").value;

    if(oldPass === ""){
        alert("Enter current password");
        return;
    }

    if(p1 === "" || p2 === ""){
        alert("Enter new password");
        return;
    }

    if(p1 !== p2){
        alert("Passwords do not match");
        return;
    }

    alert("Password changed successfully ✅");
}
</script>

</body>
</html>
""", height=420)
