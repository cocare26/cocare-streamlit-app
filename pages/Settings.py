# ===== الأزرار =====

# 1. هدول خليهم زي ما هم (مسافة عادية)
if st.button("🔒&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Change Password"):
    st.switch_page("pages/ChangePassword.py")

if st.button("🌐&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Change Language"):
    st.switch_page("pages/ChangeLanguage.py")


# 2. هدول زدنا فيهم المسافة (&nbsp;) بشكل كبير عشان يندفع النص لليمين
# زدنا عدد الفراغات هون بس عشان يلحقوا النصوص اللي فوق
if st.button("⭐&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rate App"):
    st.switch_page("pages/RateApp.py")

if st.button("🚪&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Log Out"):
     st.session_state.clear()
     st.switch_page("app.py")
