import streamlit as st

st.set_page_config(layout="centered")

# 🎨 CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #dff4fb, #cfeef7);
}

.box {
    width: 360px;
    margin: 80px auto;
    padding: 25px;
    border-radius: 6px;
    background: rgba(170, 205, 205, 0.6);
    text-align: center;
}

.title {
    font-size: 26px;
    font-weight: bold;
    margin-bottom: 25px;
    color: #222;
    position: relative;
}

.back {
    position: absolute;
    left: 0;
    top: 0;
    font-size: 28px;
}

.pill {
    background: #f7f5ee;
    border-radius: 30px;
    padding: 14px;
    margin: 10px 0;
    font-weight: 600;
    color: #222;
    box-shadow: 0 3px 8px rgba(0,0,0,0.2);
    text-align: left;
}

.row {
    display: flex;
    gap: 10px;
}

.row .pill {
    flex: 1;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# 🟦 البوكس
st.markdown('<div class="box">', unsafe_allow_html=True)

st.markdown('<div class="title"><span class="back">←</span>Settings</div>', unsafe_allow_html=True)

st.markdown('<div class="pill">🔒   Change Password        ›</div>', unsafe_allow_html=True)
st.markdown('<div class="pill">🌐   Change Language        ›</div>', unsafe_allow_html=True)
st.markdown('<div class="pill">⭐   Rate App               ›</div>', unsafe_allow_html=True)
st.markdown('<div class="pill">🚪↗️  Log Out               ›</div>', unsafe_allow_html=True)

st.markdown('<div class="row">', unsafe_allow_html=True)
st.markdown('<div class="pill">⚠️ Report<br>a Problem</div>', unsafe_allow_html=True)
st.markdown('<div class="pill">✉️ Contact Us</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
