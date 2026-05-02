import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="لوحة الموظف", layout="centered")

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

.page{height:690px;overflow-y:auto;padding-bottom:90px}

/* 🔥 العنوان */
.title{
 font-size:17px;
 font-weight:900;
 color:var(--navy);
}

/* 📍 الموقع */
.location{
 font-size:11px;
 border:none;
 background:white;
 border-radius:8px;
 padding:7px;
 box-shadow:0 2px 8px rgba(0,0,0,.10);
}

/* 🔔 التنبيهات */
.alert{
 background:white;
 border-radius:10px;
 box-shadow:0 4px 14px rgba(0,0,0,.12);
 padding:8px;
 margin-bottom:8px;
 cursor:pointer;
}

.alert-head{
 color:white;
 padding:6px;
 border-radius:6px;
 font-weight:bold;
}

.red{background:#e94c4c}
.yellow{background:#f2b72f}
.blue{background:#2f80ed}

/* 👤 موظف */
.employee{
 background:white;
 border-radius:14px;
 padding:10px;
 box-shadow:0 4px 14px rgba(0,0,0,.10);
 cursor:pointer;
}

.nav{
 position:absolute;
 bottom:10px;
 left:15px;
 right:15px;
 display:flex;
 gap:10px;
}

.nav form{width:33%}

.nav button{
 width:100%;
 height:58px;
 border-radius:18px;
 border:none;
 background:white;
 font-weight:900;
 cursor:pointer;
}

.nav button:hover{
 background:#eef6ff;
 color:#2f80ed;
}

</style>
</head>

<body>

<div class="phone">

<div class="page">

<h3 class="title">مشاكل الشبكة</h3>

<select class="location">
<option>📍 عمان</option>
<option>📍 الزرقاء</option>
<option>📍 إربد</option>
</select>

<br><br>

<div class="alert" onclick="alert('تم اختيار مشكلة')">
<div class="alert-head red">❗ مشكلة</div>
بطء في الإنترنت - تقارير مستخدمين
</div>

<div class="alert" onclick="alert('مشكلة داخلية')">
<div class="alert-head yellow">⚠️ داخلي</div>
مشكلة داخلية بالشبكة
</div>

<div class="alert" onclick="alert('مشكلة خارجية')">
<div class="alert-head blue">🌐 خارجي</div>
المشكلة من مزود الخدمة
</div>

<br>

<div class="employee" onclick="alert('تفاصيل الموظف')">
👨‍💼 أحمد علي - أفضل موظف لهذا الشهر
</div>

</div>

<!-- 🔥 NAV -->
<div class="nav">

<form action="/" method="get" target="_top">
<input type="hidden" name="page" value="employee">
<button>🏠 الرئيسية</button>
</form>

<form action="/" method="get" target="_top">
<button>🚪 تسجيل الخروج</button>
</form>

<form action="/" method="get" target="_top">
<input type="hidden" name="page" value="todo">
<button>📋 المهام</button>
</form>

</div>

</div>

</body>
</html>
""", height=820)
