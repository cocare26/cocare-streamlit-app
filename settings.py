 import streamlit as st

st.set_page_config(layout="centered")

# أول مرة فقط
if "page" not in st.session_state:
    st.session_state.page = "settings"

# 🎨 الخلفية + الشكل
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #dff4fb, #cfeef7);
}

.box {
    width: 360px;
    margin: 50px auto;
    padding: 25px;
    border-radius: 6px;
    background: rgba(170, 205, 205, 0.6);
    text-align: center;
}

.title {
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 20px;
}

.pill {
    background: #f7f5ee;
    border-radius: 25px;
    padding: 12px;
    margin: 10px 0;
    font-weight: 600;
    box-shadow: 0 2px 6px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# ======================
# 🟢 الصفحة الرئيسية
# ======================
if st.session_state.page == "settings":

    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<div class="title">‹ Settings</div>', unsafe_allow_html=True)

    if st.button("🔒 Change Password"):
        st.session_state.page = "password"

    if st.button("🌐 Change Language"):
        st.session_state.page = "language"

    if st.button("⭐ Rate App"):
        st.session_state.page = "rate"

    if st.button("🚪 Log Out"):
        st.session_state.page = "logout"

    if st.button("⚠️ Report a Problem"):
        st.session_state.page = "report"

    if st.button("✉️ Contact Us"):
        st.session_state.page = "contact"

    st.markdown('</div>', unsafe_allow_html=True)

# ======================
# 🔒 Password
# ======================
elif st.session_state.page == "password":

    if st.button("←"):
        st.session_state.page = "settings"

    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<div class="title">Change Password</div>', unsafe_allow_html=True)

    st.markdown('<div class="pill">🔒 Current Password</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">🔒 New Password</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">🔒 Re-write Password</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">Save</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ======================
# 🌐 Language
# ======================
elif st.session_state.page == "language":

    if st.button("←"):
        st.session_state.page = "settings"

    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<div class="title">Change Language</div>', unsafe_allow_html=True)

    st.markdown('<div class="pill">🌐 English ✔️</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">🌐 العربية ›</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ======================
# ⭐ Rate
# ======================
elif st.session_state.page == "rate":

    if st.button("←"):
        st.session_state.page = "settings"

    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<div class="title">Rate App</div>', unsafe_allow_html=True)

    st.markdown('<div class="pill">▶️ Google Play Store</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill"> Apple Store</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">🛍️ Huawei AppGallery</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ======================
# ⚠️ Report
# ======================
elif st.session_state.page == "report":

    if st.button("←"):
        st.session_state.page = "settings"

    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<div class="title">Report a Problem</div>', unsafe_allow_html=True)

    st.markdown('<div class="pill">I need help</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">✈️ Send Report</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ======================
# ✉️ Contact
# ======================
elif st.session_state.page == "contact":

    if st.button("←"):
        st.session_state.page = "settings"

    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<div class="title">Contact Us</div>', unsafe_allow_html=True)

    st.markdown('<div class="pill">✉️ Email: Co.Care26@gmail.com</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">📞 Phone: +962 79 123 4567</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ======================
# 🚪 Logout
# ======================
elif st.session_state.page == "logout":

    if st.button("←"):
        st.session_state.page = "settings"

    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<div class="title">Logged Out</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">You have logged out</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
[5:36 PM, 5/2/2026] ‏🤍: import streamlit as st

st.set_page_config(layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "settings"

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #dff4fb, #cfeef7);
}

.box {
    width: 360px;
    margin: 50px auto;
    padding: 25px;
    border-radius: 6px;
    background: rgba(170, 205, 205, 0.6);
    text-align: center;
}

.title {
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 20px;
}

.pill {
    background: #f7f5ee;
    border-radius: 25px;
    padding: 12px;
    margin: 10px 0;
    font-weight: 600;
    box-shadow: 0 2px 6px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

if st.session_state.page == "settings":

    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<div class="title">‹ Settings</div>', unsafe_allow_html=True)

    if st.button("🔒 Change Password"):
        st.session_state.page = "password"

    if st.button("🌐 Change Language"):
        st.session_state.page = "language"

    if st.button("⭐ Rate App"):
        st.session_state.page = "rate"

    if st.button("🚪 Log Out"):
        st.session_state.page = "logout"

    if st.button("⚠️ Report a Problem"):
        st.session_state.page = "report"

    if st.button("✉️ Contact Us"):
        st.session_state.page = "contact"

    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "password":

    if st.button("← Back"):
        st.session_state.page = "settings"

    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<div class="title">Change Password</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">🔒 Current Password</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">🔒 New Password</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">🔒 Re-write Password</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">Save</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "language":

    if st.button("← Back"):
        st.session_state.page = "settings"

    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<div class="title">Change Language</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">🌐 English ✔️</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">🌐 العربية ›</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "rate":

    if st.button("← Back"):
        st.session_state.page = "settings"

    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<div class="title">Rate App</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">▶️ Google Play Store</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill"> Apple Store</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">🛍️ Huawei AppGallery</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "logout":

    if st.button("← Back"):
        st.session_state.page = "settings"

    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<div class="title">Logged Out</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">You have logged out</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "report":

    if st.button("← Back"):
        st.session_state.page = "settings"

    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<div class="title">Report a Problem</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">I need help</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">✈️ Send Report</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "contact":

    if st.button("← Back"):
        st.session_state.page = "settings"

    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<div class="title">Contact Us</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">✉️ Email: Co.Care26@gmail.com</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">📞 Phone: +962 79 123 4567</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
