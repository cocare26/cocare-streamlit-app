import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Employee Dashboard", layout="centered")

components.html("""
<!DOCTYPE html>
<html>
<head>
<style>

*{box-sizing:border-box;font-family:Arial,sans-serif}
body{margin:0;background:transparent}

/* 📱 PHONE */
.phone{
 width:390px;
 height:800px;
 margin:auto;
 background:#fbfdff;
 border-radius:40px;
 padding:18px;
 box-shadow:0 8px 25px rgba(0,0,0,.25);
 position:relative;
 overflow:hidden;
}

/* PAGES */
.page{display:none;height:690px;overflow-y:auto;padding-bottom:20px}
.page.active{display:block}

/* TITLE */
.title{
 font-size:18px;
 font-weight:800;
}
.section{
 font-size:14px;
 font-weight:800;
 margin:15px 0 8px;
}

/* TOP */
.top{
 display:grid;
 grid-template-columns:110px 1fr;
 gap:12px;
}

.rate-card{
 height:110px;
 background:white;
 border-radius:14px;
 display:flex;
 align-items:center;
 justify-content:center;
 box-shadow:0 3px 10px rgba(0,0,0,.1);
}

.circle{
 width:85px;height:85px;border-radius:50%;
 border:8px solid #2f80ed;
 display:flex;flex-direction:column;
 align-items:center;justify-content:center;
}
.circle span{font-size:9px}
.circle b{font-size:20px}

.map{
 height:90px;background:#e6ecf5;
 border-radius:12px;position:relative;
}

/* ALERT */
.alerts{
 display:grid;
 grid-template-columns:repeat(3,1fr);
 gap:6px;
}
.alert{
 background:white;border-radius:10px;
 box-shadow:0 3px 10px rgba(0,0,0,.1);
 font-size:10px;
}
.alert-head{
 color:white;padding:6px;font-weight:800;
}
.red{background:#e94c4c}
.yellow{background:#f2b72f}
.blue{background:#2f80ed}
.alert-body{padding:6px}

/* METRICS */
.metrics{
 display:grid;
 grid-template-columns:1fr 1fr;
 gap:10px;
}
.chart{
 height:130px;background:white;
 border-radius:12px;
 position:relative;
 box-shadow:0 3px 10px rgba(0,0,0,.1);
}
.chart-title{
 position:absolute;
 bottom:25px;
 width:100%;
 text-align:center;
 font-size:11px;
}
.chart-stars{
 position:absolute;
 bottom:5px;
 width:100%;
 text-align:center;
 color:#2f80ed;
}

/* EMPLOYEE */
.employee{
 display:flex;gap:10px;
 background:white;padding:8px;
 border-radius:12px;
 box-shadow:0 3px 10px rgba(0,0,0,.1);
}
.avatar{
 width:50px;height:50px;border-radius:50%;
 background:#dbeafe;
 display:flex;align-items:center;justify-content:center;
}
.emp-name{font-weight:800}
.emp-text{font-size:10px}

/* TODO */
.todo-title{
 text-align:center;font-size:16px;font-weight:800;
}
.task-input{
 width:100%;padding:8px;
 border-radius:8px;border:1px solid #ccc;
 margin-bottom:8px;
}
.todo-grid{
 display:grid;
 grid-template-columns:1fr 1fr;
 gap:6px;
 margin-bottom:8px;
}
.todo-grid input,.todo-grid select{
 height:32px;border-radius:6px;border:1px solid #ccc;
}
.add-btn{
 width:100%;height:36px;background:#2f80ed;
 color:white;border:none;border-radius:8px;font-weight:800;
 margin-bottom:10px;
}

.empty{
 text-align:center;margin-top:50px;
 opacity:.6;
}
.clipboard{
 width:50px;height:50px;border-radius:10px;
 background:#eef6ff;
 display:flex;align-items:center;justify-content:center;
 margin:auto;font-size:25px;
}

.task-card{
 background:white;border-radius:10px;
 padding:8px;margin-bottom:6px;
 box-shadow:0 2px 6px rgba(0,0,0,.1);
 font-size:11px;
}

/* NAV */
.nav{
 position:absolute;bottom:0;left:0;right:0;
 height:60px;
 display:flex;justify-content:space-around;
 align-items:center;
 border-top:1px solid #ddd;
 background:white;
}
.nav button{
 background:none;border:none;font-size:13px;font-weight:800;
}
.nav span{display:block;font-size:22px}

</style>
</head>

<body>

<div class="phone">

<!-- HOME -->
<div id="homePage" class="page active">

<div class="top">
<div class="rate-card">
<div class="circle">
<span>Problem Rate</span>
<b>4.5%</b>
</div>
</div>

<div>
<div class="title">Network Issues</div>
<div class="map"></div>
</div>
</div>

<div class="section">Alert History & Problems</div>

<div class="alerts">
<div class="alert">
<div class="alert-head red">Problem</div>
<div class="alert-body">Irbid issue</div>
</div>

<div class="alert">
<div class="alert-head yellow">Internal</div>
<div class="alert-body">Irbid issue</div>
</div>

<div class="alert">
<div class="alert-head blue">External</div>
<div class="alert-body">ISP issue</div>
</div>
</div>

<div class="section">Network Performance Metrics</div>

<div class="metrics">
<div class="chart">
<div class="chart-title">Latency</div>
</div>

<div class="chart">
<div class="chart-title">Packet Loss</div>
<div class="chart-stars">★ ★ ★</div>
</div>
</div>

<div class="section">Employee of the Month</div>

<div class="employee">
<div class="avatar">👨‍💼</div>
<div>
<div class="emp-name">Ahmed Ali</div>
<div class="emp-text">Great performance</div>
</div>
</div>

</div>

<!-- TODO -->
<div id="todoPage" class="page">

<div class="todo-title">To Do List</div>

<input id="taskInput" class="task-input" placeholder="Add task...">

<div class="todo-grid">
<input type="date" id="date">
<input type="time" id="time">

<select id="diff">
<option>Low</option>
<option>Medium</option>
<option>High</option>
</select>

<select id="status">
<option>Pending</option>
<option>Done</option>
</select>
</div>

<button class="add-btn" onclick="addTask()">Add</button>

<div id="empty" class="empty">
<div class="clipboard">✔</div>
<p>No tasks</p>
</div>

<div id="list"></div>

</div>

<!-- NAV -->
<div class="nav">
<button onclick="showPage('home')"><span>⌂</span>Home</button>
<button onclick="logout()"><span>⇥</span>Logout</button>
<button onclick="showPage('todo')"><span>☑</span>To Do</button>
</div>

</div>

<script>

function showPage(p){
document.getElementById("homePage").classList.remove("active");
document.getElementById("todoPage").classList.remove("active");

if(p==="home"){document.getElementById("homePage").classList.add("active");}
if(p==="todo"){document.getElementById("todoPage").classList.add("active");}
}

function logout(){
window.top.location.href="/";
}

function addTask(){
let t=document.getElementById("taskInput").value;
if(t==="") return;

document.getElementById("empty").style.display="none";

let card=document.createElement("div");
card.className="task-card";
card.innerHTML=t;

document.getElementById("list").appendChild(card);

document.getElementById("taskInput").value="";
}

</script>

</body>
</html>
""", height=820)
