import streamlit as st
from engine import process_message

st.set_page_config(page_title="CoCare Chatbot", layout="centered")

st.title("🤖 CoCare Chatbot")

EN_RESPONSES = {
    "greeting": "Hello 👋 How can I help you?",
    "slow_internet": "It looks like your internet is slow. I’ll check the issue for you.",
    "no_signal": "It seems there may be a signal issue. I’ll report it for review.",
    "offer_inquiry": "Sure. You can check the available internet offers from the offers section.",
    "renew_package": "You can renew your package from the packages section.",
    "check_data_usage": "You can check your remaining internet usage from your dashboard.",
    "payment_issue": "It looks like there is a payment issue. Please check your payment details and try again.",
    "network_status": "I’ll check the current network status for your area.",
    "network_complaint": "Sorry for the inconvenience. Your network complaint will be reviewed.",
    "technical_support": "I’ll help you with the technical issue.",
    "feedback": "Thank you for your feedback.",
    "goodbye": "Goodbye 👋 We’re here whenever you need us.",
    "other": "Could you please provide more details?"
}

QUICK_REPLIES = {
    "Network Test": "Your network signal is strong.",
    "Internet Usage": "Your current internet usage is available in your dashboard.",
    "Renew Package": "You can renew your package from the packages section.",
    "International Calls": "International call options are available for your line.",
    "Offers & Games": "Current offers and games are available in the offers section.",
    "Contact Support": "Support team will contact you soon."
}

def fix_english_intent(text, detected_intent):
    t = text.lower().strip()

    if "hello" in t or "hi" == t or "hey" in t:
        return "greeting"

    if "bye" in t or "goodbye" in t or "see you" in t:
        return "goodbye"

    if "thank" in t or "thanks" in t:
        return "feedback"

    if "offer" in t or "offers" in t:
        return "offer_inquiry"

    if "how much internet" in t or "internet i have" in t or "internet left" in t or "data usage" in t or "usage" in t:
        return "check_data_usage"

    if "renew" in t or "package" in t:
        return "renew_package"

    if "slow" in t or "bad internet" in t or "weak internet" in t:
        return "slow_internet"

    if "no signal" in t or "signal" in t:
        return "no_signal"

    if "payment" in t or "paid" in t or "pay" in t:
        return "payment_issue"

    return detected_intent or "other"


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, how can I help you?"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

st.subheader("Quick Services")
cols = st.columns(2)

for i, key in enumerate(QUICK_REPLIES.keys()):
    with cols[i % 2]:
        if st.button(key):
            st.session_state.messages.append({"role": "user", "content": key})
            st.session_state.messages.append({"role": "assistant", "content": QUICK_REPLIES[key]})
            st.rerun()

prompt = st.chat_input("Type your question here...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        result = process_message(
            user_message=prompt,
            user_id="customer_1",
            region="Amman"
        )

        intent = fix_english_intent(prompt, result.get("intent", "other"))
        reply = EN_RESPONSES.get(intent, EN_RESPONSES["other"])

    except Exception as e:
        reply = "Sorry, something went wrong while analyzing your message."

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()
