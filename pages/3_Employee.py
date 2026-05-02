import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Employee Dashboard", layout="centered")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] { background:#eef2f7; }
.block-container { padding-top:10px; max-width:520px; }
header, footer { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
/* ✨ كروت قابلة للضغط */
.alert,
.chart,
.employee {
    cursor: pointer;
    transition: all 0.2s ease;
}

/* hover */
.alert:hover,
.chart:hover,
.employee:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,.15);
}

/* عند الضغط */
.alert:active,
.chart:active,
.employee:active {
    transform: scale(0.95);
    box-shadow: 0 4px 10px rgba(0,0,0,.2);
}
:root{
 --navy:#0f2446;
 --navy-light:#2f4f7c;
 --accent:#2f80ed;
}

*{box-sizing:border-box;font-family:Arial,sans-serif}
body{margin:0;background:transparent}

.phone{
 width:400px;height:790px;margin:auto;background:#fbfdff;border-radius:42px;
 padding:22px 18px 10px;box-shadow:0 8px 25px rgba(0,0,0,.25);
 border:1px solid #d9dee8;position:relative;overflow:hidden;
}

.page{height:690px;overflow-y:auto;padding-bottom:20px}
.top{display:grid;grid-template-columns:124px 1fr;gap:14px}

.rate-card{
 height:124px;background:white;border-radius:16px;display:flex;
 align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(0,0,0,.12)
}

.circle{
 width:100px;height:100px;border-radius:50%;border:10px solid var(--accent);
 display:flex;flex-direction:column;align-items:center;justify-content:center
}
.circle span{font-size:10px}
.circle b{font-size:25px}

.head{display:flex;justify-content:space-between;align-items:start;margin-bottom:10px}

.title{
 font-size:17px;
 font-weight:900;
 line-height:1.2;
 color:var(--navy);
}

.section{
 font-size:13px;
 font-weight:800;
 margin:14px 0 6px;
 color:var(--navy-light);
}

.location{
 font-size:11px;border:none;background:white;border-radius:8px;padding:7px;
 box-shadow:0 2px 8px rgba(0,0,0,.10);max-width:115px;
 color:var(--navy);font-weight:600;
}

.map{
 height:98px;background:#e6ecf5;border-radius:13px;position:relative;overflow:hidden;
 box-shadow:inset 0 0 0 1px #d7deea
}

