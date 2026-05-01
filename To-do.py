import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CoCare", layout="centered")

components.html("""
<!DOCTYPE html>
<html>
<head>
<style>

body{margin:0;font-family:Arial;background:#eef2f7}

.phone{
 width:430px;margin:auto;background:#fbfdff;border-radius:45px;
 padding:20px;box-shadow:0 8px 25px rgba(0,0,0,.25);
}

.page{display:none}
.page.active{display:block}

/* TODO */
.todo-title{
 text-align:center;font-size:18px;font-weight:800;margin-bottom:15px
}

.task-input{
 width:100%;padding:12px;border:1px solid #ccc;
 border-radius:10px;margin-bottom:10px
}

.todo-row{
 display:grid;grid-template-columns:1fr 1fr 1fr 70px;
 gap:5px;margin-bottom:15px
}

.todo-row select,.todo-row button{
 height:36px;border-radius:6px;border:1px solid #ccc
}

.todo-row button{
 background:#2f80ed;color:white;font-weight:bold;border:none
}

/* 🔥 EMPTY BOX */
.empty{
 text-align:center;
 margin-top:70px;
 color:#6b7280;
 opacity:0.6;   /* 👈 60% */
}

.clipboard{
 width:65px;      /* 👈 أصغر */
 height:65px;
 border-radius:12px;
 background:#eef6ff;
 margin:auto;
 display:flex;
 align-items:center;
 justify-content:center;
 font-size:35px;  /* 👈 أصغر */
 box-shadow:0 4px 12px rgba(0,0,0,.1);
}

.task-card{
 background:white;border-radius:12px;padding:10px;
 margin-bottom:10px;box-shadow:0 3px 10px rgba(0,0,0,.1)
}

/* NAV */
.nav{
 margin-top:20px;height:70px;
 border-top:1px solid #ddd;
 display:flex;justify-content:space-around;align-items:center;
}

.nav button{
 background:none;border:none;font-size:14px;font-weight:bold;cursor:pointer
}

.nav span{
 display:block;font-size:28px;color:#2f80ed
}

</style>
</head>

<body>

<div class="phone">

<!-- TODO PAGE -->
<div id="todoPage" class="page active">

    <div class="todo-title">To-Do List</div>

    <input class="task-input" id="taskInput" placeholder="Add a new task..." />

    <div class="todo-row">
        <select id="schedule">
            <option>📅 Schedule</option>
            <option>Today</option>
            <option>Tomorrow</option>
        </select>

        <select id="difficulty">
            <option>🔥 Difficulty</option>
            <option>Low</option>
            <option>Medium</option>
            <option>High</option>
        </select>

        <select id="status">
            <option>Status</option>
            <option>Pending</option>
            <option>Done</option>
        </select>

        <button onclick="addTask()">Add</button>
    </div>

    <!-- EMPTY STATE -->
    <div id="emptyBox" class="empty">
        <div class="clipboard">✔</div>
        <p>No tasks added yet</p>
    </div>

    <div id="taskList"></div>

</div>

<!-- NAV -->
<div class="nav">
    <button><span>⌂</span>Home</button>
    <button><span>⇥</span>Logout</button>
    <button><span>☑</span>To Do</button>
</div>

</div>

<script>
function addTask(){
    const task = document.getElementById("taskInput").value;

    if(task.trim() === ""){
        alert("Add task first");
        return;
    }

    document.getElementById("emptyBox").style.display = "none";

    const card = document.createElement("div");
    card.className = "task-card";
    card.innerHTML = "<b>"+task+"</b>";

    document.getElementById("taskList").appendChild(card);
    document.getElementById("taskInput").value = "";
}
</script>

</body>
</html>
""", height=700)
