import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CoCare", layout="centered")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: #eef2f7;
}
.block-container {
    padding-top: 10px;
    max-width: 560px;
}
header, footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
* {
    box-sizing: border-box;
    font-family: Arial, sans-serif;
}

body {
    margin: 0;
    background: transparent;
}

.phone {
    width: 430px;
    margin: auto;
    background: #fbfdff;
    border-radius: 45px;
    padding: 24px 20px 12px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.25);
    border: 2px solid #d8dde6;
}

.top {
    display: grid;
    grid-template-columns: 135px 1fr;
    gap: 16px;
}

.rate-card {
    background: white;
    border-radius: 18px;
    height: 135px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.12);
}

.circle {
    width: 112px;
    height: 112px;
    border-radius: 50%;
    border: 12px solid #2f80ed;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.circle span {
    font-size: 11px;
}

.circle b {
    font-size: 25px;
}

.head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}

.title {
    font-size: 20px;
    font-weight: 800;
}

.location {
    font-size: 11px;
    color: #667085;
}

.map {
    height: 105px;
    border-radius: 16px;
    background: #e6ecf5;
    position: relative;
    overflow: hidden;
    box-shadow: inset 0 0 0 1px #d7deea;
}

.road {
    position: absolute;
    height: 3px;
    width: 240px;
    background: white;
    opacity: .9;
    transform: rotate(-35deg);
}

.road2 {
    position: absolute;
    height: 3px;
    width: 210px;
    background: white;
    opacity: .9;
    transform: rotate(35deg);
}

.dot {
    position: absolute;
    color: #e02020;
    font-size: 23px;
}

.section {
    font-size: 18px;
    font-weight: 800;
    margin: 20px 0 10px;
}

.alerts {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
}

.alert {
    background: white;
    border-radius: 12px;
    min-height: 112px;
    overflow: hidden;
    box-shadow: 0 4px 14px rgba(0,0,0,0.12);
    font-size: 11px;
}

.alert-head {
    color: white;
    padding: 8px;
    font-size: 14px;
    font-weight: 800;
}

.red { background: #e84c4c; }
.yellow { background: #f2b72f; }
.blue { background: #2f80ed; }

.alert-body {
    padding: 8px;
    line-height: 1.35;
}

.metrics {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
}

.chart {
    background: white;
    height: 130px;
    border-radius: 15px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.10);
    padding: 10px;
    position: relative;
}

.line {
    position: absolute;
    left: 35px;
    bottom: 45px;
    width: 135px;
    height: 65px;
}

.chart-title {
    position: absolute;
    bottom: 10px;
    width: 100%;
    left: 0;
    text-align: center;
    font-size: 13px;
}

.bar {
    position: absolute;
    bottom: 43px;
    width: 20px;
    background: #2f80ed;
}

.stars {
    text-align: center;
    color: #1267c9;
    font-size: 20px;
    margin-top: 4px;
}

.employee {
    display: flex;
    gap: 14px;
    align-items: center;
    background: white;
    border-radius: 15px;
    padding: 12px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.10);
}

.avatar {
    width: 65px;
    height: 65px;
    border-radius: 50%;
    background: #dbeafe;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 34px;
}

.emp-name {
    font-size: 18px;
    font-weight: 800;
}

.emp-text {
    font-size: 11px;
    line-height: 1.3;
}

.nav {
    margin-top: 14px;
    height: 72px;
    border-top: 1px solid #e5e7eb;
    display: flex;
    justify-content: space-around;
    align-items: center;
    font-weight: 800;
}

.nav div {
    text-align: center;
    font-size: 15px;
}

.nav span {
    display: block;
    font-size: 30px;
    color: #376f91;
}
</style>
</head>

<body>
<div class="phone">

    <div class="top">
        <div class="rate-card">
            <div class="circle">
                <span>Problem Rate:</span>
                <b>4.5%</b>
            </div>
        </div>

        <div>
            <div class="head">
                <div class="title">Network Issues</div>
                <div class="location">📍 Select Location</div>
            </div>

            <div class="map">
                <div class="road" style="top:10px;left:-55px;"></div>
                <div class="road" style="top:35px;left:-30px;"></div>
                <div class="road" style="top:60px;left:-55px;"></div>
                <div class="road" style="top:85px;left:-20px;"></div>
                <div class="road2" style="top:20px;left:60px;"></div>
                <div class="road2" style="top:55px;left:80px;"></div>
                <div class="road2" style="top:90px;left:95px;"></div>

                <div class="dot" style="top:20px;left:85px;">●</div>
                <div class="dot" style="top:42px;left:150px;">●</div>
                <div class="dot" style="top:68px;left:160px;">●</div>
                <div class="dot" style="top:13px;left:200px;font-size:14px;">●</div>
            </div>
        </div>
    </div>

    <div class="section">Alert History & Problems</div>

    <div class="alerts">
        <div class="alert">
            <div class="alert-head red">❗ Problem</div>
            <div class="alert-body">
                <b>Region:</b> Irbid: Multiple User Reports 09:30 AM of Slow Internet.
            </div>
        </div>

        <div class="alert">
            <div class="alert-head yellow">⚠️ Internal</div>
            <div class="alert-body">
                <b>Region:</b> Irbid: Multiple User Reports 09:30 AM of Slow Internet.
            </div>
        </div>

        <div class="alert">
            <div class="alert-head blue">↗ External</div>
            <div class="alert-body">
                <b>Region:</b> Irbid This Internet issue is external. The problem is reported by the ISP.
            </div>
        </div>
    </div>

    <div class="section">Network Performance Metrics</div>

    <div class="metrics">
        <div class="chart">
            <svg class="line" viewBox="0 0 140 70">
                <polygon points="0,65 0,55 45,40 95,25 135,5 135,65" fill="#dbeafe"/>
                <polyline points="0,55 45,40 95,25 135,5" fill="none" stroke="#2f80ed" stroke-width="4"/>
            </svg>
            <div style="position:absolute;left:15px;top:20px;font-size:12px;">20</div>
            <div style="position:absolute;left:15px;top:58px;font-size:12px;">10</div>
            <div style="position:absolute;left:15px;top:96px;font-size:12px;">0</div>
            <div class="chart-title">Avg Latency (ms)</div>
        </div>

        <div class="chart">
            <div class="bar" style="left:50px;height:45px;"></div>
            <div class="bar" style="left:85px;height:25px;"></div>
            <div class="bar" style="left:120px;height:70px;"></div>
            <div class="bar" style="left:155px;height:28px;"></div>
            <div class="bar" style="left:190px;height:72px;"></div>
            <div style="position:absolute;left:20px;top:20px;font-size:12px;">10</div>
            <div style="position:absolute;left:20px;top:62px;font-size:12px;">5</div>
            <div style="position:absolute;left:20px;top:96px;font-size:12px;">0</div>
            <div class="chart-title">Packet Loss (%)</div>
        </div>
    </div>

    <div class="stars">★ ★ ★</div>

    <div class="section">Employee of the Month Announcement</div>

    <div class="employee">
        <div class="avatar">👨‍💼</div>
        <div>
            <div class="emp-name">Ahmed Ali</div>
            <div class="emp-text">
                For your exceptional dedication and outstanding performance in improving network stability and customer service this month.
                Congratulations on this well-deserved recognition.
            </div>
        </div>
    </div>

    <div class="nav">
        <div><span>⌂</span>Home</div>
        <div><span>⇥</span>Logout</div>
        <div><span>☑</span>To Do List</div>
    </div>

</div>
</body>
</html>
""", height=850)
