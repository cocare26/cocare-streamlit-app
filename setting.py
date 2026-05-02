# --- الشاشة الرئيسية ---
if st.session_state.page == 'main':
    # كود HTML لعرض السهم < بجانب كلمة Settings
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: flex-start; margin-bottom: 20px;">
            <div style="cursor: pointer;">
                <span style="font-size: 30px; font-weight: bold; color: black; font-family: sans-serif;"><</span>
            </div>
            <div style="flex-grow: 1; text-align: center;">
                <h2 style="color: #4a4a4a; margin: 0; padding-right: 30px;">Settings</h2>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # باقي الأزرار كما هي
    if st.button("🔒 Change Password"): nav('password')
    if st.button("🌐 Change Language"): nav('language')
    if st.button("⭐ Rate App"): nav('rate')
    if st.button("🚪 Log Out"): st.write("Logged Out!")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report"): nav('report')
    with col2:
        if st.button("✉️ Contact"): nav('contact')
