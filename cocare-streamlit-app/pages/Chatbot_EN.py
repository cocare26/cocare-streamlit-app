import streamlit as st
import base64
import os
import sys
import html as html_lib
import pandas as pd
from datetime import datetime, timedelta

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cocare import process_message

st.set_page_config(page_title="AI Agent", layout="centered")

PHONE_WIDTH = 430
PHONE_HEIGHT = 820

CHAT_KEY = "chat_en_messages"
CONTEXT_KEY = "chat_en_context"

LOG_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "data", "chat_logs.csv")
)

JORDAN_REGIONS = [
    "Amman", "Zarqa", "Irbid", "Balqa", "Madaba", "Karak",
    "Tafilah", "Maan", "Aqaba", "Jerash", "Ajloun", "Mafraq"
]

PROBLEM_WORDS = [
    "problem", "issue", "slow", "weak", "disconnect", "disconnection",
    "cut", "outage", "fault", "network", "signal", "internet"
]

NEGATIVE_WORDS = [
    "bad", "angry", "terrible", "worst", "stupid", "useless",
    "hate", "annoying", "trash"
]

if "region" not in st.session_state:
    st.session_state["region"] = "Amman"

if CONTEXT_KEY not in st.session_state:
    st.session_state[CONTEXT_KEY] = {
        "last_intent": None,
        "awaiting_details": False,
        "last_network_problem": False
    }

if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = [
        ("bot", "Hi 👋 I am CoCare AI Assistant. How can I help you?")
    ]


def reset_context():
    st.session_state[CONTEXT_KEY] = {
        "last_intent": None,
        "awaiting_details": False,
        "last_network_problem": False
    }


def img_to_base64(path):
    try:
        paths = [
            os.path.join(os.path.dirname(__file__), path),
            os.path.join(os.path.dirname(__file__), "..", path),
        ]

        for full_path in paths:
            if os.path.exists(full_path):
                with open(full_path, "rb") as f:
                    return base64.b64encode(f.read()).decode()
    except Exception:
        pass

    return ""


robot = (
    img_to_base64("robot_black.png")
    or img_to_base64("robot_head.png")
    or img_to_base64("robot.png")
)


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


def cleanup_old_logs():
    if not os.path.exists(LOG_PATH):
        return

    try:
        df = pd.read_csv(LOG_PATH)
        if "time" not in df.columns:
            return

        df["time"] = pd.to_datetime(df["time"], errors="coerce")
        cutoff = datetime.now() - timedelta(hours=48)
        df = df[df["time"] >= cutoff]
        df.to_csv(LOG_PATH, index=False)

    except Exception:
        pass


def current_message_has_problem(text):
    t = str(text).lower()
    return any(word in t for word in PROBLEM_WORDS)


def has_negative_language(text):
    t = str(text).lower()
    return any(word in t for word in NEGATIVE_WORDS)


def detect_network_problem_type(text):
    t = str(text).lower()

    if any(w in t for w in ["slow"]):
        return "slow_connection"

    if any(w in t for w in ["weak signal", "signal"]):
        return "weak_signal"

    if any(w in t for w in ["disconnect", "cut"]):
        return "disconnection"

    if any(w in t for w in ["outage", "fault"]):
        return "outage"

    if any(w in t for w in ["network", "internet"]):
        return "general_network_issue"

    return "none"


def get_repeat_count(user_id):
    if not os.path.exists(LOG_PATH):
        return 0

    try:
        df = pd.read_csv(LOG_PATH)
        if "user_id" not in df.columns:
            return 0

        return len(df[df["user_id"] == user_id])

    except Exception:
        return 0


def get_area_issue_count(region):
    if not os.path.exists(LOG_PATH):
        return 0

    try:
        df = pd.read_csv(LOG_PATH)
        if "region" not in df.columns or "network_problem" not in df.columns:
            return 0

        area_df = df[
            (df["region"] == region) &
            (df["network_problem"] == True)
        ]

        return len(area_df)

    except Exception:
        return 0


