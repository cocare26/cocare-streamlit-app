import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="CoCare", layout="centered")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: #eef2f7;
}

.block-container {
    max-width: 520px;
    padding-top: 20px;
    padding-bottom: 20px;
}

.phone {
    background: #ffffff;
    border-radius: 45px;
    padding: 22px 18px 10px 18px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.25);
    border: 2px solid #d1d5db;
    overflow: hidden;
}

.top-row {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 12px;
    align-items: start;
}

.title-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
}

.title {
    font-size: 20px;
    font-weight: 800;
    color: #1f2937;
}

.location {
    font-size: 11px;
    color: #6b7280;
}

.card {
    background: white;
    border-radius: 16px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.10);
    padding: 10px;
}

.circle {
    width: 105px;
    height: 105px;
    border-radius: 50%;
    border: 10px solid #2f80ed;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: auto;
    font-size: 23px;
    font-weight: 800;
    color: #111827;
    position: relative;
}

.circle-label {
    position: absolute;
    top: 26px;
    font-size: 12px;
    font-weight: 500;
    color: #374151;
}

.circle-value {
    margin-top: 28px;
}

.map {
    height: 120px;
    background: #e8edf5;
    border-radius: 14px;
    position: relative;
    overflow: hidden;
}

.road {
    position: absolute;
    height: 3px;
    width: 220px;
    background: white;
    opacity: .9;
    transform: rotate(-35deg);
}

.road2 {
    position: absolute;
    height: 3px;
    width: 180px;
    background: white;
    opacity: .9;
    transform: rotate(35deg);
}

.dot {
    position: absolute;
    color: #c93434;
    font-size: 24px;
}

.section-title {
    font-size: 18px;
    font-weight: 800;
    margin: 18px 0 10px 0;
    color: #1f2937;
}

.alerts {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
}

.alert-card {
    background: white;
    border-radius: 10px;
    box-shadow: 0 2px 9px rgba(0,0,0,0.12);
    overflow: hidden;
    min-height: 105px;
    font-size: 10px;
}

.alert-head {
    color: white;
    padding: 7px;
    font-size: 13px;
    font-weight: 800;
}

.alert-body {
    padding: 8px;
    line-height: 1.25;
}

.red { background:#e74c3c; }
.yellow { background:#f2b233; }
.blue { background:#2f80ed; }

.metrics {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
}

.stars {
    text-align: center;
    color: #2f80ed;
    font-size: 20px;
    margin-top: -8px;
}

.divider {
    height: 1px;
    background: #d7dde7;
    margin: 12px 0;
}

.employee {
    display: flex;
    gap: 14px;
    align-items: center;
    background: white;
    border-radius: 14px;
    padding: 12px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.10);
}

.emp-img {
    width: 68px;
    height: 68px;
    border-radius: 50%;
    background: #dbeafe;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 35px;
}

.emp-name {
    font-size: 18px;
    font-weight: 800;
}

.emp-text {
    font-size: 11px;
    line-height: 1.25;
}

.bottom-nav {
    margin-top: 12px;
    height: 72px;
    background: white;
    display: flex;
    justify-content: space-around;
    align-items: center;
    border-top: 1px solid #e5e7eb;
    font-size: 16px;
    font-weight: 800;
    color: #374151;
}

.nav-item {
    text-align: center;
}

.nav-icon {
    font-size: 30px;
    color: #3b6f8f;
}

button {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="phone">', unsafe_allow_html=True)

st.markdown("""
<div class="top-row">
    <div class="card">
        <div class="circle">
            <div class="circle-label">Problem Rate:</div>
            <div class="circle-value">4.5%</div>
        </div>
    </div>

    <div>
        <div class="title-row">
            <div class="title">Network Issues</div>
            <div class="location">📍 Select Location</div>
        </div>

        <div class="map">
            <div class="road" style="top:15px;left:-35px;"></div>
            <div class="road" style="top:45px;left:-10px;"></div>
            <div class="road" style="top:75px;left:-45px;"></div>
            <div class="road" style="top:105px;left:-5px;"></div>

            <div class="road2" style="top:25px;left:85px;"></div>
            <div class="road2" style="top:65px;left:70px;"></div>
            <div class="road2" style="top:100px;left:105px;"></div>

            <div class="dot" style="top:28px;left:82px;">●</div>
            <div class="dot" style="top:55px;left:160px;">●</div>
            <div class="dot" style="top:83px;left:170px;">●</div>
            <div class="dot" style="top:15px;left:205px;font-size:14px;">●</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Alert History & Problems</div>', unsafe_allow_html=True)

st.markdown("""
<div class="alerts">
    <div class="alert-card">
        <div class="alert-head red">❗ Problem</div>
        <div class="alert-body">
            <b>Region:</b> Irbid: Multiple User Reports 09:30 AM of Slow Internet.
        </div>
    </div>

    <div class="alert-card">
        <div class="alert-head yellow">⚠️ Internal</div>
        <div class="alert-body">
            <b>Region:</b> Irbid: Multiple User Reports 09:30 AM of Slow Internet.
        </div>
    </div>

    <div class="alert-card">
        <div class="alert-head blue">↗ External</div>
        <div class="alert-body">
            <b>Region:</b> Irbid This Internet issue is external. The problem is reported by the ISP.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Network Performance Metrics</div>', unsafe_allow_html=True)

m1, m2 = st.columns(2)

with m1:
    fig, ax = plt.subplots(figsize=(2.4, 1.6))
    ax.plot([0, 1, 2, 3], [5, 10, 15, 20], linewidth=2)
    ax.fill_between([0, 1, 2, 3], [5, 10, 15, 20], alpha=0.2)
    ax.set_ylim(0, 25)
    ax.set_xticks([])
    ax.set_title("Avg Latency (ms)", fontsize=9)
    ax.tick_params(labelsize=8)
    st.pyplot(fig, use_container_width=True)

with m2:
    fig, ax = plt.subplots(figsize=(2.4, 1.6))
    ax.bar(["", "", "", ""], [6, 3, 11, 10])
    ax.set_ylim(0, 12)
    ax.set_title("Packet Loss (%)", fontsize=9)
    ax.tick_params(labelsize=8)
    st.pyplot(fig, use_container_width=True)

st.markdown('<div class="stars">★★★</div>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Employee of the Month Announcement</div>', unsafe_allow_html=True)

st.markdown("""
<div class="employee">
    <div class="emp-img">👨‍💼</div>
    <div>
        <div class="emp-name">Ahmed Ali</div>
        <div class="emp-text">
            For your exceptional dedication and outstanding performance in improving network stability and customer service this month.
            Congratulations on this well-deserved recognition.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="bottom-nav">
    <div class="nav-item">
        <div class="nav-icon">⌂</div>
        Home
    </div>
    <div class="nav-item">
        <div class="nav-icon">⇥</div>
        Logout
    </div>
    <div class="nav-item">
        <div class="nav-icon">☑</div>
        To Do List
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
