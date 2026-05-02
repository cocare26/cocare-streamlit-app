# 4. عرض الصفحة الرئيسية
if st.session_state.page == 'main':
    # الهيدر المنسق
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: flex-start; gap: 40px; margin-bottom: 50px; padding-left: 20px;">
            <span style="font-size: 40px; font-weight: 900; color: #0f2446; cursor: pointer;">‹</span>
            <h1 style="margin: 0; font-size: 38px;">Settings</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # دالة بناء الأزرار العادية
    def make_btn(emoji, label, page, extra_gap=110):
        gap = "&nbsp;" * extra_gap 
        if st.button(f"{emoji} {gap} {label} &nbsp;&nbsp; ›"):
            nav(page)

    # الأزرار العادية
    make_btn("🔒", "Change Password", "password")
    make_btn("🌐", "Change Language", "language")
    
    # --- تعديل "الريت" و "اللوق" لزيادة الطول والمسافة بشكل أكبر ---
    # زدنا عدد المسافات لـ 140 لتدفع النص لأقصى زاوية اليمين
    make_btn("⭐", "Rate App", "rate", extra_gap=145)
    make_btn("🚪", "Log Out", "main", extra_gap=145)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # السطر الأخير
    col1, col2 = st.columns(2)
    with col1:
        # زر الريبورت مع سهم ممتد
        if st.button("⚠️ Report a Problem &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ›"): nav('report')
    with col2:
        # زر كونتاكت مع سهم ممتد
        if st.button("✉️ Contact Us &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ›"): nav('contact')
