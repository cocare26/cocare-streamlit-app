import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #dceff7, #cce6ef, #e8f6fa);
}

.block-container {
    padding-top: 15px;
}

.settings-box {
    width: 400px;
    margin: 0 auto;
    padding: 22px 22px 28px 22px;
    background: rgba(160, 195, 195, 0.55);
    border-radius: 6px;
}

.header {
    position: relative;
    height: 48px;
    margin-bottom: 18px;
}

.back {
    position: absolute;
    left: 0;
    top: -3px;
    font-size: 34px;
    color: #000;
    font-weight: 700;
}

.title {
    position: absolute;
    left: 72px;
    top: 4px;
    font-size: 30px;
    font-weight: 800;
    color: #000;
}

.item {
    height: 58px;
    background: #f7f3e8;
    border-radius: 35px;
    margin: 13px 0;
    display: grid;
    grid-template-columns: 58px 1fr 25px;
    align-items: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.18);
}

.icon {
    font-size: 27px;
    text-align: center;
    opacity: 0.55;
}

.label {
    font-size: 21px;
    font-weight: 800;
    color: #000;
    text-align: right;
    padding-right: 2px;
}

.rate-label {
    padding-right: 38px;
}

.logout-label {
    padding-right: 42px;
}

.arrow {
    font-size: 25px;
    color: #ffffff;
    font-weight: 900;
    text-align: center;
}

.bottom-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4px;
    margin-top: 8px;
}

.small-item {
    height: 62px;
    background: #f7f3e8;
    border-radius: 35px;
    display: grid;
    grid-template-columns: 42px 1fr 18px;
    align-items: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.18);
}

.small-label {
    font-size: 16px;
    font-weight: 800;
    color: #000;
    line-height: 20px;
    text-align: right;
    padding-right: 2px;
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
        <div class="label rate-label">Rate App</div>
        <div class="arrow">›</div>
    </div>

    <div class="item">
        <div class="icon">🚪</div>
        <div class="label logout-label">Log Out</div>
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
