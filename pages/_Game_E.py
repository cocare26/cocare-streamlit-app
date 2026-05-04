import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Game", layout="centered")

st.markdown("""
<style>
:root{
    --navy:#0f2446;
    --accent:#2f80ed;
    --accent2:#1c6fa4;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}

[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}

.block-container{
    max-width:420px;
    margin:auto;
    padding:18px 0 0 0;
    background:linear-gradient(160deg,var(--bg1),var(--bg2),var(--bg3));
    border-radius:42px;
    box-shadow:0 10px 30px rgba(0,0,0,.15);
    overflow:visible;
}
</style>
""", unsafe_allow_html=True)

html = """
<html>
<head>
<style>
html, body{
    margin:0;
    padding:0;
    font-family:Arial;
    direction:ltr;
    background:transparent;
}

.game{
    width:420px;
    height:810px;
    background:linear-gradient(160deg,#d6ecff 0%,#bfe3ff 45%,#eaf6ff 100%);
    text-align:center;
    overflow:hidden;
    border-radius:42px;
    padding-top:22px;
    box-sizing:border-box;
}

.header{
    width:350px;
    margin:0 auto 8px;
    padding:12px 10px;
    border-radius:32px;
    background:rgba(255,255,255,.78);
    box-shadow:0 10px 30px rgba(0,0,0,.15);
}

.title{
    font-size:34px;
    font-weight:900;
    color:#0f2446;
}

.desc{
    font-size:15px;
    font-weight:800;
    color:#0f2446;
    margin-top:6px;
    line-height:1.25;
}

.prizes{
    display:flex;
    justify-content:center;
    gap:7px;
    margin-top:12px;
}

.prize{
    width:80px;
    height:66px;
    background:white;
    border-radius:14px;
    box-shadow:0 2px 8px rgba(0,0,0,.1);
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
    transform:translateY(-8px) scale(1.06);
    box-shadow:0 8px 18px rgba(0,0,0,.2);
}

.prize span{
    font-size:24px;
}

.wheel-wrap{
    width:315px;
    height:315px;
    margin:30px auto 18px;
    position:relative;
}

.pointer{
    position:absolute;
    top:-27px;
    left:50%;
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
    line-height:1.15;
}

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
    top:53%;
    left:53%;
    transform:translate(-50%,-50%);
    width:76px;
    height:76px;
    border-radius:50%;
    background:linear-gradient(90deg,#2f80ed,#1c6fa4);
    color:white;
    font-size:22px;
    font-weight:900;
    border:6px solid #f6c64a;
    display:flex;
    align-items:center;
    justify-content:center;
    cursor:pointer;
    transition:.25s;
    z-index:20;
    box-shadow:0 6px 14px rgba(47,128,237,.25);
}

.center:hover{
    transform:translate(-50%,-60%) scale(1.08);
    box-shadow:0 8px 18px rgba(0,0,0,.2);
}

.result{
    font-size:19px;
    font-weight:900;
    color:#0f2446;
    margin-top:12px;
    min-height:28px;
}

.tries,.points{
    font-size:17px;
    font-weight:900;
    color:#0f2446;
    margin-top:8px;
}

.extra{
    width:300px;
    height:46px;
    margin:18px auto 0;
    border-radius:25px;
    background:linear-gradient(90deg,#2f80ed,#1c6fa4);
    color:white;
    line-height:46px;
    font-weight:900;
    cursor:pointer;
    transition:.25s;
    box-shadow:0 6px 14px rgba(47,128,237,.25);
}

.extra:hover{
    transform:translateY(-6px) scale(1.03);
    box-shadow:0 8px 18px rgba(0,0,0,.2);
}
</style>
</head>

<body>
<div class="game">

    <div class="header">
        <div class="title">Play & Win!</div>
        <div class="desc">Spin the wheel to win internet bundles, points or vouchers!</div>

        <div class="prizes">
            <div class="prize"><span>💰</span>+10 GB</div>
            <div class="prize"><span>⭐</span>+50 Points</div>
            <div class="prize"><span>🎁</span>Voucher</div>
            <div class="prize"><span>🌐</span>1 GB</div>
        </div>
    </div>

    <div class="wheel-wrap">
        <div class="pointer"><span>⭐</span></div>

        <div id="wheel" class="wheel">
            <div class="slice s1">⭐ 50<br>Points</div>
            <div class="slice s2">🌐<br>1 GB</div>
            <div class="slice s3">⭐ 100<br>Points</div>
            <div class="slice s4">⭐ 20<br>Points</div>
            <div class="slice s5">🎁<br>Voucher</div>
            <div class="slice s6">😢 Try<br>Again</div>
            <div class="slice s7">💰<br>+5 GB</div>
            <div class="slice s8">🚀<br>+10 GB</div>
        </div>

        <div class="center" onclick="spin()">Spin</div>
    </div>

    <div id="result" class="result"></div>
    <div id="tries" class="tries">Attempts left: 1</div>
    <div id="points" class="points">Total points: 0</div>

    <div class="extra" onclick="buyTry()">+ Extra attempt for 100 ⭐</div>

</div>

<script>
let currentRotation = 0;
let tries = 1;
let totalPoints = 0;

const rewards = [
    {text:"⭐ 50 Points", points:50},
    {text:"🌐 1 GB", points:0},
    {text:"⭐ 100 Points", points:100},
    {text:"⭐ 20 Points", points:20},
    {text:"🎁 Voucher", points:0},
    {text:"😢 Try Again", points:0},
    {text:"💰 +5 GB", points:0},
    {text:"🚀 +10 GB", points:0}
];

function updateUI(){
    document.getElementById("tries").innerText = "Attempts left: " + tries;
    document.getElementById("points").innerText = "Total points: " + totalPoints;
}

function spin(){
    if(tries <= 0){
        document.getElementById("result").innerText = "No attempts left 😢";
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

        if(reward.text.includes("Try")){
            document.getElementById("result").innerText = "Try again 😢";
        }else{
            document.getElementById("result").innerText = "🎉 You won: " + reward.text;
        }

        totalPoints += reward.points;
        updateUI();
    },3000);
}

function buyTry(){
    if(totalPoints >= 100){
        totalPoints -= 100;
        tries++;
        document.getElementById("result").innerText = "✅ Extra attempt added";
    }else{
        document.getElementById("result").innerText = "Not enough points";
    }
    updateUI();
}
</script>

</body>
</html>
"""

components.html(html, height=900, scrolling=False)