def decide_escalation(user_id, region, network_problem):
    repeat_count = get_repeat_count(user_id)
    area_issue_count = get_area_issue_count(region)

    notification_type = "none"
    display_channel = "monitoring_log"
    escalation = False
    reason = "normal_monitoring"
    priority = "low"
    decision_rule = "monitoring_log"

    if network_problem and repeat_count >= 2:
        notification_type = "external_notification"
        display_channel = "customer_app"
        escalation = True
        reason = "third_complaint_from_same_customer"
        priority = "medium"
        decision_rule = "customer_app"

    if network_problem and area_issue_count >= 2:
        notification_type = "internal_escalation"
        display_channel = "employee_dashboard"
        escalation = True
        reason = "third_complaint_in_same_region"
        priority = "high"
        decision_rule = "employee_dashboard"

    return {
        "repeat_count": repeat_count + 1,
        "area_issue_count": area_issue_count + 1,
        "notification_type": notification_type,
        "display_channel": display_channel,
        "escalation": escalation,
        "reason": reason,
        "priority": priority,
        "decision_rule": decision_rule
    }


def save_chat_log(row):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

    df = pd.DataFrame([row])

    if os.path.exists(LOG_PATH):
        df.to_csv(LOG_PATH, mode="a", header=False, index=False)
    else:
        df.to_csv(LOG_PATH, index=False)


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

    cleanup_old_logs()

    if region not in JORDAN_REGIONS:
        region = "Amman"

    try:
        result = process_message(msg, user_id=user_id, region=region)
        analysis_result = result

        message_has_problem = current_message_has_problem(msg)
        negative_language = has_negative_language(msg)

        network_problem = bool(result.get("network_problem", False)) and message_has_problem
        network_problem_type = detect_network_problem_type(msg) if network_problem else "none"

        decision = decide_escalation(user_id, region, network_problem)

        if negative_language:
            result["response"] = (
                "I apologize for the inconvenience. I understand that this situation is frustrating. "
                "I will check the issue and guide you to the right support step."
            )

        log_row = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user_id": user_id,
            "region": region,
            "message": msg,
            "bot_response": result.get("response", ""),
            "intent": result.get("intent", ""),
            "sentiment": result.get("sentiment", ""),
            "prediction": result.get("prediction", ""),
            "issue_type": result.get("issue_type", ""),
            "network_problem": network_problem,
            "repeat_count": decision["repeat_count"],
            "area_issue_count": decision["area_issue_count"],
            "notification_type": decision["notification_type"],
            "display_channel": decision["display_channel"],
            "escalation": decision["escalation"],
            "reason": decision["reason"],
            "priority": decision["priority"],
            "decision_rule": decision["decision_rule"]
        }

        save_chat_log(log_row)

        result["network_problem"] = network_problem
        result["network_problem_type"] = network_problem_type
        result.update(decision)

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
html, body, [data-testid="stAppViewContainer"] {{
    background:#d8ecff;
    direction:ltr;
}}

header, footer, #MainMenu {{
    visibility:hidden;
}}

.block-container {{
    width:{PHONE_WIDTH}px !important;
    height:{PHONE_HEIGHT}px !important;
    max-width:{PHONE_WIDTH}px !important;
    min-height:{PHONE_HEIGHT}px !important;
    margin:auto;
    padding:14px 14px 8px;
    border-radius:34px;
    background:#f8fcff;
    box-shadow:0 12px 35px rgba(0,0,0,.14);
    overflow:hidden;
    border:1px solid #cfe8ff;
}}

.topbar {{
    height:130px;
    background:#f9fcff;
    border-radius:26px 26px 0 0;
    display:grid;
    grid-template-columns:92px 1fr 90px;
    align-items:center;
    gap:12px;
    padding:14px;
    border-bottom:1px solid #cfe4f7;
}}

.avatar-wrap {{
    position:relative;
    width:84px;
    height:84px;
}}

.avatar {{
    width:84px;
    height:84px;
    border-radius:50%;
    object-fit:cover;
    background:white;
    box-shadow:0 5px 14px rgba(0,0,0,.16);
}}

.dot {{
    position:absolute;
    right:-2px;
    bottom:12px;
    width:14px;
    height:14px;
    background:#43d43b;
    border-radius:50%;
    border:3px solid white;
}}

.status-main {{
    font-size:20px;
    font-weight:900;
    color:#102646;
}}

.status-sub {{
    font-size:14px;
    color:#6b7280;
    margin-top:5px;
}}

.region-label {{
    background:white;
    color:#111827;
    font-size:15px;
    font-weight:800;
    border-radius:16px;
    padding:12px 10px;
    text-align:center;
    box-shadow:0 3px 10px rgba(0,0,0,.13);
}}

.quick-title {{
    font-size:18px;
    font-weight:900;
    color:#102646;
    margin:14px 4px 12px;
    text-align:left;
}}

div[data-testid="stHorizontalBlock"] {{
    gap:10px;
}}

