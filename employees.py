import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="CoCare", layout="centered")

# ================== CSS ==================
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: #F6F8FC;
}

.main-card {
    background: white;
    padding: 18px;
    border-radius: 20px;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.08);
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

.alert-card {
    background:white;
    border-radius:14px;
    overflow:hidden;
    box-shadow:0px 3px 10px rgba(0,0,0,0.08);
}

.alert-header {
    color:white;
    padding:8px;
    font-weight:bold;
}

.red {background:#EB5757;}
.yellow {background:#F2C94C;}
.blue {background:#2F80ED;}

.bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    height: 80px;
    background: white;
    border-top: 1px solid #ddd;
    display: flex;
    justify-content: center;
    gap: 90px;
    align-items: center;
    box-shadow: 0 -3px 10px rgba(0,0,0,0.05);
}

.nav-item {
    font-size: 22px;
    text-align:center;
}
.nav-active {
    color:#2F80ED;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# ================== NAV ==================
if "page" not in st.session_state:
    st.session_state.page = "Home"

cols = st.columns(3)

if cols[0].button("🏠 Home", use_container_width=True):
    st.session_state.page = "Home"

if cols[1].button("🚪 Logout", use_container_width=True):
    st.session_state.page = "Logout"

if cols[2].button("✅ To Do", use_container_width=True):
    st.session_state.page = "To Do"

page = st.session_state.page

# ================== HOME ==================
if page == "Home":
    st.title("CoCare Dashboard")

    st.markdown("""
    <div class="main-card">
    Welcome to CoCare System 🚀
    </div>
    """, unsafe_allow_html=True)

# ================== NETWORK ==================
elif page == "To Do":

    st.title("Network Issues")

    col1, col2 = st.columns([1,2])

    # circle
    with col1:
        st.markdown("""
        <div class="main-card">
            <div style="text-align:center;">
            <p>Problem Rate</p>
            <div class="circle">4.5%</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # map
    with col2:
        st.markdown("""
        <div class="main-card">
            <div style="height:200px;position:relative;background:#E9EEF6;border-radius:15px;">

            <svg viewBox="0 0 260 300" style="width:150px;height:180px;position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);">
            <path d="M110 10 L160 25 L175 70 L150 95 L170 130 L150 170 L165 210 L135 285 L95 260 L85 210 L60 180 L75 140 L55 105 L78 70 L70 35 Z"
            fill="#DDE6F2" stroke="#9AA9BD" stroke-width="4"/>
            </svg>

            <div style="position:absolute;top:60px;left:160px;color:red;">●</div>
            <div style="position:absolute;top:100px;left:150px;color:red;">●</div>
            <div style="position:absolute;top:140px;left:140px;color:red;">●</div>

            </div>
        </div>
        """, unsafe_allow_html=True)

    # alerts
    st.subheader("Alerts")

    c1, c2, c3 = st.columns(3)

    c1.markdown("""
    <div class="alert-card">
    <div class="alert-header red">Problem</div>
    Region: Irbid
    </div>
    """, unsafe_allow_html=True)

    c2.markdown("""
    <div class="alert-card">
    <div class="alert-header yellow">Internal</div>
    Region: Irbid
    </div>
    """, unsafe_allow_html=True)

    c3.markdown("""
    <div class="alert-card">
    <div class="alert-header blue">External</div>
    Region: Irbid
    </div>
    """, unsafe_allow_html=True)

    # charts
    st.subheader("Metrics")

    c1, c2 = st.columns(2)

    with c1:
        fig, ax = plt.subplots()
        ax.plot([5,10,15,20])
        st.pyplot(fig)

    with c2:
        fig, ax = plt.subplots()
        ax.bar([1,2,3],[3,7,5])
        st.pyplot(fig)

# ================== LOGOUT ==================
elif page == "Logout":
    st.title("Logout")
    st.success("تم تسجيل الخروج")

# ================== BOTTOM NAV ==================
st.markdown("<br><br><br>", unsafe_allow_html=True)

active_home = "nav-active" if page=="Home" else ""
active_logout = "nav-active" if page=="Logout" else ""
active_todo = "nav-active" if page=="To Do" else ""

st.markdown(f"""
<div class="bottom-nav">
    <div class="nav-item {active_home}">🏠<br>Home</div>
    <div class="nav-item {active_logout}">🚪<br>Logout</div>
    <div class="nav-item {active_todo}">✅<br>To Do</div>
</div>
""", unsafe_allow_html=True)
