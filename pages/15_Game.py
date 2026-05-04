import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Game", layout="centered")

html = """
<html>
<head>
<style>
body{
    margin:0;
    font-family:Arial;
    direction:rtl;
    background:#eef2f7;
}

.game{
    width:420px;
    height:810px;
    margin:auto;
    background:linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
    border-radius:42px;
    overflow:hidden;
    text-align:center;
}

.header{
    width:350px;
    margin:16px auto 6px;
    padding:10px;
    border-radius:32px;
    background:rgba(255,255,255,.75);
    box-shadow:0 4px 12px rgba(0,0,0,.15);
}

.title{
    font-size:34px;
    font-weight:900;
    color:#0f2446;
}

.desc{
    font-size:15px;
    font-weight:bold;
    color:#0f2446;
    margin-top:5px;
}

.prizes{
    display:flex;
    justify-content:center;
    gap:7px;
    margin-top:10px;
}

.prize{
    width:80px;
    height:66px;
    background:white;
    border-radius:14px;
    box-shadow:0 4px 10px rgba(0,0,0,.13);
    font-size:12px;
    font-weight:900;
    color:#0f2446;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    cursor:pointer;
    transition:.25s;
}

.prize:hover{
    transform:translateY(-8px) scale(1.08);
}

.prize span{
    font-size:24px;
}

.wheel-wrap{
    width:315px;
    height:315px;
    margin:34px auto 26px;
    position:relative;
}

.pointer{
    position:absolute;
    top:-28px;
    left:46%;
    transform:translateX(-50%) rotate(-45deg);
    width:48px;
    height:48px;
    border-radius:50% 50% 50% 0;
    background:#f6c64a;
    border:5px solid #b68417;
    display:flex;
    align-items:center;
    justify-content:center;
    z-index:50;
}

.pointer span{
    transform:rotate(45deg);
    font-size:21px;
}

.wheel{
    width:315px;
    height:315px;
    border-radius:50%;
    border:13px solid #c8941e;
    background:conic-gradient(
        #ffe58a 0deg 45deg,
        #bfe3ff 45deg 90deg,
        #d6ecff 90deg 135deg,
        #9fdcff 135deg 180deg,
        #ffd36e 180deg 225deg,
        #aee8c0 225deg 270deg,
        #f4f4f4 270deg 315deg,
        #f7d97d 315deg 360deg
    );
    box-shadow:0 10px 25px rgba(0,0,0,.25);
    transition:transform 3s ease-out;
    position:relative;
}

.wheel:before{
    content:"";
    position:absolute;
    inset:-7px;
    border-radius:50%;
    border:4px dotted rgba(255,255,255,.95);
}

.slice{
    position:absolute;
    left:50%;
    top:50%;
    width:88px;
    height:34px;
    margin-left:-44px;
    margin-top:-17px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:12px;
    font-weight:900;
    color:#0f2446;
    text-align:center;
    line-height:1.2;
}

/* توزيع الكلام داخل العجلة بشكل مقروء */
.s1{transform:rotate(22.5deg) translateY(-108px) rotate(-22.5deg)}
.s2{transform:rotate(67.5deg) translateY(-108px) rotate(-67.5deg)}
.s3{transform:rotate(112.5deg) translateY(-108px) rotate(-112.5deg)}
.s4{transform:rotate(157.5deg) translateY(-108px) rotate(-157.5deg)}
.s5{transform:rotate(202.5deg) translateY(-108px) rotate(-202.5deg)}
.s6{transform:rotate(247.5deg) translateY(-108px) rotate(-247.5deg)}
.s7{transform:rotate(292.5deg) translateY(-108px) rotate(-292.5deg)}
.s8{transform:rotate(337.5deg) translateY(-108px) rotate(-337.5deg)}

.center{
    position:absolute;
    top:52%;
    left:47%;
    transform:translate(-50%,-50%);
    width:76px;
    height:76px;
    border-radius:50%;
    background:linear-gradient(#54c7ff,#1c6fa4);
    color:white;
    font-size:24px;
    font-weight:bold;
    border:6px solid #f6c64a;
    display:flex;
    align-items:center;
    justify-content:center;
    cursor:pointer;
    transition:.25s;
    z-index:20;
}

.center:hover{
    transform:translate(-50%,-58%) scale(1.08);
}

.result{
    font-size:20px;
    font-weight:900;
    color:#0f2446;
    margin-top:4px;
    min-height:28px;
}

.tries,
.points{
    font-size:17px;
    font-weight:900;
    color:#0f2446;
    margin-top:8px;
}

.extra{
    width:300px;
    height:48px;
    margin:18px auto 0;
    border-radius:25px;
    background:linear-gradient(90deg,#2f80ed,#1c6fa4);
    color:white;
    line-height:48px;
    font-weight:bold;
    cursor:pointer;
    transition:.25s;
}

.extra:hover{
    transform:translateY(-6px) scale(1.03);
}
</style>
</head>

<body>

<div class="game">

    <div class="header">
        <div class="title">إلعب واربح!</div>
        <div class="desc">أدر العجلة لتربح حزم إنترنت إضافية أو نقاط أو قسائم!</div>

        <div class="prizes">
            <div class="prize"><span>💰</span>+10 جيجابايت</div>
            <div class="prize"><span>⭐</span>+50 نقطة</div>
            <div class="prize"><span>🎁</span>قسيمة</div>
            <div class="prize"><span>🌐</span>1 جيجابايت</div>
        </div>
    </div>

    <div class="wheel-wrap">
        <div class="pointer"><span>⭐</span></div>

        <div id="wheel" class="wheel">
            <div class="slice s1">⭐ 50 نقطة</div>
            <div class="slice s2">🌐 1 جيجا</div>
            <div class="slice s3">⭐ 100 نقطة</div>
            <div class="slice s4">⭐ 20 نقطة</div>
            <div class="slice s5">🎁 قسيمة</div>
            <div class="slice s6">😢 حظًا أوفر</div>
            <div class="slice s7">💰 +5 جيجا</div>
            <div class="slice s8">🚀 +10 جيجا</div>
        </div>

        <div class="center" onclick="spin()">أدر</div>
    </div>

    <div id="result" class="result"></div>
    <div id="tries" class="tries">المحاولات المتبقية: 1</div>
    <div id="points" class="points">مجموع النقاط: 0</div>

    <div class="extra" onclick="buyTry()">+ محاولة إضافية مقابل 100 نقطة ⭐</div>

</div>

<script>
let currentRotation = 0;
let tries = 1;
let totalPoints = 0;

const rewards = [
    {text:"⭐ 50 نقطة", points:50},
    {text:"🌐 1 جيجا", points:0},
    {text:"⭐ 100 نقطة", points:100},
    {text:"⭐ 20 نقطة", points:20},
    {text:"🎁 قسيمة", points:0},
    {text:"😢 حظًا أوفر", points:0},
    {text:"💰 +5 جيجا", points:0},
    {text:"🚀 +10 جيجا", points:0}
];

function updateUI(){
    document.getElementById("tries").innerText = "المحاولات المتبقية: " + tries;
    document.getElementById("points").innerText = "مجموع النقاط: " + totalPoints;
}

function spin(){
    if(tries <= 0){
        document.getElementById("result").innerText = "انتهت المحاولات 😢";
        return;
    }

    tries--;
    updateUI();

    const index = Math.floor(Math.random() * rewards.length);
    const sectorCenter = index * 45 + 22.5;
    const targetRotation = -sectorCenter;

    currentRotation += 1440 + targetRotation;

    document.getElementById("wheel").style.transform =
        "rotate(" + currentRotation + "deg)";

    setTimeout(()=>{
        const reward = rewards[index];

        if(reward.text.includes("حظًا")){
            document.getElementById("result").innerText = "حظًا أوفر 😢";
        }else{
            document.getElementById("result").innerText =
                "🎉 جائزتك: " + reward.text;
        }

        totalPoints += reward.points;
        updateUI();
    },3000);
}

function buyTry(){
    if(totalPoints >= 100){
        totalPoints -= 100;
        tries++;
        document.getElementById("result").innerText = "✅ تمت إضافة محاولة";
    }else{
        document.getElementById("result").innerText = "لا يوجد نقاط كافية";
    }
    updateUI();
}
</script>

</body>
</html>
"""

components.html(html, height=840)
