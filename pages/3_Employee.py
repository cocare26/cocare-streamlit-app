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

/* 🎨 ألوان احتراف */
:root{
    --navy-main:#0f2446;
    --navy-light:#2f4f7c;
    --text-dark:#1f2937;
    --text-soft:#6b7280;
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

/* 🧠 العنوان الرئيسي */
h3{
 color:var(--navy-main);
 font-size:20px;
 font-weight:900;
 letter-spacing:.5px;
 text-align:center;
 margin-top:10px;
}

/* 📌 Network Issues */
.title{
 color:var(--navy-main);
 font-weight:900;
 font-size:18px;
}

/* 📊 عناوين الأقسام */
.section{
 color:var(--navy-light);
 font-size:13px;
 font-weight:800;
 margin:14px 0 6px;
}

/* 👤 اسم الموظف */
.emp-name{
 color:var(--navy-main);
 font-size:15px;
 font-weight:900;
}

/* 📝 النص */
.emp-text,
.alert-body{
 color:var(--text-dark);
}

.location{
 color:var(--navy-main);
 font-weight:600;
 font-size:11px;
 border:none;background:white;border-radius:8px;padding:7px;
 box-shadow:0 2px 8px rgba(0,0,0,.10);max-width:115px
}

.rate-card,
.alert,
.chart,
.employee{
 background:#ffffff;
}

.circle{
 width:100px;height:100px;border-radius:50%;border:10px solid var(--accent);
 display:flex;flex-direction:column;align-items:center;justify-content:center
}

.alert-head{color:white;padding:8px;font-weight:900;font-size:13px}

.red{background:#e94c4c}
.yellow{background:#f2b72f}
.blue{background:#2f80ed}

/* ⭐ النجوم */
.chart-stars{
 color:var(--accent);
 font-size:18px;
}

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
 color:#5a7ea6;
 margin-bottom:2px;
}

.nav button:hover span{color:var(--accent)}
.nav .active-nav{color:var(--accent);background:#eef6ff}

</style>
</head>

<body>
<div class="phone">

<h3>Employee Dashboard</h3>

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
                    <option>📍 Amman</option>
                    <option>📍 Zarqa</option>
                    <option>📍 Irbid</option>
                </select>
            </div>
        </div>
    </div>

    <div class="section">Alert History & Problems</div>

    <div class="alerts">
        <div class="alert">
            <div class="alert-head red">❗ Problem</div>
            <div class="alert-body">
                Region: Amman Slow Internet
            </div>
        </div>

        <div class="alert">
            <div class="alert-head yellow">⚠️ Internal</div>
            <div class="alert-body">
                Region: Amman Slow Internet
            </div>
        </div>

        <div class="alert">
            <div class="alert-head blue">↗ External</div>
            <div class="alert-body">
                External ISP issue
            </div>
        </div>
    </div>

</div>

<div class="nav">
    <form action="/" method="get" target="_top">
        <input type="hidden" name="page" value="employee">
        <button type="submit" class="active-nav"><span>⌂</span>Home</button>
    </form>

    <form action="/" method="get" target="_top">
        <button type="submit"><span>⇥</span>Logout</button>
    </form>

    <form action="/" method="get" target="_top">
        <input type="hidden" name="page" value="todo">
        <button type="submit"><span>☑</span>To Do</button>
    </form>
</div>

</div>

</body>
</html>
""", height=820)
