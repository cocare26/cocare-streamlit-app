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
body{margin:0;background:transparent}

.phone{
 width:400px;height:790px;margin:auto;background:#fbfdff;border-radius:42px;
 padding:22px 18px 10px;box-shadow:0 8px 25px rgba(0,0,0,.25);
 position:relative;overflow:hidden;
}

/* 🔥 NAV داخل الشاشة */
.nav{
 position:absolute;
 bottom:10px;
 left:15px;
 right:15px;

 display:flex;
 justify-content:space-between;
 gap:10px;
}

.nav form{
 width:33%;
}

.nav button{
 width:100%;
 height:58px;
 border-radius:18px;
 border:none;
 background:white;
 font-weight:900;
 font-size:13px;
 cursor:pointer;
 box-shadow:0 4px 10px rgba(0,0,0,.1);
 transition:.25s;
}

.nav button:hover{
 background:#eef6ff;
 color:#2f80ed;
 transform:translateY(-3px);
}

.nav span{
 display:block;
 font-size:22px;
 margin-bottom:3px;
}

</style>
</head>

<body>

<div class="phone">

<!-- 🔥 NAV داخل الكارد -->
<div class="nav">

<form action="/" method="get" target="_top">
<input type="hidden" name="page" value="employee">
<button>
<span>⌂</span>
Home
</button>
</form>

<form action="/" method="get" target="_top">
<button>
<span>⇥</span>
Logout
</button>
</form>

<form action="/" method="get" target="_top">
<input type="hidden" name="page" value="todo">
<button>
<span>☑</span>
To Do List
</button>
</form>

</div>

</div>

</body>
</html>
""", height=820)
