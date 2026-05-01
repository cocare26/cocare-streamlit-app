import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CoCare", layout="centered")

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
*{box-sizing:border-box;font-family:Arial,sans-serif}
body{margin:0;background:transparent}

.phone{
 width:400px;
 height:790px;
 margin:auto;
 background:#fbfdff;
 border-radius:42px;
 padding:22px 18px 10px;
 box-shadow:0 8px 25px rgba(0,0,0,.25);
 border:1px solid #d9dee8;
 position:relative;
 overflow:hidden;
}

.page{
 display:none;
 height:690px;
 overflow-y:auto;
 padding-bottom:20px;
}
.page.active{display:block}

.top{
 display:grid;
 grid-template-columns:124px 1fr;
 gap:14px;
 align-items:start;
}

.rate-card{
 height:124px;
 background:white;
 border-radius:16px;
 display:flex;
 align-items:center;
 justify-content:center;
 box-shadow:0 4px 14px rgba(0,0,0,.12);
}

.circle{
 width:100px;
 height:100px;
 border-radius:50%;
 border:10px solid #2f80ed;
 display:flex;
 flex-direction:column;
 align-items:center;
 justify-content:center;
}
.circle span{font-size:10px}
.circle b{font-size:25px}

.head{
 display:flex;
 justify-content:space-between;
 align-items:start;
 margin-bottom:10px;
}
.title{
 font-size:23px;
 font-weight:900;
 line-height:1.2;
}
.location{
 font-size:11px;
 border:none;
 background:white;
 border-radius:8px;
 padding:7px;
 box-shadow:0 2px 8px rgba(0,0,0,.10);
}

.map{
 height:98px;
 background:#e6ecf5;
 border-radius:13px;
 position:relative;
 overflow:hidden;
 box-shadow:inset 0 0 0 1px #d7deea;
}
.road{
 position:absolute;
 height:3px;
 width:240px;
 background:white;
 opacity:.9;
 transform:rotate(-35deg);
}
.road2{
 position:absolute;
 height:3px;
 width:220px;
 background:white;
 opacity:.9;
 transform:rotate(35deg);
}
.dot{
 position:absolute;
 color:#e02020;
 font-size:21px;
}

.section{
 font-size:18px;
 font-weight:900;
 margin:20px 0 10px;
}

