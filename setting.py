import streamlit as st

st.set_page_config(page_title="Settings", layout="wide")

st.write("")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #dceff7, #cce6ef, #e8f6fa);
}

.settings-box {
    width: 400px;
    margin: 0 auto;
    padding: 22px;
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
    font-size: 34px;
    color: #000;
}

.title {
    position: absolute;
    left: 85px;  /* زحلقناه شوي لليمين */
    font-size: 28px;
    font-weight: 600; /* أخف */
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
}

.icon {
    font-size: 26px;
    text-align: center;
}

.label {
    font-size: 17px;   /* أصغر */
    font-weight: 600;  /* أنحف */
    text-align: right;
    color: #000;
}

.arrow {
    color: #fff;
    text-align: center;
    font-size: 24px;
}

.bottom-row {
    display: flex;
    gap: 5px;
}

.small-item {
    flex: 1;
    background: #f7f3e8;
    border-radius: 35px;
    padding: 10px;
    display: flex; /* بدل grid */
    align-items: center;
    gap: 6px; /* مسافة بسيطة بعد الإيموجي */
}

.small-item .arrow {
    margin-left: auto; /* يخلي السهم أقصى اليمين */
}

.small-item .label {
    text-align: left; /* يخلي النص جنب الإيموجي */
    font-size: 15px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

with st.container():
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
                <div class="label">Report a<br>Problem</div>
                <div class="arrow">›</div>
            </div>

            <div class="small-item">
                <div class="icon">✉️</div>
                <div class="label">Contact Us</div>
                <div class="arrow">›</div>
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)
