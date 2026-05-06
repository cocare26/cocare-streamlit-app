import streamlit as st
import streamlit.components.v1 as components
import base64
import pandas as pd
from datetime import datetime
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from chatbot_engine import process_message

st.set_page_config(page_title="AI Agent", layout="centered")


# =========================
# SIMPLE ENGLISH CHATBOT ENGINE
# =========================
def process_message(user_message, user_id="customer_1", region="Amman"):
    text = user_message.lower()

    if any(w in text for w in ["hello", "hi", "hey"]):
        intent = "greeting"
        intent_confidence = 0.90
    elif any(w in text for w in ["slow", "internet", "lag"]):
        intent = "slow_internet"
        intent_confidence = 0.90
    elif any(w in text for w in ["signal", "coverage"]):
        intent = "no_signal"
        intent_confidence = 0.90
    elif any(w in text for w in ["support", "help"]):
        intent = "technical_support"
        intent_confidence = 0.90
    else:
        intent = "unknown"
        intent_confidence = 0.50

    if any(w in text for w in ["bad", "slow", "problem", "angry", "terrible", "poor", "not working"]):
        sentiment = "negative"
        sentiment_score = 0.90
    elif any(w in text for w in ["good", "great", "thanks", "excellent"]):
        sentiment = "positive"
        sentiment_score = 0.90
    else:
        sentiment = "neutral"
        sentiment_score = 0.50

    responses = {
        "greeting": ("Hello 👋 How can I help you?", "What would you like to know?"),
        "slow_internet": (f"It looks like your internet is slow in {region}.", "Do you want me to help troubleshoot it?"),
        "no_signal": (f"There seems to be a signal issue in {region}.", "When did the issue start?"),
        "technical_support": ("You will be transferred to technical support 👨‍💻.", "Please describe the problem."),
        "unknown": ("Could you clarify more?", "Please provide more details.")
    }

    response, followup = responses.get(intent, responses["unknown"])

    prediction = 1 if intent in ["slow_internet", "no_signal"] else 0
    network_problem = prediction == 1
    escalation_alert = sentiment == "negative" or prediction == 1 or intent_confidence < 0.6

    return {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "user_id": user_id,
        "region": region,
        "language": "en",
        "intent": intent,
        "intent_confidence": intent_confidence,
        "sentiment": sentiment,
        "sentiment_score": sentiment_score,
        "response": response,
        "followup_response": followup,
        "prediction": prediction,
        "issue_type": intent if network_problem else "normal",
        "network_problem": network_problem,
        "escalation_alert": escalation_alert
    }


if "chat_logs" not in st.session_state:
    st.session_state.chat_logs = []


# =========================
# IMAGE
# =========================
try:
    with open("robot_head.png", "rb") as f:
        robot = base64.b64encode(f.read()).decode()
except FileNotFoundError:
    robot = ""


