import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Internet Packages",
    page_icon="📶",
    layout="wide"
)

# ---------------- BACK BUTTON ---------------- #

col1, col2 = st.columns([1, 8])

with col1:
    if st.button("← Back"):
        st.switch_page("2_Customer.py")
        # إذا داخل pages استخدم:
        # st.switch_page("pages/2_Customer.py")

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
        radial-gradient(circle at 15% 20%, rgba(37, 99, 235, 0.14), transparent 28%),
        radial-gradient(circle at 85% 10%, rgba(6, 182, 212, 0.18), transparent 26%),
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

    display: grid;
    grid-template-columns: 1fr 320px;
    gap: 24px;

    align-items: center;

    box-shadow: 0 18px 45px rgba(37, 99, 235, 0.28);

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

.usage-box {
    background: rgba(255,255,255,0.17);

    border: 1px solid rgba(255,255,255,0.28);

    border-radius: 22px;

    padding: 20px;
}

.usage-label {
    font-size: 13px;
    opacity: 0.88;
}

.usage-number {
    font-size: 30px;
    font-weight: 900;

    margin: 10px 0 14px;
}

.progress-track {
    height: 10px;

    border-radius: 999px;

    background: rgba(255,255,255,0.24);

    overflow: hidden;
}

.progress-fill {
    width: 78%;
    height: 100%;

    background: white;
}

.usage-meta {
    display: flex;
    justify-content: space-between;

    margin-top: 10px;

    font-size: 12px;
}