div[data-testid="stButton"] button {{
    height:70px;
    border-radius:16px;
    border:1px solid #edf2f7;
    background:white;
    color:#155aa0;
    font-weight:900;
    font-size:14px;
    box-shadow:0 4px 12px rgba(0,0,0,.10);
    transition:.2s;
}}

div[data-testid="stButton"] button:hover {{
    background:#f4f9ff;
    color:#0f4f91;
    transform:translateY(-2px);
}}

.chat-area {{
    height:360px;
    overflow-y:auto;
    padding:18px 8px;
    margin-top:14px;
    margin-bottom:10px;
    background:linear-gradient(180deg,#f2f8ff,#eef7ff);
    border-top:1px solid #dbeafe;
    border-bottom:1px solid #dbeafe;
}}

.chat-area::-webkit-scrollbar {{
    width:5px;
}}

.chat-area::-webkit-scrollbar-thumb {{
    background:#c4cdd8;
    border-radius:10px;
}}

.message-row {{
    display:flex;
    align-items:flex-end;
    margin-bottom:18px;
    gap:8px;
}}

.user-row {{
    justify-content:flex-end;
}}

.bot-row {{
    justify-content:flex-start;
}}

.msg {{
    max-width:74%;
    padding:12px 16px;
    border-radius:18px;
    font-size:15px;
    line-height:1.7;
    white-space:pre-wrap;
    text-align:left;
}}

.bot {{
    background:white;
    color:#111;
    border-bottom-left-radius:5px;
    box-shadow:0 3px 10px rgba(0,0,0,.12);
}}

.user {{
    background:linear-gradient(135deg,#4aa3ff,#1677e8);
    color:white;
    border-bottom-right-radius:5px;
    box-shadow:0 3px 10px rgba(22,119,232,.25);
}}

.msg-avatar {{
    width:38px;
    height:38px;
    border-radius:50%;
    object-fit:cover;
    background:white;
    box-shadow:0 3px 8px rgba(0,0,0,.14);
}}

.user-avatar {{
    width:38px;
    height:38px;
    border-radius:50%;
    background:white;
    color:#1762ad;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:20px;
    box-shadow:0 3px 8px rgba(0,0,0,.14);
}}

div[data-testid="stChatInput"] {{
    position:relative !important;
    bottom:auto !important;
    background:transparent !important;
    padding:0 !important;
}}

div[data-testid="stChatInput"] textarea {{
    direction:ltr;
    border-radius:24px;
    border:none;
    background:white;
    font-size:14px;
    min-height:45px;
    box-shadow:0 4px 12px rgba(0,0,0,.12);
}}
</style>
""", unsafe_allow_html=True)


region = st.session_state.get("region", "Amman")

st.markdown(f"""
<div class="topbar">

    <div class="avatar-wrap">
        <img class="avatar" src="data:image/png;base64,{robot}">
        <div class="dot"></div>
    </div>

    <div class="status-box">
        <div class="status-main">Ready to Assist</div>
        <div class="status-sub">CoCare AI Assistant</div>
    </div>

    <div class="region-label">
        📍 {html_lib.escape(region)}
    </div>

</div>
""", unsafe_allow_html=True)


st.markdown('<div class="quick-title">Quick Services</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
c4, c5, c6 = st.columns(3)

with c1:
    if st.button("📡\nNetwork Test"):
        send_message("Network Test")
        st.rerun()

with c2:
    if st.button("📊\nInternet Usage"):
        send_message("Internet Usage")
        st.rerun()

with c3:
    if st.button("🧾\nRenew Package"):
        send_message("Renew Package")
        st.rerun()

with c4:
    if st.button("☎️\nInternational Calls"):
        send_message("International Calls")
        st.rerun()

with c5:
    if st.button("🎁\nOffers & Games"):
        send_message("Offers & Games")
        st.rerun()

with c6:
    if st.button("🎧\nContact Support"):
        send_message("Contact Support")
        st.rerun()


chat_html = '<div class="chat-area">'

for role, message in st.session_state[CHAT_KEY]:
    safe_msg = html_lib.escape(str(message))

    if role == "user":
        chat_html += f"""
<div class="message-row user-row">
    <div class="msg user">{safe_msg}</div>
    <div class="msg-avatar user-avatar">👤</div>
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


if st.button("🗑️ Clear Chat"):
    st.session_state[CHAT_KEY] = [
        ("bot", "Hi 👋 I am CoCare AI Assistant. How can I help you?")
    ]
    reset_context()
    st.rerun()


user_input = st.chat_input("Type your message here...")

if user_input:
    send_message(user_input)
    st.rerun()
