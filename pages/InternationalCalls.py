import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="International Calls",
    page_icon="🌍",
    layout="wide"
)

col1, col2 = st.columns([1, 8])
with col1:
    if st.button("← Back"):
        st.switch_page("pages/2_Customer_EN.py")

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
    margin-bottom: 24px;
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
    font-size: 46px;
    font-weight: 900;
}

.hero p {
    margin-top: 10px;
    font-size: 17px;
    opacity: 0.92;
}

.balance-box {
    background: rgba(255,255,255,0.17);
    border: 1px solid rgba(255,255,255,0.28);
    border-radius: 22px;
    padding: 20px;
}

.balance-label {
    font-size: 13px;
    opacity: 0.88;
}

.balance-number {
    font-size: 34px;
    font-weight: 900;
    margin: 8px 0;
}

.balance-meta {
    font-size: 13px;
    opacity: 0.9;
}

.search-card {
    background: rgba(255,255,255,0.92);
    border: 1px solid #E2E8F0;
    border-radius: 24px;
    padding: 20px;
    margin-bottom: 26px;
    box-shadow: 0 12px 32px rgba(15, 23, 42, 0.06);
}

.search-label {
    color: #0F172A;
    font-size: 15px;
    font-weight: 800;
    margin-bottom: 10px;
}

.search-box {
    width: 100%;
    padding: 15px 18px;
    border-radius: 16px;
    border: 1px solid #CBD5E1;
    font-size: 15px;
    color: #334155;
    background: #F8FAFC;
}

.section-title {
    margin-bottom: 20px;
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

.routes {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 26px;
}

.route-card {
    background: rgba(255,255,255,0.94);
    border-radius: 28px;
    padding: 26px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 14px 35px rgba(15, 23, 42, 0.07);
    min-height: 330px;
    display: flex;
    flex-direction: column;
    transition: all 0.28s ease;
}

.route-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 22px 50px rgba(37, 99, 235, 0.18);
    border-color: #60A5FA;
}

.route-card.popular {
    border: 2px solid #2563EB;
    box-shadow: 0 22px 55px rgba(37, 99, 235, 0.20);
}

.badge {
    width: fit-content;
    background: #DBEAFE;
    color: #2563EB;
    padding: 7px 13px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 18px;
}

.flags {
    font-size: 38px;
    margin-bottom: 16px;
}

.route-title {
    color: #0F172A;
    font-size: 25px;
    font-weight: 900;
    margin-bottom: 8px;
}

.route-desc {
    color: #64748B;
    font-size: 15px;
    line-height: 1.5;
    margin-bottom: 18px;
}

.rate {
    color: #2563EB;
    font-size: 34px;
    font-weight: 900;
    margin-bottom: 14px;
}

.feature {
    color: #334155;
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 9px;
}

.spacer {
    flex: 1;
}

.actions {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 18px;
}

.primary-btn,
.secondary-btn {
    border: none;
    border-radius: 15px;
    padding: 14px 12px;
    font-size: 14px;
    font-weight: 900;
    cursor: pointer;
}

.primary-btn {
    background: linear-gradient(135deg, #2563EB, #06B6D4);
    color: white;
    box-shadow: 0 12px 26px rgba(37, 99, 235, 0.22);
}

.secondary-btn {
    background: #EFF6FF;
    color: #2563EB;
}

.table-card {
    margin-top: 34px;
    background: rgba(255,255,255,0.94);
    border: 1px solid #E2E8F0;
    border-radius: 26px;
    padding: 24px;
    box-shadow: 0 12px 32px rgba(15, 23, 42, 0.06);
}

.table-card h3 {
    margin: 0 0 18px;
    color: #0F172A;
    font-size: 22px;
    font-weight: 900;
}

.rate-row {
    display: grid;
    grid-template-columns: 1.5fr 1fr 1fr;
    padding: 14px 0;
    border-bottom: 1px solid #E2E8F0;
    color: #334155;
    font-size: 15px;
    font-weight: 700;
}

.rate-row:last-child {
    border-bottom: none;
}

.header-row {
    color: #64748B;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}

@media(max-width: 900px) {
    .hero {
        grid-template-columns: 1fr;
    }

    .routes {
        grid-template-columns: 1fr;
    }

    .hero h1 {
        font-size: 34px;
    }

    .rate-row {
        grid-template-columns: 1fr;
        gap: 6px;
    }
}
</style>
</head>

<body>
<div class="wrapper">

    <div class="hero">
        <div>
            <div class="icon-box">🌍</div>
            <h1>International Calls</h1>
            <p>Call abroad with clear rates and quick country packages.</p>
        </div>

        <div class="balance-box">
            <div class="balance-label">International Balance</div>
            <div class="balance-number">3.50 JD</div>
            <div class="balance-meta">Enough for around 29 minutes to Saudi Arabia</div>
        </div>
    </div>

    <div class="search-card">
        <div class="search-label">Search destination</div>
        <input class="search-box" placeholder="Search country, e.g. Saudi Arabia, UAE, Egypt..." />
    </div>

    <div class="section-title">
        <h2>Popular Destinations</h2>
        <p>Quick access to the most used international calling routes.</p>
    </div>

    <div class="routes">

        <div class="route-card popular">
            <div class="badge">Most Used</div>
            <div class="flags">🇯🇴 → 🇸🇦</div>
            <div class="route-title">Saudi Arabia</div>
            <div class="route-desc">Best for frequent family and business calls.</div>
            <div class="rate">0.12 JD/min</div>
            <div class="feature">✓ Clear per-minute rate</div>
            <div class="feature">✓ Package available</div>
            <div class="spacer"></div>
            <div class="actions">
                <button class="primary-btn">Call Now</button>
                <button class="secondary-btn">Buy Pack</button>
            </div>
        </div>

        <div class="route-card">
            <div class="badge">Business</div>
            <div class="flags">🇯🇴 → 🇦🇪</div>
            <div class="route-title">UAE</div>
            <div class="route-desc">Suitable for work calls and daily contact.</div>
            <div class="rate">0.15 JD/min</div>
            <div class="feature">✓ Stable call quality</div>
            <div class="feature">✓ Package available</div>
            <div class="spacer"></div>
            <div class="actions">
                <button class="primary-btn">Call Now</button>
                <button class="secondary-btn">Buy Pack</button>
            </div>
        </div>

        <div class="route-card">
            <div class="badge">Popular</div>
            <div class="flags">🇯🇴 → 🇪🇬</div>
            <div class="route-title">Egypt</div>
            <div class="route-desc">Affordable rates for regular calls.</div>
            <div class="rate">0.10 JD/min</div>
            <div class="feature">✓ Lowest shown rate</div>
            <div class="feature">✓ Package available</div>
            <div class="spacer"></div>
            <div class="actions">
                <button class="primary-btn">Call Now</button>
                <button class="secondary-btn">Buy Pack</button>
            </div>
        </div>

    </div>

    <div class="table-card">
        <h3>International Rates</h3>

        <div class="rate-row header-row">
            <div>Destination</div>
            <div>Rate</div>
            <div>Best Option</div>
        </div>

        <div class="rate-row">
            <div>🇸🇦 Saudi Arabia</div>
            <div>0.12 JD/min</div>
            <div>Weekly Pack</div>
        </div>

        <div class="rate-row">
            <div>🇦🇪 UAE</div>
            <div>0.15 JD/min</div>
            <div>Business Pack</div>
        </div>

        <div class="rate-row">
            <div>🇪🇬 Egypt</div>
            <div>0.10 JD/min</div>
            <div>Value Pack</div>
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
