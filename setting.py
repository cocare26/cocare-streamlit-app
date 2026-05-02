import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Settings", layout="centered")

html = """
<style>
body {
    background: linear-gradient(135deg, #dceff7, #cce6ef, #e8f6fa);
    font-family: Arial;
}

.settings-box {
    width: 400px;
    margin: 0 auto;
    padding: 22px;
    background: rgba(160, 195, 195, 0.55);
}

.header {
    position: relative;
    height: 48px;
    margin-bottom: 18px;
}

.back {
    position: absolute;
    left: 0;
    font-size: 34px;
    color: black;
}

.title {
    position: absolute;
    left: 72px;
    font-size: 30px;
    font-weight: 800;
    color: black;
}

.item {
    height: 58px;
    background: #f7f3e8;
    border-radius: 35px;
    margin: 13px 0;
    display: grid;
    grid-template-columns: 58px 1fr 25px;
    align-items: center;
}

.icon {
    font-size: 27px;
    text-align: center;
}

.label {
    font-size: 21px;
    font-weight: 800;
    color: black;
    text-align: right;
}

.arrow {
    color: white;
    text-align: center;
    font-size: 24px;
}

.bottom-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 5px;
}

.small-item {
    height: 62px;
    background: #f7f3e8;
    border-radius: 35px;
    display: grid;
    grid-template-columns: 42px 1fr 18px;
    align-items: center;
}

.small-label {
    font-size: 16px;
    font-weight: 800;
    color: black;
    text-align: right;
}
</style>

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
"""

components.html(html, height=600)
