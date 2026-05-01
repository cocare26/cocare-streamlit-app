import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout="centered")

# ---------- CSS مطابق ----------
st.markdown("""
<style>
body {
    background-color: #f5f7fb;
}

.card {
    background: white;
    border-radius: 18px;
    padding: 15px;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

.circle {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    border: 10px solid #2F80ED;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:22px;
    font-weight:bold;
    margin:auto;
}

.alert {
    background: white;
    border-radius: 12px;
    padding: 10px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}

.alert-header {
    color: white;
    padding: 6px;
    border-radius: 10px 10px 0 0;
    margin:-10px -10px 10px -10px;
    font-weight:bold;
}

.red {background:#EB5757;}
.yellow {background:#F2C94C;}
.blue {background:#2F80ED;}

.bottom-bar {
    position:fixed;
    bottom:0;
    width:100%;
    background:white;
    display:flex;
    justify-content:space-around;
    padding:10px;
    border-top:1px solid #ddd;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.title("Network Issues")

st.selectbox("📍 Select Location", ["Irbid", "Amman", "Zarqa"])

# ---------- Top Section ----------
col1, col2 = st.columns([1,2])

with col1:
    st.markdown("""
    <div class="card" style="text-align:center;">
        <div style="color:gray;">Problem Rate</div>
        <div class="circle">4.5%</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div style="height:140px;background:#eef2f7;border-radius:12px;position:relative;">
            <div style="position:absolute;top:30px;left:60px;color:red;font-size:25px;">●</div>
            <div style="position:absolute;top:50px;left:120px;color:red;font-size:25px;">●</div>
            <div style="position:absolute;top:20px;left:180px;color:red;font-size:20px;">●</div>
            <div style="position:absolute;top:80px;left:150px;color:red;font-size:25px;">●</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------- Alerts ----------
st.subheader("Alert History & Problems")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="alert">
        <div class="alert-header red">❗ Problem</div>
        Region: Irbid<br>
        Multiple Reports<br>
        09:30 AM Slow Internet
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="alert">
        <div class="alert-header yellow">⚠️ Internal</div>
        Region: Irbid<br>
        Multiple Reports<br>
        09:30 AM Slow Internet
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="alert">
        <div class="alert-header blue">🔗 External</div>
        Region: Irbid<br>
        Issue reported by ISP
    </div>
    """, unsafe_allow_html=True)

# ---------- Charts ----------
st.subheader("Network Performance Metrics")

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    ax.plot([5,10,15,20])
    ax.set_title("Avg Latency (ms)")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    ax.bar([1,2,3,4],[3,7,2,8])
    ax.set_title("Packet Loss (%)")
    st.pyplot(fig)

# ---------- Employee ----------
st.subheader("Employee of the Month")

st.markdown("""
<div class="card">
<b>Ahmed Ali</b><br>
For outstanding performance in improving network stability.
</div>
""", unsafe_allow_html=True)

# ---------- Bottom Nav ----------
st.markdown("""
<div class="bottom-bar">
🏠 Home
🚪 Logout
✅ To Do
</div>
""", unsafe_allow_html=True)
