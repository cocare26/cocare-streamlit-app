import streamlit as st

st.set_page_config(page_title="CoCare Settings", page_icon="⚙️")

st.title("⚙️ CoCare Settings")

# القائمة الجانبية
option = st.sidebar.radio("Settings Menu", [
    "Change Password",
    "Report a Problem",
    "Change Language",
    "Contact Us",
    "Rate App"
])

# 1️⃣ Change Password
if option == "Change Password":
    st.header("Change Password")
    old_pass = st.text_input("Old Password", type="password")
    new_pass = st.text_input("New Password", type="password")
    
    if st.button("Update Password"):
        if old_pass and new_pass:
            st.success("Password updated successfully ✅")
        else:
            st.warning("Please fill all fields ⚠️")

# 2️⃣ Report a Problem
elif option == "Report a Problem":
    st.header("Report a Problem")
    problem = st.text_area("Describe your problem")

    if st.button("Submit"):
        if problem:
            st.success("Problem sent successfully ✅")
        else:
            st.warning("Please write something ⚠️")

# 3️⃣ Change Language
elif option == "Change Language":
    st.header("Change Language")
    language = st.selectbox("Choose language", ["Arabic", "English"])
    st.success(f"Language changed to {language} 🌍")

# 4️⃣ Contact Us
elif option == "Contact Us":
    st.header("Contact Us")
    st.write("📧 Email: support@cocare.com")
    st.write("📞 Phone: 0790000000")

# 5️⃣ Rate App
elif option == "Rate App":
    st.header("Rate App")
    rating = st.slider("Rate us", 1, 5)

    if st.button("Submit Rating"):
        st.success(f"Thanks! You rated us {rating}/5 ⭐")
