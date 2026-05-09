import streamlit as st
import base64
import os
import sys
import html as html_lib
import urllib.parse

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cocare import process_message

st.set_page_config(page_title="AI Agent", layout="centered")

PHONE_WIDTH = 390
PHONE_HEIGHT = 820

CHAT_KEY = "chat_en_messages"
CONTEXT_KEY = "chat_en_context"

if "region" not in st.session_state:
    st.session_state["region"] = "Amman"

if CONTEXT_KEY not in st.session_state:
    st.session_state[CONTEXT_KEY] = {
        "last_intent": None,
        "awaiting_details": False,
        "last_network_problem": False
    }


def reset_context():
    st.session_state[CONTEXT_KEY] = {
        "last_intent": None,
        "awaiting_details": False,
        "last_network_problem": False
    }


if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = [
        ("bot", "Hi 👋 I am CoCare AI Assistant. How can I help you?")
    ]


def img_to_base64(path):
    try:
        full_path = os.path.join(os.path.dirname(__file__), "..", path)
        if os.path.exists(full_path):
            with open(full_path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    except Exception:
        pass
    return ""


robot = img_to_base64("robot_head.png") or img_to_base64("robot.png")


def is_thanks_or_close(text):
    t = str(text).strip().lower()
    return any(p in t for p in [
        "thanks", "thank you", "ok", "okay", "fine", "great", "done",
        "شكرا", "شكراً", "تمام"
    ])


def is_goodbye(text):
    t = str(text).strip().lower()
    return any(p in t for p in ["bye", "goodbye", "see you", "مع السلامة", "باي"])


def is_no_problem(text):
    t = str(text).strip().lower()
    return any(p in t for p in [
        "no problem", "i have no problem", "nothing", "no issue",
        "not now", "never mind"
    ])


def is_social_positive(text):
    t = str(text).strip().lower()
    return any(p in t for p in [
        "nice", "good", "great", "perfect", "excellent", "awesome"
    ])


def is_short_followup(text):
    return len(str(text).strip().split()) <= 8


def looks_like_time_answer(text):
    t = str(text).lower()
    return any(w in t for w in [
        "hour", "hours", "minute", "minutes", "today", "yesterday",
        "morning", "evening", "week", "since", "ago"
    ])


def looks_like_yes(text):
    return str(text).strip().lower() in ["yes", "yeah", "yep", "ok", "okay", "sure"]


def looks_like_no(text):
    return str(text).strip().lower() in ["no", "nope", "not"]


def looks_like_location(text):
    t = str(text).strip().lower()
    locations = [
        "amman", "zarqa", "irbid", "balqa", "madaba", "karak",
        "tafilah", "maan", "aqaba", "jerash", "ajloun", "mafraq"
    ]
    return any(loc in t for loc in locations)


def human_fallback_reply(text):
    t = str(text).strip().lower()

    if is_no_problem(t):
        reset_context()
        return "Alright. If you need any help later, I am here."

    if is_thanks_or_close(t):
        reset_context()
        return "You are welcome. I am here whenever you need help."

    if is_goodbye(t):
        reset_context()
        return "Goodbye 👋 I am here whenever you need help."

    if is_social_positive(t):
        reset_context()
        return "Glad to help. I am here whenever you need support."

    if "international" in t or "calls" in t:
        return "International calls are available depending on your line type. Do you want prices or activation steps?"

    if "usage" in t or "data" in t or "remaining internet" in t:
        return "You can check your internet usage from the account or usage section in the app."

    if "renew" in t or "package" in t:
        return "You can renew your package from the packages section in the app."

    if "offer" in t or "offers" in t:
        return "Current offers are available in the offers section. Do you want internet offers or call offers?"

    if any(w in t for w in ["who are you", "what are you", "what do you do"]):
        return (
            "I am CoCare AI Assistant 🤖\n\n"
            "I can help with network issues, packages, internet usage, offers, international calls, and technical support."
        )

    if any(w in t for w in ["help", "help me", "i need help"]):
        return (
            "Sure. Tell me your question or the problem you are facing, "
            "and I will guide you to the right service."
        )

    if any(w in t for w in ["how", "steps", "method"]):
        return "Tell me which service you want to use, and I will explain the steps clearly."

    if any(w in t for w in ["where", "location", "place"]):
        return "Please clarify what location you mean. If you mean a service inside the app, tell me its name."

    return (
        "I understand. To help you better, please clarify whether your request is about "
        "network, packages, app services, or another service."
    )


def handle_context_followup(text):
    context = st.session_state[CONTEXT_KEY]
    msg = str(text).strip()
    t = msg.lower()

    if not context.get("awaiting_details"):
        return None

    if any(p in t for p in [
        "renew", "package", "usage", "data", "offer", "offers",
        "international", "calls", "support", "help", "network test"
    ]):
        reset_context()
        return None

    if is_no_problem(msg):
        reset_context()
        return "Alright. I will not record an issue. If you need help later, I am here."

    if is_thanks_or_close(msg):
        reset_context()
        return "You are welcome. I am here whenever you need help."

    if not is_short_followup(msg):
        return None

    reset_context()

    if looks_like_time_answer(msg):
        return "Got it. I recorded the time or duration of the issue. The network status will be followed up by the technical team."

    if looks_like_location(msg):
        return "Got it. I received your area. I will add it to the issue details for the technical team."

    if looks_like_yes(msg):
        return "Okay. Try restarting the router or enabling airplane mode for 10 seconds, then tell me if the connection improves."

    if looks_like_no(msg):
        return "Okay. I will record the issue without extra steps. If it continues, the technical team will follow up."

    return "Got it. I received the details and will add them to the recorded issue."


def direct_service_reply(text):
    t = str(text).strip().lower()
    region = st.session_state.get("region", "Amman")

    if t == "network test":
        reset_context()
        return f"I can help you check the network status in {region}.\n\nAre you facing slow internet, disconnection, or weak signal?"

    if t == "internet usage":
        reset_context()
        return "You can check your internet usage from the account or usage section in the app."

    if t == "renew package":
        reset_context()
        return "You can renew your package from the packages section in the app. Do you want the renewal steps?"

    if t == "international calls":
        reset_context()
        return "International calls are available depending on your line type. Do you want prices or activation steps?"

    if t == "offers & games":
        reset_context()
        return "Current offers are available in the offers section. Do you want internet offers or call offers?"

    if t == "contact support":
        reset_context()
        return "Sure. Tell me the technical issue details and I will help you step by step."

    return None


def get_bot_reply(user_text):
    msg = str(user_text).strip()
    analysis_result = {}

    if is_no_problem(msg):
        reset_context()
        return "Alright. If you need any help later, I am here.", analysis_result

    if is_thanks_or_close(msg):
        reset_context()
        return "You are welcome. I am here whenever you need help.", analysis_result

    if is_goodbye(msg):
        reset_context()
        return "Goodbye 👋 I am here whenever you need help.", analysis_result

    if is_social_positive(msg):
        reset_context()
        return "Glad to help. I am here whenever you need support.", analysis_result

    service_reply = direct_service_reply(msg)
    if service_reply:
        return service_reply, analysis_result

    context_reply = handle_context_followup(msg)
    if context_reply:
        return context_reply, analysis_result

    user_id = st.session_state.get("user_id", "customer_1")
    region = st.session_state.get("region", "Amman")

    try:
        result = process_message(msg, user_id=user_id, region=region)
        analysis_result = result

        intent = result.get("intent", "")
        network_problem = result.get("network_problem", False)

        st.session_state[CONTEXT_KEY]["last_intent"] = intent
        st.session_state[CONTEXT_KEY]["last_network_problem"] = network_problem
        st.session_state[CONTEXT_KEY]["awaiting_details"] = bool(network_problem)

        if intent in ["clarification", "unknown", "other", "fallback"]:
            if len(msg.split()) > 4:
                return "I understand. To help you better, please tell me whether this is about network, package, app, or another service.", analysis_result

            reset_context()
            return human_fallback_reply(msg), analysis_result

        response = str(result.get("response", "")).strip()
        followup = str(result.get("followup_response", "")).strip()
        reply = f"{response}\n\n{followup}".strip()

        if not reply:
            return human_fallback_reply(msg), analysis_result

        return reply, analysis_result

    except Exception as e:
        return f"Connection error: {e}", analysis_result


def send_message(text):
    if not text:
        return

    st.session_state[CHAT_KEY].append(("user", text))
    bot_reply, _ = get_bot_reply(text)
    st.session_state[CHAT_KEY].append(("bot", bot_reply))


st.markdown(f"""
<style>
:root{{
    --navy:#0f2446;
    --accent:#2f80ed;
    --accent2:#1c6fa4;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}}

html, body, [data-testid="stAppViewContainer"]{{
    background:#eef2f7;
    direction:ltr;
}}

header, footer, #MainMenu{{
    visibility:hidden;
}}

.block-container{{
    width:{PHONE_WIDTH}px;
    height:{PHONE_HEIGHT}px;
    max-width:calc(100vw - 24px);
    max-height:calc(100vh - 24px);
    margin:auto;
    padding:25px 24px 14px;
    box-sizing:border-box;
    background:linear-gradient(160deg,var(--bg1) 0%,var(--bg2) 45%,var(--bg3) 100%);
    border-radius:42px;
    box-shadow:0 10px 30px rgba(0,0,0,.15);
    overflow:hidden;
}}

.topbar{{
    height:58px;
    background:white;
    border-radius:18px;
    display:flex;
    align-items:center;
    gap:10px;
    padding:0 14px;
    box-shadow:0 3px 10px rgba(0,0,0,.12);
    margin-bottom:10px;
}}

.back{{
    font-size:28px;
    color:#436577;
    text-decoration:none;
    font-weight:700;
}}

.avatar{{
    width:42px;
    height:42px;
    border-radius:50%;
    object-fit:cover;
}}

.dot{{
    width:8px;
    height:8px;
    background:#36c06a;
    border-radius:50%;
}}

.status{{
    font-size:15px;
    font-weight:700;
    color:#222;
}}

.region-label{{
    margin-left:auto;
    font-size:11px;
    color:#436577;
    font-weight:700;
}}

.quick-title{{
    font-size:13px;
    font-weight:800;
    color:var(--navy);
    margin:4px 0 6px;
}}
div[data-testid="stButton"]{{
    margin:4px 1% !important;
    vertical-align:top !important;
}}
div[data-testid="stHorizontalBlock"]{{
    gap:8px !important;
}}

div[data-testid="stButton"] button{{
    height:42px !important;
    border-radius:22px !important;
    font-size:11px !important;
    font-weight:700 !important;
    padding:0 4px !important;
    background:white !important;
    color:black !important;
}}
.chat-area{{
    height:430px;
    overflow-y:auto;
    padding:10px 4px;
    margin-top:10px;
    margin-bottom:8px;
}}

.msg{{
    max-width:75%;
    padding:9px 12px;
    border-radius:16px;
    margin-bottom:8px;
    font-size:13px;
    line-height:1.5;
    white-space:pre-wrap;
    text-align:left;
}}

.message-row{{
    display:flex;
    align-items:flex-end;
    gap:6px;
    margin-bottom:8px;
}}

.message-row.user-row{{
    justify-content:flex-end;
}}

.message-row.bot-row{{
    justify-content:flex-start;
}}

.msg-avatar{{
    width:26px;
    height:26px;
    border-radius:50%;
    object-fit:cover;
    display:flex;
    align-items:center;
    justify-content:center;
    overflow:hidden;
    font-size:13px;
    background:white;
}}

.bot{{
    background:white;
    color:#222;
    margin-right:auto;
}}

.user{{
    background:var(--accent2);
    color:white;
    margin-left:auto;
}}

div[data-testid="stChatInput"]{{
    position:relative !important;
    bottom:auto !important;
    background:transparent !important;
    padding:0 !important;
}}

div[data-testid="stChatInput"] textarea{{
    direction:ltr;
    border-radius:25px;
    border:none;
    background:white;
    font-size:13px;
}}
</style>
""", unsafe_allow_html=True)

region = st.session_state.get("region", "Amman")

st.markdown(f"""
<div class="topbar">
    <a class="back" href="/?page=customer">‹</a>
    <img class="avatar" src="data:image/png;base64,{robot}">
    <div class="dot"></div>
    <div class="status">Ready to assist</div>
    <div class="region-label">📍 {html_lib.escape(region)}</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="quick-title">Quick Services</div>', unsafe_allow_html=True)

st.markdown("""
<style>

div[data-testid="stForm"]{
    border:none !important;
    background:transparent !important;
    padding:0 !important;
}

div[data-testid="stForm"] form{
    display:grid !important;
    grid-template-columns:repeat(3,1fr) !important;
    gap:10px !important;
}

div[data-testid="stFormSubmitButton"]{
    width:100% !important;
}

div[data-testid="stFormSubmitButton"] button{
    width:100% !important;
    height:42px !important;
    border-radius:22px !important;
    background:white !important;
    color:black !important;
    border:none !important;
    font-size:10px !important;
    font-weight:700 !important;
    padding:0 4px !important;
    line-height:1.15 !important;
    white-space:normal !important;
    box-shadow:0 4px 12px rgba(0,0,0,.08) !important;
}

.clear-chat-wrap{
    display:flex;
    justify-content:center;
    margin-top:14px;
}

div[data-testid="stButton"] button{
    height:42px !important;
    border-radius:22px !important;
    background:white !important;
    color:black !important;
    border:none !important;
    font-size:11px !important;
    font-weight:700 !important;
    padding:0 20px !important;
}

</style>
""", unsafe_allow_html=True)

with st.form("quick_services_form"):

    b1 = st.form_submit_button("Network Test")
    b2 = st.form_submit_button("Internet Usage")
    b3 = st.form_submit_button("Renew Package")
    b4 = st.form_submit_button("International Calls")
    b5 = st.form_submit_button("Offers & Games")
    b6 = st.form_submit_button("Contact Support")

if b1:
    send_message("Network Test")
    st.rerun()

elif b2:
    send_message("Internet Usage")
    st.rerun()

elif b3:
    send_message("Renew Package")
    st.rerun()

elif b4:
    send_message("International Calls")
    st.rerun()

elif b5:
    send_message("Offers & Games")
    st.rerun()

elif b6:
    send_message("Contact Support")
    st.rerun()

st.markdown('<div class="clear-chat-wrap">', unsafe_allow_html=True)

if st.button("Clear Chat", key="clear_chat_btn"):
    st.session_state[CHAT_KEY] = [
        ("bot", "Hi 👋 I am CoCare AI Assistant. How can I help you?")
    ]
    reset_context()
    st.rerun()
    
st.markdown('</div>', unsafe_allow_html=True)
        st.rerun()
chat_html = '<div class="chat-area">'

for role, message in st.session_state[CHAT_KEY]:
    safe_msg = html_lib.escape(str(message))

    if role == "user":
        chat_html += f"""
<div class="message-row user-row">
    <div class="msg user">{safe_msg}</div>
    <div class="msg-avatar user-avatar">U</div>
</div>
"""
    else:
        chat_html += f"""
<div class="message-row bot-row">
    <img class="msg-avatar" src="data:image/png;base64,{robot}">
    <div class="msg bot">{safe_msg}</div>
</div>
"""

chat_html += """
</div>
<script>
const chatArea = window.parent.document.querySelector('.chat-area');
if (chatArea) {
    chatArea.scrollTop = chatArea.scrollHeight;
}
</script>
"""

st.markdown(chat_html, unsafe_allow_html=True)

user_input = st.chat_input("Type your question here...")

if user_input:
    send_message(user_input)
    st.rerun()
