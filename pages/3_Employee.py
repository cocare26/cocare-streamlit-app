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
*{box-sizing:border-box;font-family:Arial,sans-serif}
body{margin:0;background:transparent}

.phone{
 width:400px;height:790px;margin:auto;background:#fbfdff;border-radius:42px;
 padding:22px 18px 10px;box-shadow:0 8px 25px rgba(0,0,0,.25);
 border:1px solid #d9dee8;position:relative;overflow:hidden;
}

.page{height:690px;overflow-y:auto;padding-bottom:20px}

/* ===== NAV احترافي ===== */
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
 color:#2f80ed;
 transform:translateY(-3px);
}

.nav span{
 display:block;
 font-size:25px;
 color:#376f91;
 margin-bottom:2px;
}

.nav button:hover span{
 color:#2f80ed;
}

.nav .active-nav{
 color:#2f80ed;
 background:#eef6ff;
}
/* ===== END NAV ===== */

</style>
</head>

<body>
<div class="phone">

<div class="page">
    <h3 style="text-align:center;margin-top:40px;">Employee Dashboard</h3>
</div>

<!-- 🔥 NAVIGATION -->
<div class="nav">

    <!-- Home -->
    <form action="/" method="get" target="_top">
        <input type="hidden" name="page" value="employee">
        <button type="submit" class="active-nav">
            <span>⌂</span>Home
        </button>
    </form>

    <!-- Logout -->
    <form action="/" method="get" target="_top">
        <input type="hidden" name="page" value="">
        <button type="submit">
            <span>⇥</span>Logout
        </button>
    </form>

    <!-- To Do -->
    <form action="/" method="get" target="_top">
        <input type="hidden" name="page" value="todo">
        <button type="submit">
            <span>☑</span>To Do List
        </button>
    </form>

</div>

</div>

</body>
</html>
""", height=820)
