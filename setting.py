# 4. عرض الصفحة الرئيسية
if st.session_state.page == 'main':
    # الهيدر
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: flex-start; gap: 40px; margin-bottom: 50px; padding-left: 20px;">
            <span style="font-size: 40px; font-weight: 900; color: #0f2446; cursor: pointer;">‹</span>
            <h1 style="margin: 0; font-size: 38px;">Settings</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # دالة بناء الأزرار
    def make_btn(emoji, label, page, gap_size):
        gap = "&nbsp;" * gap_size 
        if st.button(f"{emoji} {gap} {label} &nbsp;&nbsp; ›"):
            nav(page)

    # --- تقليل المسافة في أول بوكسين (خليتها 40 بدل 80 عشان "يصغر" الفراغ) ---
    make_btn("🔒", "Change Password", "password", gap_size=40) 
    make_btn("🌐", "Change Language", "language", gap_size=40) 
    
    # --- إبقاء الريت واللوق طوال جداً بمسافة ضخمة (145) ---
    make_btn("⭐", "Rate App", "rate", gap_size=145)
    make_btn("🚪", "Log Out", "main", gap_size=145)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # السطر الأخير (Report & Contact)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report a Problem &nbsp; ›"): nav('report')
    with col2:
        if st.button("✉️ Contact Us &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ›"): nav('contact')
