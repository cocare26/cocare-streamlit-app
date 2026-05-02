import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #dceff7, #cce6ef, #e8f6fa);
}

.settings-box {
    width: 400px;
    margin: 0 auto;
    padding: 20px;
    background: rgba(160, 195, 195, 0.55);
    border-radius: 6px;
}

.header {
    position: relative;
    height: 40px;
    margin-bottom: 15px;
}

.back {
    position: absolute;
    left: 0;
    font-size: 30px;
    color: black;
}

.title {
    position: absolute;
    left: 90px;
    top: -5px;
    font-size: 28px;
    font-weight: 800;
    color: black;
}

.item {
    height: 55px;
    background: #f7f3e8;
    border-radius: 35px;
    margin: 12px 0;
    display: grid;
    grid-template-columns: 55px 1fr 25px;
    align-items: center;
    box-shadow: 
        0 4px 8px rgba(0,0,0,0.08),
        0 8px 20px rgba(0,0,0,0.10);
}

.icon {
    font-size: 24px;
    text-align: center;
}

.label {
    font-size: 18px;
    font-weight: 800;
    color: black;
    text-align: right;
    padding-right: 4px;
}

.arrow {
    font-size: 22px;
    color: white;
    text-align: center;
}

.bottom-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
    margin-top: 6px;
}

.small-item {
    height: 60px;
    background: #f7f3e8;
    border-radius: 35px;
    display: grid;
    grid-template-columns: 35px 1fr 20px;
    align-items: center;
    box-shadow: 
        0 4px 8px rgba(0,0,0,0.08),
        0 8px 20px rgba(0,0,0,0.10);
}

.small-label {
    font-size: 14px;
    font-weight: 800;
    color: black;
    text-align: left;
    line-height: 18px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="settings-box">

    <div class="header">
        <div class="back">‹</div>
        <div class="title">Settings</div>
    </div>

    <div class="item">
        <div class="icon">🔒</div>
        <div class="label">Change Password</div>
        <div class="arrow">›</div>
    </div>

    <div class="item">
        <div class="icon">🌐</div>
        <div class="label">Change Language</div>
        <div class="arrow">›</div>
    </div>

    <div class="item">
        <div class="icon">⭐</div>
        <div class="label">Rate App</div>
        <div class="arrow">›</div>
    </div>

    <div class="item">
        <div class="icon">🚪</div>
        <div class="label">Log Out</div>
        <div class="arrow">›</div>
    </div>

    <div class="bottom-row">
        <div class="small-item">
            <div class="icon">⚠️</div>
            <div class="small-label">Report a<br>Problem</div>
            <div class="arrow">›</div>
        </div>

        <div class="small-item">
            <div class="icon">✉️</div>
            <div class="small-label">Contact Us</div>
            <div class="arrow">›</div>
        </div>
    </div>

</div>
""", unsafe_allow_html=True)
