import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CoCare", layout="centered")

components.html("""
<!DOCTYPE html>
<html>
<head>
<style>

body{
 margin:0;
 background:#eef2f7;
 display:flex;
 justify-content:center;
}

/* 📱 PHONE SIZE */
.phone{
 width:390px;
 height:820px;
 background:#fbfdff;
 border-radius:45px;
 padding:18px;
 box-shadow:0 8px 25px rgba(0,0,0,.25);
 overflow:hidden;
 position:relative;
}

/* PAGES */
.page{
 display:none;
 height:100%;
 overflow:auto;
 padding-bottom:80px;
}
.page.active{
 display:block;
}

/* ================= HOME ================= */
.top{
 display:flex;
 gap:10px;
}

.circle{
 width:95px;
 height:95px;
 border-radius:50%;
 border:10px solid #2f80ed;
 display:flex;
 align-items:center;
 justify-content:center;
 font-weight:bold;
}

.map{
 flex:1;
 height:95px;
 background:#e6ecf5;
 border-radius:12px;
 position:relative;
}

.dot{
 position:absolute;
 color:red;
}

/* ================= TODO ================= */
.todo-title{
 text-align:center;
 font-size:18px;
 font-weight:bold;
 margin-bottom:10px;
}

.task-input{
 width:100%;
 padding:10px;
 border-radius:8px;
 border:1px solid #ccc;
 margin-bottom:10px;
}

.todo-row{
 display:grid;
 grid-template-columns:1fr 1fr 1fr 60px;
 gap:5px;
 margin-bottom:10px;
}

.todo-row select,.todo-row button{
 height:34px;
 border-radius:6px;
 border:1px solid #ccc;
}

.todo-row button{
 background:#2f80ed;
 color:white;
 border:none;
}

.empty{
 text-align:center;
 margin-top:60px;
 color:#6b7280;
 opacity:0.6;
}

.clipboard{
 width:60px;
 height:60px;
 border-radius:12px;
 background:#eef6ff;
 margin:auto;
 display:flex;
 align-items:center;
 justify-content:center;
 font-size:30px;
}

.task-card{
 background:white;
 padding:10px;
 border-radius:10px;
 margin-bottom:10px;
 box-shadow:0 3px 10px rgba(0,0,0,.1);
}

/* ================= NAV ================= */
.nav{
 position:absolute;
 bottom:0;
 left:0;
 right:0;
 height:70px;
 border-top:1px solid #ddd;
 display:flex;
 justify-content:space-around;
 align-items:center;
 background:white;
}

.nav button{
 background:none;
 border:none;
 font-weight:bold;
 cursor:pointer;
}

.nav span{
 display:block;
 font-size:28px;
 color:#2f80ed;
}

</style>
</head>

<body>

<div class="phone">

<!-- ================= HOME PAGE ================= -->
<div id="homePage" class="page active">

<div class="top">
    <div class="circle">4.5%</div>

    <div class="map">
        <div class="dot" style="top:20px;left:50px;">●</div>
        <div class="dot" style="top:40px;left:100px;">●</div>
    </div>
</div>

<h3>Network Issues</h3>

<p>Welcome to CoCare Dashboard 🚀</p>

</div>

<!-- ================= TODO PAGE ================= -->
<div id="todoPage" class="page">

<div class="todo-title">To-Do List</div>

<input class="task-input" id="taskInput" placeholder="Add a new task..." />

<div class="todo-row">
<select><option>📅</option></select>
<select><option>🔥</option></select>
<select><option>🚩</option></select>
<button onclick="addTask()">Add</button>
</div>

<div id="emptyBox" class="empty">
<div class="clipboard">✔</div>
<p>No tasks added yet</p>
</div>

<div id="taskList"></div>

</div>

<!-- ================= NAV ================= -->
<div class="nav">
<button onclick="showPage('home')"><span>⌂</span>Home</button>
<button onclick="showPage('todo')"><span>☑</span>To Do</button>
</div>

</div>

<script>

function showPage(page){
 document.getElementById("homePage").classList.remove("active");
 document.getElementById("todoPage").classList.remove("active");

 if(page==="home"){
   document.getElementById("homePage").classList.add("active");
 }
 if(page==="todo"){
   document.getElementById("todoPage").classList.add("active");
 }
}

function addTask(){
 let task=document.getElementById("taskInput").value;

 if(task===""){
  alert("Add task first");
  return;
 }

 document.getElementById("emptyBox").style.display="none";

 let card=document.createElement("div");
 card.className="task-card";
 card.innerHTML=task;

 document.getElementById("taskList").appendChild(card);

 document.getElementById("taskInput").value="";
}

</script>

</body>
</html>
""", height=850)
