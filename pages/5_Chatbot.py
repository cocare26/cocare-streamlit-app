import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AI Chatbot", layout="centered")

html = """
<!DOCTYPE html>
<html>
<head>

<style>

body{
    margin:0;
    font-family:Arial;
}

.phone{
    width:420px;
    height:700px;
    margin:auto;
    border-radius:42px;
    overflow:hidden;
    position:relative;
    background:linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
}

.topbar{
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
}

.status{
    font-size:15px;
    font-weight:bold;
}

.chat-box{
    position:absolute;
    top:90px;
    left:18px;
    right:18px;
    bottom:75px;
    overflow-y:auto;
    padding:10px;
}

.msg{
    max-width:75%;
    padding:9px 12px;
    border-radius:16px;
    margin-bottom:8px;
    font-size:13px;
}

.bot{
    background:white;
    color:#222;
    margin-right:auto;
}

.user{
    background:#1c6fa4;
    color:white;
    margin-left:auto;
}

.bottom{
    position:absolute;
    bottom:18px;
    left:18px;
    right:18px;
    height:42px;
    display:flex;
    align-items:center;
    gap:8px;
}

.chat-input{
    flex:1;
    height:34px;
    background:white;
    border-radius:22px;
    border:none;
    padding-left:14px;
}

.send{
    width:40px;
    height:40px;
    border-radius:50%;
    background:#1c6fa4;
    color:white;
    text-align:center;
    line-height:40px;
    font-size:20px;
    cursor:pointer;
}

</style>
</head>

<body>

<div class="phone">

    <div class="topbar">
        <div class="status">Ready to assist</div>
    </div>

    <div id="chatBox" class="chat-box">
        <div class="msg bot">
            Hi, how can I help you?
        </div>
    </div>

    <div class="bottom">

        <input
            id="chatInput"
            class="chat-input"
            placeholder="Type your question here..."
            onkeydown="checkEnter(event)"
        >

        <div class="send" onclick="sendMessage()">➤</div>

    </div>

</div>

<script>

function addMessage(text, sender){

    const chatBox = document.getElementById("chatBox");

    const msg = document.createElement("div");

    msg.className = "msg " + sender;

    msg.innerText = text;

    chatBox.appendChild(msg);

    chatBox.scrollTop = chatBox.scrollHeight;
}

function getBotReply(message){

    let msg = message.toLowerCase();

    if(msg.includes("network")){
        return "Checking your network connection...";
    }

    if(msg.includes("renew")){
        return "You can renew your package from the services section.";
    }

    if(msg.includes("support")){
        return "Connecting you to customer support.";
    }

    if(msg.includes("internet")){
        return "Your internet service is working normally.";
    }

    return "Sorry, I did not understand your request.";
}

function sendMessage(){

    const input = document.getElementById("chatInput");

    const message = input.value.trim();

    if(message === "") return;

    addMessage(message,"user");

    input.value = "";

    setTimeout(() => {

        let reply = getBotReply(message);

        addMessage(reply,"bot");

    },500);
}

function checkEnter(event){

    if(event.key === "Enter"){
        sendMessage();
    }
}

</script>

</body>
</html>
"""

components.html(html,height=730)
