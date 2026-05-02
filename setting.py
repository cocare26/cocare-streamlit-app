import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #dff4fb 0%, #cfeef7 50%, #e8f7fb 100%);
}

.block-container {
    padding-top: 45px;
}

.settings-box {
    width: 430px;
    margin: 0 auto;
    padding: 28px 28px 34px 28px;
    background: rgba(165, 200, 200, 0.55);
    text-align: center;
}

.header {
    position: relative;
    height: 50px;
    margin-bottom: 18px;
}

.back {
    position: absolute;
    left: 0;
    top: 2px;
    font-size: 38px;
    color: #222;
    font-weight: 400;
}

.title {
    font-size: 30px;
    font-weight: 800;
    color: #222;
    line-height: 50px;
}

.item {
    height: 58px;
    background: #f7f3e8;
    border-radius: 35px;
    margin: 16px 0;
    display: grid;
    grid-template-columns: 58px 1fr 25px;
    align-items: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.18);
    color: #222;
}

.icon {
    font-size: 28px;
    opacity: 0.55;
    text-align: center;
}

.label {
    font-size: 21px;
    font-weight: 800;
    text-align: center;
}

.arrow {
    font-size: 24px;
    opacity: 0.35;
    padding-right: 8px;
}

.bottom-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
    margin-top: 18px;
}

.small-item {
    height: 68px;
    background: #f7f3e8;
    border-radius: 35px;
    display: grid;
    grid-template-columns: 45px 1fr 18px;
    align-items: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.18);
    color: #222;
}

.small-label {
    font-size: 19px;
    font-weight: 800;
    line-height: 22px;
    text-align: center;
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
        <div class="icon">🚪↗️</div>
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
