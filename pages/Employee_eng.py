import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import os

st.set_page_config(page_title="Employee Dashboard", layout="centered")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] { background:#eef2f7; }
.block-container { padding-top:10px; max-width:520px; direction: ltr; }
header, footer { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

# =========================
# Original Interface
# =========================
components.html("""
<!DOCTYPE html>
<html dir="ltr">
<head>
<style>
:root{
 --navy:#0f2446;
 --navy-light:#2f4f7c;
 --accent:#2f80ed;
}
*{box-sizing:border-box;font-family:Arial,sans-serif}
body{margin:0;background:transparent}

.phone{
 width:400px;height:790px;margin:auto;background:#fbfdff;border-radius:42px;
 padding:22px 18px 10px;box-shadow:0 8px 25px rgba(0,0,0,.25);
 border:1px solid #d9dee8;position:relative;overflow:hidden;
}

.page{height:690px;overflow-y:auto;padding-bottom:90px}
.top{display:grid;grid-template-columns:124px 1fr;gap:14px}

.rate-card{
 height:124px;background:white;border-radius:16px;display:flex;
 align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(0,0,0,.12)
}

.circle{
 width:100px;height:100px;border-radius:50%;border:10px solid var(--accent);
 display:flex;flex-direction:column;align-items:center;justify-content:center
}
.circle span{font-size:10px}
.circle b{font-size:25px}

.head{display:flex;justify-content:space-between;align-items:start;margin-bottom:10px}

.title{
 font-size:17px;font-weight:900;line-height:1.2;color:var(--navy);
}

.section{
 font-size:13px;font-weight:800;margin:14px 0 6px;color:var(--navy-light);
}

.location{
 font-size:11px;border:none;background:white;border-radius:8px;padding:7px;
 box-shadow:0 2px 8px rgba(0,0,0,.10);max-width:115px;
 color:var(--navy);font-weight:600;
}

.map{
 height:98px;background:#e6ecf5;border-radius:13px;position:relative;overflow:hidden;
 box-shadow:inset 0 0 0 1px #d7deea
}

.road{position:absolute;height:3px;width:240px;background:white;opacity:.9;transform:rotate(-35deg)}
.road2{position:absolute;height:3px;width:220px;background:white;opacity:.9;transform:rotate(35deg)}
.dot{position:absolute;color:#e02020;font-size:21px}

.alerts{display:grid;grid-template-columns:repeat(3,1fr);gap:9px}

.alert{
 background:white;border-radius:10px;overflow:hidden;min-height:118px;
 box-shadow:0 4px 14px rgba(0,0,0,.12);font-size:9.5px;
 cursor:pointer;transition:.2s;
}
.alert:hover{transform:translateY(-5px);box-shadow:0 10px 20px rgba(0,0,0,.15)}
.alert:active{transform:scale(.95)}

.alert-head{color:white;padding:8px;font-weight:900;font-size:13px}
.red{background:#e94c4c}
.yellow{background:#f2b72f}
.blue{background:#2f80ed}

.alert-body{padding:8px;line-height:1.35;color:#1f2937}

.metrics{display:grid;grid-template-columns:1fr 1fr;gap:13px}

.chart{
 height:145px;background:white;border-radius:14px;
 box-shadow:0 4px 14px rgba(0,0,0,.10);position:relative;overflow:hidden;
 cursor:pointer;transition:.2s;
}
.chart:hover{transform:translateY(-5px);box-shadow:0 10px 20px rgba(0,0,0,.15)}
.chart:active{transform:scale(.95)}

.chart-title{
 position:absolute;bottom:29px;left:0;width:100%;text-align:center;font-size:12px
}

.chart-stars{
 position:absolute;bottom:8px;left:0;width:100%;text-align:center;color:#1267c9;font-size:18px
}

.line{position:absolute;left:35px;bottom:55px;width:130px;height:62px}
.bar{position:absolute;bottom:55px;width:19px;background:#2f80ed}

.employee{
 background:white;border-radius:14px;padding:11px;display:flex;gap:12px;align-items:center;
 box-shadow:0 4px 14px rgba(0,0,0,.10);
 cursor:pointer;transition:.2s;
}
.employee:hover{transform:translateY(-5px);box-shadow:0 10px 20px rgba(0,0,0,.15)}
.employee:active{transform:scale(.95)}

.avatar{
 width:58px;height:58px;border-radius:50%;background:#dbeafe;
 display:flex;align-items:center;justify-content:center;font-size:30px
}

.emp-name{font-size:15px;font-weight:900;color:var(--navy)}
.emp-text{font-size:10px;line-height:1.25;color:#1f2937}

.nav{
 position:absolute;
 bottom:10px;
 left:15px;
 right:15px;
 display:flex;
 justify-content:space-between;
 gap:10px;
}

.nav form{width:33%;margin:0}

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
 color:#376f91;
}

.nav .active-nav{
 background:#eef6ff;
 color:#2f80ed;
}
</style>
</head>

<body>
<div class="phone">

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
                    <option value="Amman">📍 Amman</option>
                    <option value="Zarqa">📍 Zarqa</option>
                    <option value="Irbid">📍 Irbid</option>
                    <option value="Balqa">📍 Balqa</option>
                    <option value="Mafraq">📍 Mafraq</option>
                    <option value="Jerash">📍 Jerash</option>
                    <option value="Ajloun">📍 Ajloun</option>
                    <option value="Madaba">📍 Madaba</option>
                    <option value="Karak">📍 Karak</option>
                    <option value="Tafilah">📍 Tafilah</option>
                    <option value="Ma'an">📍 Ma'an</option>
                    <option value="Aqaba">📍 Aqaba</option>
                </select>
            </div>

            <div class="map">
                <div class="road" style="top:8px;left:-65px;"></div>
                <div class="road" style="top:32px;left:-40px;"></div>
                <div class="road" style="top:60px;left:-65px;"></div>
                <div class="road" style="top:86px;left:-25px;"></div>
                <div class="road2" style="top:18px;left:48px;"></div>
                <div class="road2" style="top:55px;left:70px;"></div>
                <div class="road2" style="top:90px;left:90px;"></div>
                <div class="dot" style="top:22px;left:78px;">●</div>
                <div class="dot" style="top:44px;left:138px;">●</div>
                <div class="dot" style="top:67px;left:148px;">●</div>
                <div class="dot" style="top:13px;left:182px;font-size:13px;">●</div>
            </div>
        </div>
    </div>

    <div class="section">Alerts and Issues Log</div>

    <div class="alerts">
        <div class="alert">
            <div class="alert-head red">❗ Problem</div>
            <div class="alert-body">
                <b>Region:</b> <span class="region-name">Amman</span>: Customer issues are displayed from the chat log below.
            </div>
        </div>

        <div class="alert">
            <div class="alert-head yellow">⚠️ Internal</div>
            <div class="alert-body">
                Employee alerts appear based on customer message analysis.
            </div>
        </div>

        <div class="alert">
            <div class="alert-head blue">↗ External</div>
            <div class="alert-body">
                Customer notifications appear when escalation is required.
            </div>
        </div>
    </div>

    <div class="section">Network Performance Indicators</div>

    <div class="metrics">
        <div class="chart">
            <svg class="line" viewBox="0 0 140 70">
                <polygon points="0,65 0,55 45,40 95,25 135,5 135,65" fill="#dbeafe"/>
                <polyline points="0,55 45,40 95,25 135,5" fill="none" stroke="#2f80ed" stroke-width="4"/>
            </svg>
            <div style="position:absolute;left:15px;top:25px;font-size:12px;">20</div>
            <div style="position:absolute;left:15px;top:63px;font-size:12px;">10</div>
            <div style="position:absolute;left:15px;top:101px;font-size:12px;">0</div>
            <div class="chart-title">Average Response Time (ms)</div>
        </div>

        <div class="chart">
            <div class="bar" style="left:45px;height:43px;"></div>
            <div class="bar" style="left:76px;height:28px;"></div>
            <div class="bar" style="left:107px;height:70px;"></div>
            <div class="bar" style="left:138px;height:31px;"></div>
            <div style="position:absolute;left:18px;top:25px;font-size:12px;">10</div>
            <div style="position:absolute;left:18px;top:66px;font-size:12px;">5</div>
            <div style="position:absolute;left:18px;top:101px;font-size:12px;">0</div>
            <div class="chart-title">Packet Loss (%)</div>
            <div class="chart-stars">★ ★ ★</div>
        </div>
    </div>

    <div class="section">Employee of the Month</div>

    <div class="employee">
        <div class="avatar">👨‍💼</div>
        <div>
            <div class="emp-name">Ahmad Ali</div>
            <div class="emp-text">
                In recognition of your outstanding efforts and exceptional performance in improving network stability and customer service this month.
                Congratulations on this well-deserved recognition.
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
        <input type="hidden" name="page" value="logout">
        <button type="submit"><span>⇥</span>Logout</button>
    </form>

    <form action="/" method="get" target="_top">
        <input type="hidden" name="page" value="todo">
        <button type="submit"><span>☑</span>Tasks</button>
    </form>
</div>

</div>

<script>
function updateRegion(){
    const selected = document.getElementById("region").value;
    const regions = document.getElementsByClassName("region-name");

    for(let i=0;i<regions.length;i++){
        regions[i].innerText = selected;
    }
}
</script>

</body>
</html>
""", height=820)


# =========================
# Customer Message Analysis
# =========================
st.markdown("---")
st.subheader("📊 Customer Message Analysis")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHAT_LOG_PATH = os.path.join(BASE_DIR, "..", "data", "chat_logs.csv")

if os.path.exists(CHAT_LOG_PATH):
    logs = pd.read_csv(CHAT_LOG_PATH, encoding="utf-8-sig")

    if logs.empty:
        st.info("No customer messages yet.")
    else:
        latest = logs.tail(1).iloc[0]

        channel = str(latest.get("display_channel", "none"))
        notification_type = str(latest.get("notification_type", "none"))
        escalation = str(latest.get("escalation", "False")).lower() in ["true", "1", "yes"]
        network_problem = str(latest.get("network_problem", "False")).lower() in ["true", "1", "yes"]

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Intent", latest.get("intent", ""))
            st.metric("Sentiment", latest.get("sentiment", ""))

        with col2:
            st.metric("Problem", latest.get("issue_type", ""))
            st.metric("Network", str(latest.get("network_problem", "")))

        with col3:
            st.metric("Notification", notification_type)
            st.metric("Channel", channel)

        st.markdown("### 🚦 Escalation Status")

        if channel == "monitoring_log":
            st.info("🟢 Normal monitoring: the issue was logged without internal or external notification.")

        elif channel == "customer_app":
            st.warning("🟡 External Notification: the customer was notified due to repeated issues from the same customer.")

        elif channel == "employee_dashboard":
            st.error("🔴 Internal Escalation: the issue repeated in the same region and requires employee follow-up.")

        elif not network_problem:
            st.success("✅ No network issue in the latest message.")

        else:
            st.info("No escalation stage is currently defined.")

        st.markdown("### 🚨 Problem / Alert")
        if network_problem:
            st.error(f"Issue Type: {latest.get('issue_type', '')}")
            st.write("Reason:", latest.get("reason", ""))
            st.write("Suggested Action:", latest.get("suggested_action", ""))
            st.write("Customer Repeat Count:", latest.get("repeat_count", ""))
            st.write("Area Issue Count:", latest.get("area_issue_count", ""))
        else:
            st.success("No current network issue.")

        st.markdown("### 🏢 Internal Notification")
        if channel == "employee_dashboard":
            st.warning("Internal employee alert: please follow up from the employee dashboard.")
        else:
            st.info("No current internal alert.")

        st.markdown("### 📱 External Notification")
        if channel == "customer_app":
            st.warning("External customer alert: the customer will be notified about the issue follow-up.")
        elif channel == "employee_dashboard" and str(latest.get("show_to_customer", "0")) in ["1", "True", "true"]:
            st.warning("External customer alert + internal employee escalation.")
        else:
            st.info("No current external alert.")

        st.markdown("### 👤 Latest Message")
        st.write("Customer Message:", latest.get("message", ""))
        st.write("Bot Response:", latest.get("bot_response", ""))
        st.write("Region:", latest.get("region", ""))
        st.write("Customer:", latest.get("user_id", ""))
        st.write("Decision Rule:", latest.get("decision_rule", ""))

        st.markdown("### 📋 Latest 20 Records")
        st.dataframe(logs.tail(20), use_container_width=True)

else:
    st.info("No log file exists yet. Send a message from the customer chat first.")