.alerts{
 display:grid;
 grid-template-columns:repeat(3,1fr);
 gap:9px;
}
.alert{
 background:white;
 border-radius:10px;
 overflow:hidden;
 min-height:118px;
 box-shadow:0 4px 14px rgba(0,0,0,.12);
 font-size:10.5px;
}
.alert-head{
 color:white;
 padding:8px;
 font-weight:900;
 font-size:14px;
}
.red{background:#e94c4c}
.yellow{background:#f2b72f}
.blue{background:#2f80ed}
.alert-body{
 padding:8px;
 line-height:1.35;
}

.metrics{
 display:grid;
 grid-template-columns:1fr 1fr;
 gap:13px;
}
.chart{
 height:145px;
 background:white;
 border-radius:14px;
 box-shadow:0 4px 14px rgba(0,0,0,.10);
 position:relative;
 overflow:hidden;
}
.chart-title{
 position:absolute;
 bottom:29px;
 left:0;
 width:100%;
 text-align:center;
 font-size:13px;
}
.chart-stars{
 position:absolute;
 bottom:8px;
 left:0;
 width:100%;
 text-align:center;
 color:#1267c9;
 font-size:18px;
}
.line{
 position:absolute;
 left:35px;
 bottom:55px;
 width:130px;
 height:62px;
}
.bar{
 position:absolute;
 bottom:55px;
 width:19px;
 background:#2f80ed;
}

.employee{
 background:white;
 border-radius:14px;
 padding:11px;
 display:flex;
 gap:12px;
 align-items:center;
 box-shadow:0 4px 14px rgba(0,0,0,.10);
}
.avatar{
 width:58px;
 height:58px;
 border-radius:50%;
 background:#dbeafe;
 display:flex;
 align-items:center;
 justify-content:center;
 font-size:30px;
}
.emp-name{font-size:19px;font-weight:900}
.emp-text{font-size:10.5px;line-height:1.25}

/* TO DO */
.todo-title{
 text-align:center;
 font-size:20px;
 font-weight:900;
 margin-bottom:14px;
}
.task-input{
 width:100%;
 padding:12px;
 border:1px solid #d1d5db;
 border-radius:10px;
 font-size:14px;
 margin-bottom:10px;
}
.todo-grid{
 display:grid;
 grid-template-columns:1fr 1fr;
 gap:8px;
 margin-bottom:10px;
}
.todo-grid select,
.todo-grid input{
 width:100%;
 height:38px;
 border:1px solid #d1d5db;
 border-radius:8px;
 background:white;
 padding:6px;
 font-size:12px;
}
.add-btn{
 width:100%;
 height:40px;
 background:#2f80ed;
 color:white;
 border:none;
 border-radius:9px;
 font-weight:900;
 cursor:pointer;
 margin-bottom:16px;
}
.empty{
 text-align:center;
 margin-top:80px;
 color:#6b7280;
 opacity:.6;
}
.clipboard{
 width:62px;
 height:62px;
 border-radius:14px;
 background:#eef6ff;
 margin:auto;
 display:flex;
 align-items:center;
 justify-content:center;
 font-size:32px;
 box-shadow:0 4px 12px rgba(0,0,0,.10);
}
.task-card{
 background:white;
 border-radius:12px;
 padding:10px;
 margin-bottom:10px;
 box-shadow:0 3px 10px rgba(0,0,0,.10);
 font-size:12px;
}
.task-title{
 font-weight:900;
 font-size:14px;
 margin-bottom:5px;
}
.badges{
 display:flex;
 flex-wrap:wrap;
 gap:5px;
}
.badge{
 padding:4px 7px;
 border-radius:7px;
 background:#eef2ff;
 font-size:11px;
}
.low{background:#dbeafe}
.medium{background:#fff3bf}
.high{background:#ffd6d6}
.done{background:#d1fae5}
.pending{background:#fee2e2}
.progress{background:#e0e7ff}

.task-actions{
 display:flex;
 gap:6px;
 margin-top:8px;
}

.task-actions button{
 border:none;
 border-radius:7px;
 padding:6px 8px;
 font-size:11px;
 font-weight:800;
 cursor:pointer;
}

.hide-btn{
 background:#e0e7ff;
 color:#1d4ed8;
}

.delete-btn{
 background:#fee2e2;
 color:#b91c1c;
}

/* NAV */
.nav{
 position:absolute;
 bottom:0;
 left:18px;
 right:18px;
 height:70px;
 border-top:1px solid #e5e7eb;
 background:#fbfdff;
 display:flex;
 justify-content:space-around;
 align-items:center;
}
.nav button{
 background:none;
 border:none;
 font-weight:900;
 font-size:14px;
 cursor:pointer;
 color:#111827;
}
.nav span{
 display:block;
 font-size:27px;
 color:#376f91;
}
.nav .active-nav{
 color:#2f80ed;
}
</style>
</head>

<body>
<div class="phone">

<div id="homePage" class="page active">
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
                    <option value="Irbid">📍 Irbid</option>
                    <option value="Amman">📍 Amman</option>
                    <option value="Zarqa">📍 Zarqa</option>
                    <option value="Balqa">📍 Balqa</option>
                    <option value="Aqaba">📍 Aqaba</option>
                    <option value="Karak">📍 Karak</option>
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
            <div class="alert-body"><b>Region:</b> <span class="region-name">Irbid</span>: Multiple User Reports 09:30 AM of Slow Internet.</div>
        </div>
        <div class="alert">
            <div class="alert-head yellow">⚠️ Internal</div>
            <div class="alert-body"><b>Region:</b> <span class="region-name">Irbid</span>: Multiple User Reports 09:30 AM of Slow Internet.</div>
        </div>
        <div class="alert">
            <div class="alert-head blue">↗ External</div>
            <div class="alert-body"><b>Region:</b> <span class="region-name">Irbid</span> This Internet issue is external. The problem is reported by the ISP.</div>
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
            <div class="emp-text">For your exceptional dedication and outstanding performance in improving network stability and customer service this month. Congratulations on this well-deserved recognition.</div>
        </div>
    </div>
</div>

<div id="todoPage" class="page">
    <div class="todo-title">To-Do List</div>

    <input class="task-input" id="taskInput" placeholder="Add a new task..." />

    <div class="todo-grid">
        <input type="date" id="taskDate">
        <input type="time" id="taskTime">

        <select id="difficulty">
            <option value="Low">🔵 Low</option>
            <option value="Medium">🟡 Medium</option>
            <option value="High">🔴 High</option>
        </select>

        <select id="status">
            <option value="Pending">🚩 Pending</option>
            <option value="In Progress">🔄 In Progress</option>
            <option value="Done">✅ Done</option>
        </select>
    </div>

    <button class="add-btn" onclick="addTask()">Add Task</button>

    <div id="emptyBox" class="empty">
        <div class="clipboard">✔</div>
        <p>No tasks added yet</p>
    </div>

    <div id="taskList"></div>
</div>

<div id="logoutPage" class="page">
    <div style="text-align:center;margin-top:260px;">
        <h2>Logout</h2>
        <p>You have been logged out successfully.</p>
    </div>
</div>

<div class="nav">
    <button id="homeBtn" class="active-nav" onclick="showPage('home')"><span>⌂</span>Home</button>
    <button id="logoutBtn" onclick="showPage('logout')"><span>⇥</span>Logout</button>
    <button id="todoBtn" onclick="showPage('todo')"><span>☑</span>To Do List</button>
</div>

</div>

<script>
function showPage(page){
    document.getElementById("homePage").classList.remove("active");
    document.getElementById("todoPage").classList.remove("active");
    document.getElementById("logoutPage").classList.remove("active");

    document.getElementById("homeBtn").classList.remove("active-nav");
    document.getElementById("todoBtn").classList.remove("active-nav");
    document.getElementById("logoutBtn").classList.remove("active-nav");

    if(page==="home"){
        document.getElementById("homePage").classList.add("active");
        document.getElementById("homeBtn").classList.add("active-nav");
    }
    if(page==="todo"){
        document.getElementById("todoPage").classList.add("active");
        document.getElementById("todoBtn").classList.add("active-nav");
    }
    if(page==="logout"){
        document.getElementById("logoutPage").classList.add("active");
        document.getElementById("logoutBtn").classList.add("active-nav");
    }
}

function updateRegion(){
    const selected = document.getElementById("region").value;
    const regions = document.getElementsByClassName("region-name");
    for(let i=0;i<regions.length;i++){
        regions[i].innerText = selected;
    }
}

function addTask(){
    const task = document.getElementById("taskInput").value.trim();
    const date = document.getElementById("taskDate").value;
    const time = document.getElementById("taskTime").value;
    const difficulty = document.getElementById("difficulty").value;
    const status = document.getElementById("status").value;

    if(task === ""){
        alert("Please add a task first");
        return;
    }

    document.getElementById("emptyBox").style.display = "none";

    let diffClass = "low";
    if(difficulty === "Medium") diffClass = "medium";
    if(difficulty === "High") diffClass = "high";

    let statusClass = "pending";
    if(status === "In Progress") statusClass = "progress";
    if(status === "Done") statusClass = "done";

    const card = document.createElement("div");
    card.className = "task-card";
  card.innerHTML = `
    <div class="task-title">${task}</div>
    <div class="badges">
        <span class="badge">📅 ${date || "No date"}</span>
        <span class="badge">⏰ ${time || "No time"}</span>
        <span class="badge ${diffClass}">${difficulty}</span>
        <span class="badge ${statusClass}">${status}</span>
    </div>
`;

    document.getElementById("taskList").prepend(card);

    document.getElementById("taskInput").value = "";
    document.getElementById("taskDate").value = "";
    document.getElementById("taskTime").value = "";
}
</script>

</body>
</html>
""", height=820)
