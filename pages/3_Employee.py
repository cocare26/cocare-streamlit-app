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

:root{
 --navy:#0f2446;
 --navy-light:#2f4f7c;
 --accent:#2f80ed;
}

*{box-sizing:border-box;font-family:Arial}
body{margin:0}

.phone{
 width:400px;height:790px;margin:auto;background:#fbfdff;
 border-radius:42px;padding:22px 18px 10px;
 box-shadow:0 8px 25px rgba(0,0,0,.25);
 border:1px solid #d9dee8;position:relative;overflow:hidden;
}

.page{height:690px;overflow-y:auto}

/* ===== TITLES ===== */
h3{
 text-align:center;
 color:var(--navy);
 font-size:20px;
 font-weight:900;
}

.title{
 color:var(--navy);
 font-size:18px;
 font-weight:900;
}

.section{
 color:var(--navy-light);
 font-size:13px;
 font-weight:800;
 margin:14px 0 6px;
}

/* ===== RATE ===== */
.top{display:grid;grid-template-columns:124px 1fr;gap:14px}

.rate-card{
 height:124px;background:white;border-radius:16px;
 display:flex;align-items:center;justify-content:center;
 box-shadow:0 4px 14px rgba(0,0,0,.12)
}

.circle{
 width:100px;height:100px;border-radius:50%;
 border:10px solid var(--accent);
 display:flex;flex-direction:column;align-items:center;justify-content:center
}

/* ===== ALERTS ===== */
.alerts{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}

.alert{
 background:white;
 border-radius:12px;
 overflow:hidden;
 box-shadow:0 6px 16px rgba(0,0,0,.12);
 font-size:10px;
 transition:.2s;
}

.alert:hover{transform:translateY(-3px)}

.alert-head{
 color:white;
 padding:8px;
 font-weight:800;
 font-size:12px;
 border-radius:12px 12px 0 0;
}

.red{background:#e54848;}
.yellow{background:#f2b72f;}
.blue{background:#2f80ed;}

.alert-body{
 padding:8px;
 color:#1f2937;
}

/* ===== NAV ===== */
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

.nav form{width:32%}

.nav button{
 width:100%;
 background:transparent;
 border:none;
 font-weight:900;
 font-size:13px;
 cursor:pointer;
 padding:6px 0;
 border-radius:16px;
 transition:.2s;
}

.nav button:hover{
 background:#eef6ff;
 color:var(--accent);
}

.nav span{
 display:block;
 font-size:24px;
 color:#5a7ea6;
}

.nav .active-nav{
 color:var(--accent);
 background:#eef6ff;
}

</style>
</head>

<body>
<div class="phone">

<h3>Employee Dashboard</h3>

<div class="page">

<div class="top">
    <div class="rate-card">
        <div class="circle">
            <span>Problem Rate:</span>
            <b>4.5%</b>
        </div>
    </div>

    <div>
        <div class="title">Network Issues</div>
    </div>
</div>

<div class="section">Alert History & Problems</div>

<div class="alerts">

    <div class="alert">
        <div class="alert-head red">❗ Problem</div>
        <div class="alert-body">Region: Amman Slow Internet</div>
    </div>

    <div class="alert">
        <div class="alert-head yellow">⚠️ Internal</div>
        <div class="alert-body">Region: Amman Slow Internet</div>
    </div>

    <div class="alert">
        <div class="alert-head blue">↗ External</div>
        <div class="alert-body">External ISP issue</div>
    </div>

</div>

</div>

<!-- NAV -->
<div class="nav">

    <form action="/" method="get" target="_top">
        <input type="hidden" name="page" value="employee">
        <button class="active-nav"><span>⌂</span>Home</button>
    </form>

    <form action="/" method="get" target="_top">
        <button><span>⇥</span>Logout</button>
    </form>

    <form action="/" method="get" target="_top">
        <input type="hidden" name="page" value="todo">
        <button><span>☑</span>To Do</button>
    </form>

</div>

</div>
</body>
</html>
""", height=820)