.road{position:absolute;height:3px;width:240px;background:white;opacity:.9;transform:rotate(-35deg)}
.road2{position:absolute;height:3px;width:220px;background:white;opacity:.9;transform:rotate(35deg)}
.dot{position:absolute;color:#e02020;font-size:21px}

.alerts{display:grid;grid-template-columns:repeat(3,1fr);gap:9px}

.alert{
 background:white;border-radius:10px;overflow:hidden;min-height:118px;
 box-shadow:0 4px 14px rgba(0,0,0,.12);font-size:9.5px
}

.alert-head{color:white;padding:8px;font-weight:900;font-size:13px}
.red{background:#e94c4c}
.yellow{background:#f2b72f}
.blue{background:#2f80ed}

.alert-body{padding:8px;line-height:1.35;color:#1f2937}

.metrics{display:grid;grid-template-columns:1fr 1fr;gap:13px}

.chart{
 height:145px;background:white;border-radius:14px;
 box-shadow:0 4px 14px rgba(0,0,0,.10);position:relative;overflow:hidden
}

.chart-title{
 position:absolute;bottom:29px;left:0;width:100%;text-align:center;font-size:12px
}

.chart-stars{
 position:absolute;bottom:8px;left:0;width:100%;text-align:center;color:#1267c9;font-size:18px
}

.line{position:absolute;left:35px;bottom:55px;width:130px;height:62px}
.bar{position:absolute;bottom:55px;width:19px;background:#2f80ed}

.employee{
 background:white;border-radius:14px;padding:11px;display:flex;gap:12px;align-items:center;
 box-shadow:0 4px 14px rgba(0,0,0,.10)
}

.avatar{
 width:58px;height:58px;border-radius:50%;background:#dbeafe;
 display:flex;align-items:center;justify-content:center;font-size:30px
}

.emp-name{font-size:15px;font-weight:900;color:var(--navy)}
.emp-text{font-size:10px;line-height:1.25;color:#1f2937}

/* NAV */
.nav{
 position:absolute;
 bottom:0;
 left:18px;
 right:18px;
 height:76px;
 border-top:1px solid #e5e7eb;
 background:rgba(255,255,255,.9);
 backdrop-filter:blur(10px);
 display:flex;
 justify-content:space-around;
 align-items:center;
 border-radius:0 0 32px 32px;
}

.nav form{margin:0;width:32%}

.nav button{
 width:100%;
 background:transparent;
 border:none;
 font-weight:900;
 font-size:13px;
 cursor:pointer;
 color:#111827;
 padding:6px 0;
 border-radius:16px;
 transition:.25s;
}

.nav button:hover{
 background:#eef6ff;
 color:var(--accent);
 transform:translateY(-3px);
}

.nav span{
 display:block;
 font-size:25px;
 color:#376f91;
 margin-bottom:2px;
}

.nav button:hover span{color:var(--accent)}
.nav .active-nav{color:var(--accent);background:#eef6ff}
</style>
</head>
<script>
const alerts = document.querySelectorAll(".alert");

alerts.forEach((card, index) => {
    card.addEventListener("click", () => {
        if(index === 0){
            alert("🚨 Problem selected");
        } else if(index === 1){
            alert("⚠️ Internal issue");
        } else {
            alert("🌐 External issue");
        }
    });
});

const charts = document.querySelectorAll(".chart");

charts.forEach((c, i) => {
    c.addEventListener("click", () => {
        alert(i === 0 ? "Latency details 📊" : "Packet Loss details 📊");
    });
});

const employee = document.querySelector(".employee");

employee.addEventListener("click", () => {
    alert("👨‍💼 Employee Details: Ahmed Ali");
});
</script>
<body>
<div class="phone">

<div id="homePage" class="page">
    <div class="top">
        <div class="rate-card">
            <div class="circle">
                <span>Problem Rate:</span>
                <b>4.5%</b>
            </div>
        </div>

        <div>
            <div class="head">
                <div class="title">Network<br>Issues</div>

                <select class="location" id="region" onchange="updateRegion()">
                    <option value="Amman">📍 Amman</option>
                    <option value="Zarqa">📍 Zarqa</option>
                    <option value="Irbid">📍 Irbid</option>
                    <option value="Balqa">📍 Balqa</option>
                    <option value="Mafraq">📍 Mafraq</option>
                    <option value="Jerash">📍 Jerash</option>
                    <option value="Ajloun">📍 Ajloun</option>
                    <option value="Madaba">📍 Madaba</option>
                    <option value="Karak">📍 Karak</option>
                    <option value="Tafilah">📍 Tafilah</option>
                    <option value="Ma'an">📍 Ma'an</option>
                    <option value="Aqaba">📍 Aqaba</option>
                </select>
            </div>

            <div class="map">
                <div class="road" style="top:8px;left:-65px;"></div>
                <div class="road" style="top:32px;left:-40px;"></div>
                <div class="road" style="top:60px;left:-65px;"></div>
                <div class="road" style="top:86px;left:-25px;"></div>
                <div class="road2" style="top:18px;left:48px;"></div>
                <div class="road2" style="top:55px;left:70px;"></div>
                <div class="road2" style="top:90px;left:90px;"></div>
                <div class="dot" style="top:22px;left:78px;">●</div>
                <div class="dot" style="top:44px;left:138px;">●</div>
                <div class="dot" style="top:67px;left:148px;">●</div>
                <div class="dot" style="top:13px;left:182px;font-size:13px;">●</div>
            </div>
        </div>
    </div>

    <div class="section">Alert History & Problems</div>

    <div class="alerts">
        <div class="alert">
            <div class="alert-head red">❗ Problem</div>
            <div class="alert-body">
                <b>Region:</b> <span class="region-name">Amman</span>: Multiple User Reports 09:30 AM of Slow Internet.
            </div>
        </div>

        <div class="alert">
            <div class="alert-head yellow">⚠️ Internal</div>
            <div class="alert-body">
                <b>Region:</b> <span class="region-name">Amman</span>: Multiple User Reports 09:30 AM of Slow Internet.
            </div>
        </div>

        <div class="alert">
            <div class="alert-head blue">↗ External</div>
            <div class="alert-body">
                <b>Region:</b> <span class="region-name">Amman</span> This Internet issue is external. The problem is reported by the ISP.
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
            <div style="position:absolute;left:15px;top:25px;font-size:12px;">20</div>
            <div style="position:absolute;left:15px;top:63px;font-size:12px;">10</div>
            <div style="position:absolute;left:15px;top:101px;font-size:12px;">0</div>
            <div class="chart-title">Avg Latency (ms)</div>
        </div>

        <div class="chart">
            <div class="bar" style="left:45px;height:43px;"></div>
            <div class="bar" style="left:76px;height:28px;"></div>
            <div class="bar" style="left:107px;height:70px;"></div>
            <div class="bar" style="left:138px;height:31px;"></div>
            <div style="position:absolute;left:18px;top:25px;font-size:12px;">10</div>
            <div style="position:absolute;left:18px;top:66px;font-size:12px;">5</div>
            <div style="position:absolute;left:18px;top:101px;font-size:12px;">0</div>
            <div class="chart-title">Packet Loss (%)</div>
            <div class="chart-stars">★ ★ ★</div>
        </div>
    </div>

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
</div>


</div>

<script>
function updateRegion(){
    const selected = document.getElementById("region").value;
    const regions = document.getElementsByClassName("region-name");

    for(let i=0;i<regions.length;i++){
        regions[i].innerText = selected;
    }
}
</script>

</body>
</html>
""", height=820)
st.markdown("""
<style>
div[data-testid="column"] .stButton > button {
    width: 100%;
    height: 62px;
    border-radius: 18px;
    border: none;
    background: white;
    color: #111827;
    font-weight: 900;
    box-shadow: 0 3px 10px rgba(0,0,0,.08);
}

div[data-testid="column"]:first-child .stButton > button {
    background: #eef6ff;
    color: #2f80ed;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⌂\nHome"):
        st.switch_page("pages/3_Employee.py")

with col2:
    if st.button("⇥\nLogout"):
        st.switch_page("app.py")

with col3:
    if st.button("☑\nTo Do List"):
        st.switch_page("pages/4_To_Do.py")
