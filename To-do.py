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
 height:690px;
 overflow-y:auto;
 padding-bottom:20px;
}

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

.add-btn,
.hidden-toggle-btn{
 width:100%;
 height:40px;
 border:none;
 border-radius:9px;
 font-weight:900;
 cursor:pointer;
 margin-bottom:10px;
}

.add-btn{
 background:#2f80ed;
 color:white;
}

.hidden-toggle-btn{
 background:#eef2ff;
 color:#1d4ed8;
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

.section-title{
 font-size:14px;
 font-weight:900;
 margin:14px 0 8px;
 color:#374151;
}

.task-card{
 background:white;
 border-radius:12px;
 padding:10px;
 margin-bottom:10px;
 box-shadow:0 3px 10px rgba(0,0,0,.10);
 font-size:12px;
}

.hidden-card{
 opacity:.65;
 background:#f8fafc;
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
 margin-bottom:8px;
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
 padding:6px 10px;
 font-size:11px;
 font-weight:800;
 cursor:pointer;
}

.hide-btn{
 background:#e0e7ff;
 color:#1d4ed8;
}

.restore-btn{
 background:#d1fae5;
 color:#047857;
}

.delete-btn{
 background:#fee2e2;
 color:#b91c1c;
}

#hiddenSection{
 display:none;
}

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
        <div id="hiddenEmpty" class="empty" style="margin-top:20px;">
            <p>No hidden tasks</p>
        </div>
        <div id="hiddenList"></div>
    </div>
</div>

<div class="nav">
    <button onclick="goHome()"><span>⌂</span>Home</button>
    <button onclick="logoutToLogin()"><span>⇥</span>Logout</button>
    <button><span>☑</span>To Do List</button>
</div>

</div>

<script>
function goHome(){
    window.top.location.href = "/?page=employee";
}

function logoutToLogin(){
    window.top.location.href = "/";
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
    const activeTasks = document.querySelectorAll("#taskList .task-card");
    const hiddenTasks = document.querySelectorAll("#hiddenList .task-card");

    document.getElementById("emptyBox").style.display =
        activeTasks.length === 0 ? "block" : "none";

    document.getElementById("hiddenEmpty").style.display =
        hiddenTasks.length === 0 ? "block" : "none";
}
</script>

</body>
</html>
""", height=820)