# =========================
# CHATBOT UI
# =========================
html = f"""
<html>
<head>
<style>
body {{
    margin:0;
    background:#eef2f7;
    font-family:Arial;
}}

.phone {{
    width:420px;
    height:700px;
    margin:auto;
    border-radius:42px;
    overflow:hidden;
    position:relative;
    background:linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
}}

.topbar {{
    position:absolute;
    top:14px;
    left:18px;
    right:18px;
    height:58px;
    background:white;
    border-radius:18px;
    display:flex;
    align-items:center;
    gap:10px;
    padding:0 14px;
    box-shadow:0 3px 10px rgba(0,0,0,.12);
}}

.back {{
    font-size:28px;
    color:#436577;
}}

.avatar {{
    width:42px;
    height:42px;
    border-radius:50%;
    object-fit:cover;
}}

.dot {{
    width:8px;
    height:8px;
    background:#36c06a;
    border-radius:50%;
}}

.status {{
    font-size:15px;
    font-weight:700;
    color:#222;
}}

.chat-box {{
    position:absolute;
    top:90px;
    left:18px;
    right:18px;
    bottom:75px;
    overflow-y:auto;
    padding:10px;
}}

.msg {{
    max-width:75%;
    padding:9px 12px;
    border-radius:16px;
    margin-bottom:8px;
    font-size:13px;
    line-height:1.4;
}}

.bot {{
    background:white;
    color:#222;
    margin-right:auto;
}}

.user {{
    background:#1c6fa4;
    color:white;
    margin-left:auto;
}}

.menu {{
    display:none;
    position:absolute;
    left:38px;
    bottom:90px;
    width:150px;
    background:white;
    border-radius:8px;
    box-shadow:0 4px 12px rgba(0,0,0,.18);
    padding:8px 0;
    z-index:5;
}}

.menu div {{
    font-size:13px;
    padding:7px 13px;
    color:#222;
    cursor:pointer;
}}

.menu div:hover {{
    background:#eef3f6;
}}

.bottom {{
    position:absolute;
    bottom:18px;
    left:18px;
    right:18px;
    height:42px;
    display:flex;
    align-items:center;
    gap:8px;
}}

.hamburger {{
    width:32px;
    height:32px;
    border-radius:50%;
    background:white;
    text-align:center;
    line-height:32px;
    font-size:22px;
    color:#50768a;
    cursor:pointer;
}}

.chat-input {{
    flex:1;
    height:34px;
    background:white;
    border-radius:22px;
    color:#444;
    font-size:12px;
    padding-left:14px;
    border:none;
    outline:none;
}}

.send {{
    width:40px;
    height:40px;
    border-radius:50%;
    background:linear-gradient(135deg,#6ec6ff,#1c6fa4);
    color:white;
    text-align:center;
    line-height:40px;
    font-size:20px;
    cursor:pointer;
}}
</style>
</head>

<body>
<div class="phone">

    <div class="topbar">
        <a href="/Customer" target="_self" style="text-decoration:none;">
            <div class="back">‹</div>
        </a>
        <img class="avatar" src="data:image/png;base64,{robot}">
        <div class="dot"></div>
        <div class="status">Ready to assist</div>
    </div>

    <div id="chatBox" class="chat-box">
        <div class="msg bot">Hi, how can I help you?</div>
    </div>

    <div id="menu" class="menu">
        <div onclick="quickMsg('Network Test')">Network Test</div>
        <div onclick="quickMsg('Internet Usage')">Internet Usage</div>
        <div onclick="quickMsg('Renew Package')">Renew Package</div>
        <div onclick="quickMsg('International Calls')">International Calls</div>
        <div onclick="quickMsg('Offers & Games')">Offers & Games</div>
        <div onclick="quickMsg('Contact Support')">Contact Support</div>
    </div>

    <div class="bottom">
        <div class="hamburger" onclick="toggleMenu()">≡</div>
        <input id="chatInput" class="chat-input" placeholder="Type your question here..." onkeydown="checkEnter(event)">
        <div class="send" onclick="sendMessage()">➤</div>
    </div>

</div>

<script>
function toggleMenu(){{
    const menu = document.getElementById("menu");
    menu.style.display = menu.style.display === "block" ? "none" : "block";
}}

function addMessage(text, type){{
    const chatBox = document.getElementById("chatBox");
    const msg = document.createElement("div");
    msg.className = "msg " + type;
    msg.innerText = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}}

function botReply(text){{
    let reply = "Use the backend input below to connect this message with the AI model.";

    if(text === "Network Test"){{
        reply = "Network Test selected. Analyze it from the backend input below.";
    }}
    else if(text === "Internet Usage"){{
        reply = "Internet Usage selected. Analyze it from the backend input below.";
    }}
    else if(text === "Renew Package"){{
        reply = "Renew Package selected. Analyze it from the backend input below.";
    }}
    else if(text === "International Calls"){{
        reply = "International Calls selected. Analyze it from the backend input below.";
    }}
    else if(text === "Offers & Games"){{
        reply = "Offers & Games selected. Analyze it from the backend input below.";
    }}
    else if(text === "Contact Support"){{
        reply = "Contact Support selected. Analyze it from the backend input below.";
    }}

    setTimeout(function(){{
        addMessage(reply, "bot");
    }}, 500);
}}

function sendMessage(){{
    const input = document.getElementById("chatInput");
    const text = input.value.trim();

    if(text === "") return;

    addMessage(text, "user");
    input.value = "";
    botReply(text);
}}

function quickMsg(text){{
    document.getElementById("menu").style.display = "none";
    addMessage(text, "user");
    botReply(text);
}}

function checkEnter(event){{
    if(event.key === "Enter"){{
        sendMessage();
    }}
}}
</script>

</body>
</html>
"""

components.html(html, height=730)


# =========================
# REAL BACKEND CONNECTION
# =========================
st.divider()
st.subheader("English Chatbot Backend Test")

user_msg = st.text_input("Type English message:")

if st.button("Send to Model"):
    if user_msg.strip():
        result = process_message(
            user_message=user_msg,
            user_id="customer_1",
            region="Amman"
        )

        st.session_state.chat_logs.append(result)

        st.success(result["response"])
        st.info(result["followup_response"])

        if result["escalation_alert"]:
            st.warning("Escalation Alert: This case needs attention.")

        st.write(result)


# =========================
# DASHBOARD
# =========================
st.subheader("Chatbot Dashboard")

if st.session_state.chat_logs:
    df = pd.DataFrame(st.session_state.chat_logs)

    st.metric("Total Messages", len(df))
    st.metric("Negative Sentiment", len(df[df["sentiment"] == "negative"]))
    st.metric("Network Problems", len(df[df["network_problem"] == True]))

    st.dataframe(df)

    st.write("Intent Distribution")
    st.bar_chart(df["intent"].value_counts())

    st.write("Sentiment Distribution")
    st.bar_chart(df["sentiment"].value_counts())

else:
    st.info("No messages yet.")
