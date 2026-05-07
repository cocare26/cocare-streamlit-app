import streamlit as st

# اجعلي الكود يبدأ مباشرة هكذا دون وضعه داخل def
st.title("🔔 Notifications")
st.write("Stay updated with our latest offers.")

if st.button("Back to Home"):
    # إذا كنتِ تستخدمين نظام الصفحات المتعددة (st.switch_page)
    # فاسم الملف الرئيسي غالباً هو app.py أو Customer_Dashboard.py
    st.switch_page("2_Customer.py")