.current-plan {
    background: rgba(236, 253, 245, 0.92);

    color: #047857;

    padding: 16px 20px;

    border-radius: 20px;

    border: 1px solid #A7F3D0;

    font-weight: 800;

    margin-bottom: 30px;
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

.cards {
    display: grid;

    grid-template-columns: repeat(3, 1fr);

    gap: 28px;
}

.card {
    position: relative;

    background: rgba(255,255,255,0.92);

    border-radius: 28px;

    padding: 26px;

    min-height: 430px;

    border: 1px solid #E2E8F0;

    box-shadow: 0 14px 35px rgba(15, 23, 42, 0.07);

    display: flex;
    flex-direction: column;

    transition: all 0.28s ease;
}

.card:hover {
    transform: translateY(-8px) scale(1.02);

    box-shadow: 0 22px 50px rgba(37, 99, 235, 0.18);

    border-color: #60A5FA;
}

.recommended {
    border: 2px solid #2563EB;

    box-shadow: 0 22px 55px rgba(37, 99, 235, 0.20);

    transform: scale(1.02);
}

.ribbon {
    position: absolute;

    top: -14px;
    right: 22px;

    background: linear-gradient(135deg, #2563EB, #06B6D4);

    color: white;

    padding: 8px 14px;

    border-radius: 999px;

    font-size: 12px;
    font-weight: 900;
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

.package-icon {
    font-size: 40px;

    margin-bottom: 14px;
}

.package-title {
    font-size: 40px;
    font-weight: 900;

    color: #0F172A;

    margin-bottom: 8px;
}

.subtitle {
    color: #64748B;

    line-height: 1.5;

    font-size: 15px;

    min-height: 46px;

    margin-bottom: 18px;
}

.price {
    font-size: 40px;
    font-weight: 900;

    color: #2563EB;

    margin-bottom: 20px;
}

.feature {
    color: #334155;

    font-size: 15px;
    font-weight: 700;

    margin-bottom: 10px;
}

.spacer {
    flex: 1;
}

button {
    width: 100%;

    border: none;

    border-radius: 16px;

    padding: 15px 18px;

    background: linear-gradient(135deg, #2563EB, #06B6D4);

    color: white;

    font-size: 15px;
    font-weight: 900;

    cursor: pointer;

    box-shadow: 0 12px 26px rgba(37, 99, 235, 0.22);

    transition: all 0.25s ease;
}

button:hover {
    transform: translateY(-2px);

    background: linear-gradient(135deg, #1D4ED8, #0891B2);
}

.recommend-box {
    margin-top: 34px;

    background: rgba(255,255,255,0.9);

    border-radius: 26px;

    padding: 24px;

    border: 1px solid #E2E8F0;

    box-shadow: 0 12px 32px rgba(15, 23, 42, 0.06);
}

.recommend-box h3 {
    margin: 0 0 8px;

    font-size: 22px;
    font-weight: 900;

    color: #0F172A;
}

.recommend-box p {
    margin: 0;

    color: #64748B;

    font-size: 15px;
}

@media(max-width: 900px) {

    .hero {
        grid-template-columns: 1fr;
    }

    .cards {
        grid-template-columns: 1fr;
    }

    .hero h1 {
        font-size: 34px;
    }

    .recommended {
        transform: none;
    }
}

</style>

</head>

<body>

<div class="wrapper">

    <div class="hero">

        <div>

            <div class="icon-box">📶</div>

            <h1>Internet Packages</h1>

            <p>
                Choose the best plan based on your internet usage.
            </p>

        </div>

        <div class="usage-box">

            <div class="usage-label">
                Remaining Data
            </div>

            <div class="usage-number">
                4.7 GB / 6 GB
            </div>

            <div class="progress-track">
                <div class="progress-fill"></div>
            </div>

            <div class="usage-meta">
                <span>78% remaining</span>
                <span>Renews in 12 days</span>
            </div>

        </div>

    </div>

    <div class="current-plan">
        ✅ Current Plan: 6 GB Package — Valid until May 25, 2024
    </div>

    <div class="section-title">

        <h2>Available Packages</h2>

        <p>
            Pick a plan. The 15 GB package is recommended for most users.
        </p>

    </div>

    <div class="cards">

        <div class="card">

            <div class="badge">Basic</div>

            <div class="package-icon">📱</div>

            <div class="package-title">6 GB</div>

            <div class="subtitle">
                Light browsing and social media.
            </div>

            <div class="price">5 JD</div>

            <div class="feature">✓ 6 GB Data</div>
            <div class="feature">✓ 5G Support</div>
            <div class="feature">✓ Valid for 30 Days</div>

            <div class="spacer"></div>

            <button>
                Subscribe 6 GB
            </button>

        </div>

        <div class="card recommended">

            <div class="ribbon">
                Recommended
            </div>

            <div class="badge">
                Most Popular
            </div>

            <div class="package-icon">
                🚀
            </div>

            <div class="package-title">
                15 GB
            </div>

            <div class="subtitle">
                Best value for daily usage.
            </div>

            <div class="price">
                10 JD
            </div>

            <div class="feature">✓ 15 GB Data</div>
            <div class="feature">✓ Fast Speed</div>
            <div class="feature">✓ Valid for 30 Days</div>

            <div class="spacer"></div>

            <button>
                Subscribe 15 GB
            </button>

        </div>

        <div class="card">

            <div class="badge">
                Premium
            </div>

            <div class="package-icon">
                🔥
            </div>

            <div class="package-title">
                Unlimited
            </div>

            <div class="subtitle">
                Streaming, gaming, and heavy usage.
            </div>

            <div class="price">
                25 JD
            </div>

            <div class="feature">✓ Unlimited Data</div>
            <div class="feature">✓ Priority Network</div>
            <div class="feature">✓ Valid for 30 Days</div>

            <div class="spacer"></div>

            <button>
                Subscribe Unlimited
            </button>

        </div>

    </div>

    <div class="recommend-box">

        <h3>
            Recommended For You: 15 GB Package
        </h3>

        <p>
            Based on your current usage, the 15 GB plan gives better value than renewing the 6 GB package repeatedly.
        </p>

    </div>

</div>

</body>
</html>
"""

components.html(
    html_code,
    height=1100,
    scrolling=True
)
