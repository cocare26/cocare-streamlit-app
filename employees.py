import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout="centered")

# ================= CSS =================
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: #eef2f7;
}

.block-container {
    max-width: 520px;
}

.phone {
    background: white;
    border-radius: 40px;
    padding: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.2);
}

/* top */
.top {
    display:flex;
    gap:12px;
}

.circle {
    width:110px;
    height:110px;
    border-radius:50%;
    border:10px solid #2F80ED;
    display:flex;
    align-items:center;
    justify-content:center;
    font-weight:bold;
    font-size:20px;
}

/* map */
.map {
    flex:1;
    background:#E9EEF6;
    border-radius:15px;
    height:110px;
    position:relative;
}

.dot {
    position:absolute;
    color:red;
    font-size:22px;
}

/* alerts */
.alerts {
    display:flex;
    gap:10px;
    margin-top:15px;
}

.card {
    flex:1;
    border-radius:12px;
    background:white;
    box-shadow:0 3px 10px rgba(0,0,0,0.1);
    overflow:hidden;
    font-size:11px;
}

.head {
    color:white;
    padding:6px;
    font-weight:bold;
}

.red{background:#EB5757;}
.yellow{background:#F2C94C;}
.blue{background:#2F80ED;}

.body{padding:8px;}

/* employee */
.employee{
    display:flex;
    gap:10px;
    background:white;
    padding:10px;
    border-radius:12px;
    box-shadow:0 3px 10px rgba(0,0,0,0.1);
}

.img{
    width:60px;
    height:60px;
    border-radius:50%;
    background:#ddd;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:30px;
}

/* bottom */
.bottom{
    margin-top:15px;
    display:flex;
    justify-content:space-around;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# ================= UI =================
st.markdown('<div class="phone">', unsafe_allow_html=True)

# top
st.markdown("""
<div class="top">
    <div class="circle">4.5%</div>

    <div style="flex:1;">
        <b>Network Issues</b>
        <div class="map">
            <div class="dot" style="top:20px;left:60px;">●</div>
            <div class="dot" style="top:50px;left:120px;">●</div>
            <div class="dot" style="top:70px;left:150px;">●</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# alerts
st.markdown("<h4>Alert History & Problems</h4>", unsafe_allow_html=True)

st.markdown("""
<div class="alerts">

<div class="card">
<div class="head red">Problem</div>
<div class="body">Region: Irbid Slow Internet</div>
</div>

<div class="card">
<div class="head yellow">Internal</div>
<div class="body">Region: Irbid Slow Internet</div>
</div>

<div class="card">
<div class="head blue">External</div>
<div class="body">Reported by ISP</div>
</div>

</div>
""", unsafe_allow_html=True)

# charts
st.markdown("<h4>Network Performance Metrics</h4>", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    fig, ax = plt.subplots()
    ax.plot([5,10,15,20])
    st.pyplot(fig)

with c2:
    fig, ax = plt.subplots()
    ax.bar([1,2,3],[3,7,5])
    st.pyplot(fig)

# employee
st.markdown("<h4>Employee of the Month</h4>", unsafe_allow_html=True)

st.markdown("""
<div class="employee">
<div class="img">👨‍💼</div>
<div>
<b>Ahmed Ali</b><br>
Outstanding performance this month
</div>
</div>
""", unsafe_allow_html=True)

# bottom
st.markdown("""
<div class="bottom">
🏠 Home &nbsp;&nbsp; 🚪 Logout &nbsp;&nbsp; ✅ To Do
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
