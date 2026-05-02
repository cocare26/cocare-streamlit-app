import streamlit as st

st.set_page_config(layout="centered")

# CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #dff4fb, #cfeef7);
}

.box {
    width: 350px;
    margin: auto;
    padding: 25px;
    border-radius: 12px;
    background: rgba(180, 210, 210, 0.5);
    text-align: center;
}

.title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 20px;
}

.btn {
    background: #f7f6ee;
    border-radius: 25px;
    padding: 10px;
    margin: 8px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 500;
    box-shadow: 0 2px 5px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# التصميم
st.markdown('<div class="box">', unsafe_allow_html=True)

st.markdown('<div class="title">‹ Settings</div>', unsafe_allow_html=True)

st.markdown('<div class="btn">🔒 Change Password</div>', unsafe_allow_html=True)
st.markdown('<div class="btn">🌐 Change Language</div>', unsafe_allow_html=True)
st.markdown('<div class="btn">⭐ Rate App</div>', unsafe_allow_html=True)
st.markdown('<div class="btn">↩️ Log Out</div>', unsafe_allow_html=True)

st.markdown('<div style="display:flex; gap:10px;">', unsafe_allow_html=True)
st.markdown('<div class="btn" style="flex:1;">⚠️ Report a Problem</div>', unsafe_allow_html=True)
st.markdown('<div class="btn" style="flex:1;">✉️ Contact Us</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st

st.set_page_config(layout="centered")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #dff4fb, #cfeef7);
}

/* العنوان */
.title {
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 25px;
}

/* البوكسات */
.input-box {
    background: #f7f6ee;
    border-radius: 25px;
    padding: 10px 15px;
    margin: 10px auto;
    width: 300px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.15);
}

/* زر الحفظ */
.save-btn {
    background: #f7f6ee;
    border-radius: 25px;
    padding: 12px;
    width: 200px;
    text-align: center;
    margin: 30px auto;
    font-weight: bold;
    box-shadow: 0 3px 8px rgba(0,0,0,0.2);
}

