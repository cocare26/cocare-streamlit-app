
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="قائمة المهام", layout="centered")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] { background:#eef2f7; }
.block-container { padding-top:10px; max-width:520px; }
header, footer { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html dir="rtl">
<head>
<style>

:root{
 --navy:#0f2446;
 --accent:#2f80ed;
}

*{box-sizing:border-box;font-family:Arial}
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
 text-align:right;
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
}

.add-btn{
 background:linear-gradient(90deg,#2f80ed,#1c6fa4);
 color:white;
}

.hidden-toggle-btn{
 background:white;
 color:var(--navy);
}

.empty{
 text-align:center;
 margin-top:80px;
 color:#6b7280;
 opacity:.6;
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

.nav{
 position:absolute;
 bottom:0;
 left:18px;
 right:18px;
 height:76px;
 display:flex;
 justify-content:space-around;
 align-items:center;
}

.nav form{width:32%}

.nav button{
 width:100%;
 border:none;
 font-weight:900;
 cursor:pointer;
 background:white;
 border-radius:16px;
}

</style>
</head>

<body>

<div class="phone">

<div class="page">

<div class="todo-title">📋 قائمة المهام</div>

<input class="task-input" id="taskInput" placeholder="أضف مهمة جديدة..." />

<div class="todo-grid">
    <input type="date" id="taskDate">
    <input type="time" id="taskTime">

    <select id="difficulty">
        <option value="Low">🟢 سهل</option>
        <option value="Medium">🟡 متوسط</option>
        <option value="High">🔴 صعب</option>
    </select>

    <select id="status">
        <option value="Pending">⏳ قيد الانتظار</option>
        <option value="In Progress">🔄 قيد التنفيذ</option>
        <option value="Done">✅ مكتمل</option>
    </select>
</div>

<button class="add-btn" onclick="addTask()">إضافة مهمة</button>
<button class="hidden-toggle-btn" onclick="toggleHiddenSection()">إظهار / إخفاء المهام المخفية</button>

<div id="emptyBox" class="empty">
    <p>لا توجد مهام حالياً</p>
</div>

<div id="taskList"></div>

<div id="hiddenSection" style="display:none;">
    <div class="section-title">المهام المخفية</div>
    <div id="hiddenList"></div>
</div>

</div>

<!-- NAV -->
<div class="nav">
<form action="/" method="get" target="_top">
<input type="hidden" name="page" value="employee">
<button>🏠 الرئيسية</button>
</form>

<form action="/" method="get" target="_top">
<button>🚪 خروج</button>
</form>

<form action="/" method="get" target="_top">
<input type="hidden" name="page" value="todo">
<button>☑ المهام</button>
</form>
</div>

</div>

<script>
function addTask(){
    const task = document.getElementById("taskInput").value.trim();
    if(task === ""){
        alert("اكتب مهمة أولاً");
        return;
    }

    const card = document.createElement("div");
    card.className = "task-card";
    card.innerHTML = `<div class="task-title">${task}</div>`;

    document.getElementById("taskList").prepend(card);
    document.getElementById("taskInput").value = "";
}
</script>

</body>
</html>
""", height=820)
