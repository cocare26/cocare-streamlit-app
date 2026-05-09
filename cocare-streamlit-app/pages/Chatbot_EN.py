import streamlit as st
import base64
import osimport sys
import html as html_lib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(file), "..")))from cocare import process_message

st.set_page_config(page_title="AI Agent", layout="centered")

PHONE_WIDTH = 390
PHONE_HEIGHT = 82

CHAT_KEY = "chat_en_messages"
CONTEXT_KEY = "chat_en_context"

if "region" not in st.session_state:
    st.session_state["region"] = "Amman"

if CONTEXT_KEY not in st.session_state:
    st.session_state[CONTEXT_KEY] = {"last_intent": None,"awaiting_details": False,"last_network_problem": False}

def reset_context():
    st.session_state[CONTEXT_KEY] = {"last_intent": None,"awaiting_details": False,"last_network_problem": False}

if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = [("bot", "Hi 👋 I am CoCare AI Assistant. How can I help you?")]

def img_to_base64(path):
    try:full_path = os.path.join(os.path.dirname(file), "..", path)if os.path.exists(full_path):with open(full_path, "rb") as f:return base64.b64encode(f.read()).decode()except Exception:passreturn ""

robot = img_to_base64("robot_head.png") or img_to_base64("robot.png")

def is_thanks_or_close(text):
    t = str(text).strip().lower()return any(p in t for p in ["thanks", "thank you", "ok", "okay", "fine", "great", "done","شكرا", "شكراً", "تمام"])

def is_goodbye(text):
    t = str(text).strip().lower()return any(p in t for p in ["bye", "goodbye", "see you", "مع السلامة", "باي"])

def is_no_problem(text):
    t = str(text).strip().lower()return any(p in t for p in ["no problem", "i have no problem", "nothing", "no issue","not now", "never mind"])

def is_social_positive(text):
    t = str(text).strip().lower()return any(p in t for p in ["nice", "good", "great", "perfect", "excellent", "awesome"])

def is_short_followup(text):
    return len(str(text).strip().split()) <= 8

def looks_like_time_answer(text):
    t = str(text).lower()return any(w in t for w in ["hour", "hours", "minute", "minutes", "today", "yesterday","morning", "evening", "week", "since", "ago"])

def looks_like_yes(text):
    return str(text).strip().lower() in ["yes", "yeah", "yep", "ok", "okay", "sure"]

def looks_like_no(text):
    return str(text).strip().lower() in ["no", "nope", "not"]

def looks_like_location(text):
    t = str(text).strip().lower()locations = ["amman", "zarqa", "irbid", "balqa", "madaba", "karak","tafilah", "maan", "aqaba", "jerash", "ajloun", "mafraq"]return any(loc in t for loc in locations)

def human_fallback_reply(text):
    = str(text).strip().lower()

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
    return (
        "Tell me which service you want to use, "
        "and I will explain the steps clearly."
    )

if any(w in t for w in ["where", "location", "place"]):
    return (
        "Please clarify what location you mean. "
        "If you mean a service inside the app, tell me its name."
    )

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

# NEW SERVICE REQUEST → RESET CONTEXT
if any(p in t for p in [
    "renew", "package",
    "usage", "data",
    "offer", "offers",
    "international", "calls",
    "support", "help",
    "network test"
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
    return (
        "Got it. I recorded the time or duration of the issue. "
        "The network status will be followed up by the technical team."
    )

if looks_like_location(msg):
    return (
        "Got it. I received your area. "
        "I will add it to the issue details for the technical team."
    )

if looks_like_yes(msg):
    return (
        "Okay. Try restarting the router or enabling airplane mode for 10 seconds, "
        "then tell me if the connection improves."
    )

if looks_like_no(msg):
    return (
        "Okay. I will record the issue without extra steps. "
        "If it continues, the technical team will follow up."
    )

return (
    "Got it. I received the details and will add them to the recorded issue."
)

def direct_service_reply(text):t = str(text).strip().lower()region = st.session_state.get("region", "Amman")

if t == "network test":
    reset_context()
    return (
        f"I can help you check the network status in {region}.\n\n"
        "Are you facing slow internet, disconnection, or weak signal?"
    )

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

def get_bot_reply(user_text):msg = str(user_text).strip()analysis_result = {}

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
    result = process_message(
        msg,
        user_id=user_id,
        region=region
    )

    analysis_result = result

    intent = result.get("intent", "")
    network_problem = result.get("network_problem", False)

    st.session_state[CONTEXT_KEY]["last_intent"] = intent
    st.session_state[CONTEXT_KEY]["last_network_problem"] = network_problem
    st.session_state[CONTEXT_KEY]["awaiting_details"] = bool(network_problem)

    if intent in ["clarification", "unknown", "other", "fallback"]:
        if len(msg.split()) > 4:
            return (
                "I understand. To help you better, please tell me whether this is about "
                "network, package, app, or another service."
            ), analysis_result

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
    

def send_message(text):if not text:return

st.session_state[CHAT_KEY].append(("user", text))
bot_reply, _ = get_bot_reply(text)
st.session_state[CHAT_KEY].append(("bot", bot_reply))

st.markdown(f"""

""", unsafe_allow_html=True)

region = st.session_state.get("region", "Amman")

st.markdown(f"""

st.markdown('Quick Services', unsafe_allow_html=True)

with st.form("quick_services_form"):st.markdown("""div[data-testid="stForm"] {border: none;padding: 0;background: transparent;}

div[data-testid="stForm"] > div {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
}

div[data-testid="stForm"] button {
    height: 42px;
    border-radius: 22px;
    background: white;
    color: black;
    font-size: 11px;
    font-weight: 700;
    padding: 0 4px;
    line-height: 1.15;
    white-space: normal;
}
</style>
""", unsafe_allow_html=True)

b1 = st.form_submit_button("Network Test")
b2 = st.form_submit_button("Internet Usage")
b3 = st.form_submit_button("Renew Package")
b4 = st.form_submit_button("International Calls")
b5 = st.form_submit_button("Offers & Games")
b6 = st.form_submit_button("Contact Support")

if b1:send_message("Network Test")st.rerun()elif b2:send_message("Internet Usage")st.rerun()elif b3:send_message("Renew Package")st.rerun()elif b4:send_message("International Calls")st.rerun()elif b5:send_message("Offers & Games")st.rerun()elif b6:send_message("Contact Support")st.rerun()

if st.button("Clear Chat", key="clear_chat_btn"):st.session_state[CHAT_KEY] = [("bot", "Hi 👋 I am CoCare AI Assistant. How can I help you?")]reset_context()st.rerun()

chat_html = ''for role, message in st.session_state[CHAT_KEY]:

safe_msg = html_lib.escape(str(message))

if role == "user":

    chat_html += f"""

else:

    typing_class = " typing" if str(message) == "Typing..." else ""

    chat_html += f"""

chat_html += """

"""

st.markdown(chat_html, unsafe_allow_html=True)user_input = st.chat_input("Type your question here...")

if user_input:send_message(user_input)st.rerun()