/* إزالة شكل Streamlit الافتراضي */
input {
    border: none !important;
    outline: none !important;
    background: transparent !important;
}
</style>
""", unsafe_allow_html=True)

# العنوان
st.markdown('<div class="title">← Change Password</div>', unsafe_allow_html=True)

# البوكسات
st.markdown('<div class="input-box">🔒 Current Password</div>', unsafe_allow_html=True)
st.markdown('<div class="input-box">🔒 New Password</div>', unsafe_allow_html=True)
st.markdown('<div class="input-box">🔒 Re-write New Password</div>', unsafe_allow_html=True)

# زر الحفظ
st.markdown('<div class="save-btn">Save</div>', unsafe_allow_html=True)



.stApp {
    background: linear-gradient(135deg, #dff4fb, #cfeef7);
} 


elif st.session_state.page == "language":

    st.markdown("""
    <style>
    .lang-page {
        width: 360px;
        margin: auto;
        padding-top: 20px;
        text-align: center;
    }

    .lang-title {
        font-size: 15px;
        font-weight: 600;
        color: #222;
        margin-bottom: 25px;
    }

    .lang-pill {
        width: 270px;
        height: 36px;
        margin: 10px auto;
        background: #f7f5ee;
        border-radius: 25px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.18);
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 14px;
        font-size: 12px;
        color: #222;
        font-weight: 600;
    }

    .icon {
        margin-right: 6px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="lang-page">', unsafe_allow_html=True)

    # زر الرجوع
    if st.button("←"):
        st.session_state.page = "settings"

    st.markdown('<div class="lang-title">Change Language</div>', unsafe_allow_html=True)

    # English
    st.markdown(
        '<div class="lang-pill">🌐 English ✔️</div>',
        unsafe_allow_html=True
    )

    # Arabic
    st.markdown(
        '<div class="lang-pill">🌐 العربية ›</div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


if st.button("⭐ Rate App"):
    st.session_state.page = "rate"


elif st.session_state.page == "rate":

    st.markdown("""
    <style>
    .rate-page {
        width: 360px;
        margin: auto;
        padding-top: 20px;
        text-align: center;
    }

    .rate-title {
        font-size: 15px;
        font-weight: 600;
        color: #222;
        margin-bottom: 25px;
    }

    .rate-pill {
        width: 280px;
        height: 36px;
        margin: 10px auto;
        background: #f7f5ee;
        border-radius: 25px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.18);
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 14px;
        font-size: 12px;
        color: #222;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="rate-page">', unsafe_allow_html=True)

    # زر رجوع
    if st.button("←"):
        st.session_state.page = "settings"

    st.markdown('<div class="rate-title">Rate App</div>', unsafe_allow_html=True)

    # Google Play
    st.markdown(
        '<div class="rate-pill">▶️ Google Play Store ›</div>',
        unsafe_allow_html=True
    )

    # Apple Store
    st.markdown(
        '<div class="rate-pill"> Apple App Store ›</div>',
        unsafe_allow_html=True
    )

    # Huawei
    st.markdown(
        '<div class="rate-pill">🛍️ Huawei AppGallery ›</div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


if st.button("🚪 Log Out"):
    st.session_state.page = "logout"

elif st.session_state.page == "logout":

    st.markdown("""
    <style>
    .logout-box {
        width: 400px;
        margin: 120px auto;
        padding: 30px;
        background: rgba(170, 205, 205, 0.6);
        border-radius: 10px;
        text-align: center;
    }

    .logout-title {
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 20px;
    }

    .btn {
        background: #f7f5ee;
        border-radius: 25px;
        padding: 10px;
        margin: 10px auto;
        width: 150px;
        font-weight: bold;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="logout-box">', unsafe_allow_html=True)

    st.markdown('<div class="logout-title">Are you sure you want to log out?</div>', unsafe_allow_html=True)

    if st.button("Yes"):
        st.success("Logged out successfully")

    if st.button("Cancel"):
        st.session_state.page = "settings"

    st.markdown('</div>', unsafe_allow_html=True)


if st.button("⚠️ Report a Problem"):
    st.session_state.page = "report" 

elif st.session_state.page == "report":

    st.markdown("""
    <style>
    .report-page {
        width: 360px;
        margin: auto;
        padding-top: 20px;
        text-align: center;
    }

    .report-box {
        background: rgba(170, 205, 205, 0.6);
        padding: 25px;
        border-radius: 4px;
    }

    .title-row {
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 20px;
        color: #222;
        position: relative;
    }

    .input-area {
        width: 100%;
        height: 90px;
        background: #f7f5ee;
        border-radius: 25px;
        padding: 15px;
        text-align: left;
        font-size: 12px;
        color: #444;
        box-shadow: 0 2px 6px rgba(0,0,0,0.2);
    }

    .send-btn {
        margin-top: 40px;
        height: 36px;
        background: #f7f5ee;
        border-radius: 25px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 600;
        box-shadow: 0 3px 7px rgba(0,0,0,0.2);
    }

    .arrow {
        position: absolute;
        left: 0;
        top: 0;
        font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="report-page">', unsafe_allow_html=True)

    if st.button("←"):
        st.session_state.page = "settings"

    st.markdown('<div class="report-box">', unsafe_allow_html=True)

    st.markdown('<div class="title-row">Report a Problem</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-area">I need help</div>', unsafe_allow_html=True)

    st.markdown('<div class="send-btn">✈️ Send Report</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)



if st.button("✉️ Contact Us"):
    st.session_state.page = "contact"

elif st.session_state.page == "contact":

    st.markdown("""
    <style>
    .contact-page {
        width: 360px;
        margin: auto;
        padding-top: 20px;
        text-align: center;
    }

    .contact-box {
        background: rgba(170, 205, 205, 0.6);
        padding: 25px;
        border-radius: 4px;
    }

    .title-row {
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 20px;
        color: #222;
    }

    .pill {
        width: 100%;
        height: 38px;
        margin: 10px auto;
        background: #f7f5ee;
        border-radius: 25px;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        padding: 0 14px;
        font-size: 12px;
        color: #333;
        font-weight: 600;
        box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        gap: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="contact-page">', unsafe_allow_html=True)

    # زر الرجوع
    if st.button("←"):
        st.session_state.page = "settings"

    st.markdown('<div class="contact-box">', unsafe_allow_html=True)

    st.markdown('<div class="title-row">Contact Us</div>', unsafe_allow_html=True)

    st.markdown('<div class="pill">✉️ Email: Co.Care26@gmail.com</div>', unsafe_allow_html=True)
    st.markdown('<div class="pill">📞 Phone: +962 79 123 4567</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)




