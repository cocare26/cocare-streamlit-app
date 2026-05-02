# 4. عرض الصفحة الرئيسية
if st.session_state.page == 'main':
    # الهيدر
    st.markdown("""
        <div style="display: flex; align-items: center; gap: 40px; margin-bottom: 50px; padding-left: 20px;">
            <span style="font-size: 40px; font-weight: 900; color: #0f2446;">‹</span>
            <h1 style="margin: 0; font-size: 38px; color: #0f2446;">Settings</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # دالة الأزرار
    def make_btn(emoji, label, page, gap_size):
        gap = "&nbsp;" * gap_size 
        if st.button(f"{emoji} {gap} {label} &nbsp;&nbsp; ›"):
            nav(page)

    # --- تم توحيد الطول للجميع (كلهم 145) ليكونوا بنفس امتداد لوق أوت ---
    make_btn("🔒", "Change Password", "password", gap_size=145) 
    make_btn("🌐", "Change Language", "language", gap_size=145) 
    make_btn("⭐", "Rate App", "rate", gap_size=145)
    make_btn("🚪", "Log Out", "main", gap_size=145)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # السطر الأخير (Report & Contact)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report a Problem &nbsp; ›"): nav('report')
    with col2:
        if st.button("✉️ Contact Us &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ›"): nav('contact')
