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
    width: 390px;
    margin: 0 auto;
    padding: 22px 24px 30px 24px;
    background: rgba(160, 195, 195, 0.55);
    border-radius: 4px;
}

.header {
    position: relative;
    text-align: center;
    margin-bottom: 25px;
}

.back {
    position: absolute;
    left: 0;
    top: -4px;
    font-size: 34px;
    color: #222;
}

.title {
    font-size: 30px;
    font-weight: 800;
    color: #222;
}

.item {
    height: 58px;
    background: #f7f3e8;
    border-radius: 35px;
    margin: 17px 0;
    display: grid;
    grid-template-columns: 60px 1fr 25px;
    align-items: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.18);
}

.icon {
    font-size: 28px;
    text-align: center;
    opacity: 0.55;
}

.label {
    font-size: 21px;
    font-weight: 800;
    color: #222;
    text-align: right;
    padding-right: 12px;
}

.arrow {
    font-size: 24px;
    opacity: 0.35;
    color: #222;
}

.bottom-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
    margin-top: 18px;
}

.small-item {
    height: 66px;
    background: #f7f3e8;
    border-radius: 35px;
    display: grid;
    grid-template-columns: 45px 1fr 18px;
    align-items: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.18);
}

.small-label {
    font-size: 18px;
    font-weight: 800;
    color: #222;
    line-height: 21px;
    text-align: right;
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
        <div class="arrow"></div>
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
