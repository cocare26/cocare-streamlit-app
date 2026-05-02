import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="To-Do List", layout="centered")

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
:root{
 --navy:#0f2446;
 --accent:#2f80ed;
}

*{box-sizing:border-box;font-family:Arial,sans-serif}
body{margin:0;background:transparent}

.phone{
 width:400px;
 height:790px;
 margin:auto;
 background:linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
 border-radius:42px;
 padding:22px 18px 10px;
 box-shadow:0 8px 25px rgba(0,0,0,.25);
 position:relative;
 overflow:hidden;
}

.page{
 height:690px;
 overflow-y:auto;
 padding-bottom:90px;
}

.todo-title{
 text-align:center;
 font-size:20px;
 font-weight:900;
 margin-bottom:14px;
 color:var(--navy);
}

.task-input{
 width:100%;
 padding:12px;
 border:none;
 border-radius:25px;
 font-size:14px;
 margin-bottom:10px;
 background:white;
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
 border:none;
 border-radius:20px;
 background:white;
 padding:6px;
 font-size:12px;
}

.add-btn,
.hidden-toggle-btn{
 width:100%;
 height:42px;
 border:none;
 border-radius:25px;
 font-weight:900;
 cursor:pointer;
 margin-bottom:10px;
 transition:.2s;
}

.add-btn{
 background:linear-gradient(90deg,#2f80ed,#1c6fa4);
 color:white;
}

.hidden-toggle-btn{
 background:white;
 color:var(--navy);
}

.add-btn:hover,
.hidden-toggle-btn:hover{
 transform:translateY(-2px);
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
}

.section-title{
 font-size:14px;
 font-weight:900;
 margin:14px 0 8px;
 color:var(--navy);
}

.task-card{
 background:white;
 border-radius:16px;
 padding:10px;
 margin-bottom:10px;
 box-shadow:0 4px 12px rgba(0,0,0,.12);
 font-size:12px;
 transition:.2s;
}

.task-card:hover{
 transform:translateY(-3px);
}

.hidden-card{
 opacity:.6;
 background:#f8fafc;
}

.task-title{
 font-weight:900;
 font-size:14px;
 margin-bottom:5px;
 color:var(--navy);
}

.badges{
 display:flex;
 flex-wrap:wrap;
 gap:5px;
 margin-bottom:8px;
}

.badge{
 padding:4px 7px;
 border-radius:10px;
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
 border-radius:10px;
 padding:6px 10px;
 font-size:11px;
 font-weight:800;
 cursor:pointer;
}

.hide-btn{background:#e0e7ff;}
.restore-btn{background:#d1fae5;}
.delete-btn{background:#fee2e2;}

#hiddenSection{display:none;}

/* Bottom Nav */
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

.nav form{
 margin:0;
 width:32%;
}

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

.nav button:hover span{
 color:var(--accent);
}

.nav .active-nav{
 color:var(--accent);
 background:#eef6ff;
}
</style>
</head>

<body>
<div class="phone">

<div class="page">
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
    <button class="hidden-toggle-btn" onclick="toggleHiddenSection()">Show / Hide Hidden Tasks</button>

    <div id="emptyBox" class="empty">
        <div class="clipboard">✔</div>
        <p>No tasks added yet</p>
    </div>

    <div id="taskList"></div>

    <div id="hiddenSection">
        <div class="section-title">Hidden Tasks</div>
        <div id="hiddenEmpty" class="empty">
            <p>No hidden tasks</p>
        </div>
        <div id="hiddenList"></div>
    </div>
</div>

<div class="nav">
    <form action="/" method="get" target="_top">
        <input type="hidden" name="page" value="employee">
        <button type="submit"><span>⌂</span>Home</button>
    </form>

    <form action="/" method="get" target="_top">
        <button type="submit"><span>⇥</span>Logout</button>
    </form>

    <form action="/" method="get" target="_top">
        <input type="hidden" name="page" value="todo">
        <button type="submit" class="active-nav"><span>☑</span>To Do List</button>
    </form>
</div>

</div>

<script>
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

    let diffClass = difficulty === "Medium" ? "medium" : difficulty === "High" ? "high" : "low";
    let statusClass = status === "Done" ? "done" : status === "In Progress" ? "progress" : "pending";

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
        <div class="task-actions">
            <button class="hide-btn" onclick="hideTask(this)">Hide</button>
            <button class="delete-btn" onclick="deleteTask(this)">Delete</button>
        </div>
    `;

    document.getElementById("taskList").prepend(card);
    document.getElementById("taskInput").value = "";
    document.getElementById("taskDate").value = "";
    document.getElementById("taskTime").value = "";

    checkEmpty();
}

function hideTask(btn){
    const card = btn.closest(".task-card");
    card.classList.add("hidden-card");

    const actions = card.querySelector(".task-actions");
    actions.innerHTML = `
        <button class="restore-btn" onclick="restoreTask(this)">Restore</button>
        <button class="delete-btn" onclick="deleteTask(this)">Delete</button>
    `;

    document.getElementById("hiddenList").prepend(card);
    document.getElementById("hiddenSection").style.display = "block";
    checkEmpty();
}

function restoreTask(btn){
    const card = btn.closest(".task-card");
    card.classList.remove("hidden-card");

    const actions = card.querySelector(".task-actions");
    actions.innerHTML = `
        <button class="hide-btn" onclick="hideTask(this)">Hide</button>
        <button class="delete-btn" onclick="deleteTask(this)">Delete</button>
    `;

    document.getElementById("taskList").prepend(card);
    checkEmpty();
}

function deleteTask(btn){
    btn.closest(".task-card").remove();
    checkEmpty();
}

function toggleHiddenSection(){
    const section = document.getElementById("hiddenSection");
    section.style.display = section.style.display === "none" || section.style.display === ""
        ? "block"
        : "none";
}

function checkEmpty(){
    const active = document.querySelectorAll("#taskList .task-card");
    const hidden = document.querySelectorAll("#hiddenList .task-card");

    document.getElementById("emptyBox").style.display = active.length === 0 ? "block" : "none";
    document.getElementById("hiddenEmpty").style.display = hidden.length === 0 ? "block" : "none";
}
</script>

</body>
</html>
""", height=820)
