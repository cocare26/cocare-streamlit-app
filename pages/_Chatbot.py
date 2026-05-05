import streamlit as st
from engine import process_message

st.set_page_config(page_title="CoCare Chatbot", layout="centered")

st.title("🤖 CoCare Chatbot")

EN_RESPONSES = {
    "greeting": "Hello 👋 How can I help you?",
    "slow_internet": "It looks like your internet is slow. I’ll check the issue.",
    "no_signal": "It seems there may be a signal issue.",
    "offer_inquiry": "Sure. You can check available internet offers from the offers section.",
    "renew_package": "You can renew your package from the packages section.",
    "check_data_usage": "You can check your internet usage from your dashboard.",
    "payment_issue": "It looks like there is a payment issue. Please check your payment details and try again.",
    "network_status": "I’ll check the current network status for you.",
    "network_complaint": "Sorry for the inconvenience. Your network complaint will be reviewed.",
    "technical_support": "I’ll help you with the technical issue.",
    "feedback": "Thank you for your feedback.",
    "goodbye": "Goodbye 👋 We’re here whenever you need us.",
    "other": "Could you please provide more details?"
}

def manual_intent_fix(text, detected_intent):
    t = text.lower()

    if "offer" in t or "offers" in t or "عروض" in t or "عرض" in t:
        return "offer_inquiry"

    if "internet usage" in t or "استهلاك" in t or "بيانات" in t:
        return "check_data_usage"

    if "renew" in t or "تجديد" in t or "اجدد" in t:
        return "renew_package"

    if "slow" in t or "بطي" in t or "ضعيف" in t or "ضعيفة" in t:
        return "slow_internet"

    return detected_intent


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, how can I help you?"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Type your question here...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        result = process_message(
            user_message=prompt,
            user_id="customer_1",
            region="Amman"
        )

        intent = manual_intent_fix(prompt, result.get("intent", "other"))
        reply = EN_RESPONSES.get(intent, EN_RESPONSES["other"])

        st.session_state.messages.append({
            "role": "assistant",
            "content": reply
        })

    except Exception as e:
        st.session_state.messages.append({
            "role": "assistant",
            "content": "Sorry, something went wrong while analyzing your message."
        })

    st.rerun()
