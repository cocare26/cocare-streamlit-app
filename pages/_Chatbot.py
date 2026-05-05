import streamlit as st
from engine import process_message

st.set_page_config(page_title="Chatbot", layout="centered")

st.title("🤖 CoCare Chatbot")

# حفظ المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["text"])
    else:
        st.chat_message("assistant").write(msg["text"])

# إدخال المستخدم
user_input = st.chat_input("اكتب رسالتك هنا...")

if user_input:
    # عرض رسالة المستخدم
    st.session_state.messages.append({"role": "user", "text": user_input})
    st.chat_message("user").write(user_input)

    # تحليل الرسالة
    result = process_message(
        user_message=user_input,
        user_id="customer_1",
        region="Amman"
    )

    bot_reply = result.get("response", "")
    follow = result.get("followup_response", "")

    full_reply = bot_reply + ("\n\n" + follow if follow else "")

    # عرض رد البوت
    st.session_state.messages.append({"role": "bot", "text": full_reply})
    st.chat_message("assistant").write(full_reply)
