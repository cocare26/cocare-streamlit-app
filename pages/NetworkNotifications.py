import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Notifications Center",
    page_icon="🔔",
    layout="wide"
)

# ---------------- BACK BUTTON ---------------- #

col1, col2 = st.columns([1, 8])

with col1:
    if st.button("← Back"):
        st.switch_page("pages/2_Customer_EN.py")

# ---------------- HTML UI ---------------- #

html_code = """
<!DOCTYPE html>
<html>
<head>

<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

* {
    box-sizing: border-box;
    font-family: 'Inter', sans-serif;
}

body {
    margin: 0;
    padding: 28px;

    background:
        radial-gradient(circle at 12% 18%, rgba(37, 99, 235, 0.14), transparent 28%),
        radial-gradient(circle at 88% 12%, rgba(6, 182, 212, 0.18), transparent 26%),
        linear-gradient(180deg, #F5F9FF 0%, #FFFFFF 100%);
}

.wrapper {
    max-width: 1180px;
    margin: auto;
}

.hero {
    background: linear-gradient(135deg, #2563EB, #06B6D4);

    color: white;

    padding: 32px;

    border-radius: 30px;

    box-shadow: 0 18px 45px rgba(37, 99, 235, 0.28);

    display: grid;
    grid-template-columns: 1fr 320px;

    gap: 24px;

    align-items: center;

    margin-bottom: 26px;
}

.icon-box {
    width: 60px;
    height: 60px;

    border-radius: 18px;

    background: rgba(255,255,255,0.18);

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 30px;

    margin-bottom: 18px;
}

.hero h1 {
    margin: 0;

    font-size: 44px;
    font-weight: 900;
}

.hero p {
    margin-top: 10px;

    font-size: 17px;

    opacity: 0.92;
}

.status-box {
    background: rgba(255,255,255,0.17);

    border: 1px solid rgba(255,255,255,0.28);

    border-radius: 22px;

    padding: 20px;
}

.status-label {
    font-size: 13px;
    opacity: 0.88;
}

.status-number {
    font-size: 30px;
    font-weight: 900;

    margin: 8px 0;
}

.status-meta {
    font-size: 13px;
    opacity: 0.9;
}

.summary-grid {
    display: grid;

    grid-template-columns: repeat(3, 1fr);

    gap: 22px;

    margin-bottom: 28px;
}

.summary-card {
    background: rgba(255,255,255,0.94);

    border: 1px solid #E2E8F0;

    border-radius: 24px;

    padding: 22px;

    box-shadow: 0 12px 32px rgba(15, 23, 42, 0.06);
}

.summary-label {
    color: #64748B;

    font-size: 14px;
    font-weight: 700;

    margin-bottom: 8px;
}

.summary-value {
    color: #0F172A;

    font-size: 26px;
    font-weight: 900;
}

.section-title {
    margin-bottom: 18px;
}

.section-title h2 {
    margin: 0;

    color: #0F172A;

    font-size: 30px;
    font-weight: 900;
}

.section-title p {
    color: #64748B;

    margin-top: 8px;

    font-size: 15px;
}

.notifications {
    display: grid;

    gap: 18px;
}

.notification {
    display: grid;

    grid-template-columns: 58px 1fr auto;

    gap: 18px;

    align-items: center;

    background: rgba(255,255,255,0.95);

    border-radius: 24px;

    padding: 20px;

    border: 1px solid #E2E8F0;

    box-shadow: 0 12px 32px rgba(15, 23, 42, 0.06);

    transition: all 0.25s ease;
}

.notification:hover {
    transform: translateY(-4px);

    box-shadow: 0 18px 42px rgba(37, 99, 235, 0.14);
}

.n-icon {
    width: 58px;
    height: 58px;

    border-radius: 18px;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 26px;
}

.info .n-icon {
    background: #DBEAFE;
}

.warning .n-icon {
    background: #FEF3C7;
}

.success .n-icon {
    background: #D1FAE5;
}

.n-title {
    color: #0F172A;

    font-size: 18px;
    font-weight: 900;

    margin-bottom: 6px;
}

.n-desc {
    color: #64748B;

    font-size: 15px;

    line-height: 1.45;
}

.n-time {
    color: #64748B;

    font-size: 13px;
    font-weight: 700;

    white-space: nowrap;
}

.badge {
    display: inline-block;

    padding: 7px 12px;

    border-radius: 999px;

    font-size: 12px;
    font-weight: 900;

    margin-top: 10px;
}

.info .badge {
    background: #DBEAFE;
    color: #2563EB;
}

.warning .badge {
    background: #FEF3C7;
    color: #92400E;
}

.success .badge {
    background: #D1FAE5;
    color: #047857;
}

.network-card {
    margin-top: 30px;

    background: rgba(255,255,255,0.94);

    border: 1px solid #E2E8F0;

    border-radius: 28px;

    padding: 26px;

    box-shadow: 0 14px 35px rgba(15, 23, 42, 0.07);
}

.network-card h3 {
    margin: 0 0 18px;

    color: #0F172A;

    font-size: 24px;
    font-weight: 900;
}

.metrics {
    display: grid;

    grid-template-columns: repeat(4, 1fr);

    gap: 18px;
}

.metric {
    background: #F8FAFC;

    border: 1px solid #E2E8F0;

    border-radius: 20px;

    padding: 18px;
}

.metric-label {
    color: #64748B;

    font-size: 13px;
    font-weight: 700;

    margin-bottom: 8px;
}

.metric-value {
    color: #0F172A;

    font-size: 24px;
    font-weight: 900;
}

@media(max-width: 900px) {

    .hero,
    .summary-grid,
    .metrics {
        grid-template-columns: 1fr;
    }

    .notification {
        grid-template-columns: 1fr;
    }

    .hero h1 {
        font-size: 34px;
    }
}

</style>

</head>

<body>

<div class="wrapper">

    <div class="hero">

        <div>

            <div class="icon-box">🔔</div>

            <h1>Notifications Center</h1>

            <p>
                Track service alerts, package updates, and network activity in real time.
            </p>

        </div>

        <div class="status-box">

            <div class="status-label">
                Current Status
            </div>

            <div class="status-number">
                All Systems Active
            </div>

            <div class="status-meta">
                Network stable · Amman · Excellent coverage
            </div>

        </div>

    </div>

    <div class="summary-grid">

        <div class="summary-card">
            <div class="summary-label">Unread Alerts</div>
            <div class="summary-value">3</div>
        </div>

        <div class="summary-card">
            <div class="summary-label">Signal Strength</div>
            <div class="summary-value">Excellent</div>
        </div>

        <div class="summary-card">
            <div class="summary-label">Network Status</div>
            <div class="summary-value">Stable</div>
        </div>

    </div>

    <div class="section-title">

        <h2>Recent Notifications</h2>

        <p>
            Latest updates related to your service and internet connection.
        </p>

    </div>

    <div class="notifications">

        <div class="notification info">

            <div class="n-icon">🛠️</div>

            <div>

                <div class="n-title">
                    Scheduled Maintenance
                </div>

                <div class="n-desc">
                    Network maintenance in Amman tonight from 1:00 AM to 3:00 AM.
                </div>

                <div class="badge">
                    Maintenance
                </div>

            </div>

            <div class="n-time">
                Today
            </div>

        </div>

        <div class="notification warning">

            <div class="n-icon">⚠️</div>

            <div>

                <div class="n-title">
                    Weak Signal Detected
                </div>

                <div class="n-desc">
                    Signal quality is lower than usual in your area.
                </div>

                <div class="badge">
                    Warning
                </div>

            </div>

            <div class="n-time">
                2h ago
            </div>

        </div>

        <div class="notification success">

            <div class="n-icon">✅</div>

            <div>

                <div class="n-title">
                    Package Renewed Successfully
                </div>

                <div class="n-desc">
                    Your internet package has been renewed successfully.
                </div>

                <div class="badge">
                    Success
                </div>

            </div>

            <div class="n-time">
                Yesterday
            </div>

        </div>

    </div>

    <div class="network-card">

        <h3>
            Network Performance
        </h3>

        <div class="metrics">

            <div class="metric">
                <div class="metric-label">Packet Loss</div>
                <div class="metric-value">0%</div>
            </div>

            <div class="metric">
                <div class="metric-label">Latency</div>
                <div class="metric-value">19 ms</div>
            </div>

            <div class="metric">
                <div class="metric-label">Signal</div>
                <div class="metric-value">-68 dBm</div>
            </div>

            <div class="metric">
                <div class="metric-label">Coverage</div>
                <div class="metric-value">5G</div>
            </div>

        </div>

    </div>

</div>

</body>
</html>
"""

components.html(
    html_code,
    height=1150,
    scrolling=True
)
