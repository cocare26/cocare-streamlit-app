import streamlit as st

st.set_page_config(
    page_title="Internet Packages",
    page_icon="📶",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 15% 20%, rgba(37, 99, 235, 0.14), transparent 28%),
        radial-gradient(circle at 85% 10%, rgba(6, 182, 212, 0.18), transparent 26%),
        linear-gradient(180deg, #F5F9FF 0%, #FFFFFF 100%);
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.back-btn {
    display: inline-flex;
    padding: 10px 18px;
    border-radius: 14px;
    border: 1px solid #BFDBFE;
    color: #2563EB;
    background: white;
    font-weight: 700;
    margin-bottom: 22px;
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
}

.hero {
    background: linear-gradient(135deg, #2563EB, #06B6D4);
    padding: 30px;
    border-radius: 30px;
    color: white;
    margin-bottom: 22px;
    box-shadow: 0 18px 45px rgba(37, 99, 235, 0.28);
}

.hero-grid {
    display: grid;
    grid-template-columns: 1fr 300px;
    gap: 24px;
    align-items: center;
}

.hero-icon {
    width: 58px;
    height: 58px;
    border-radius: 18px;
    background: rgba(255,255,255,0.18);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 30px;
    margin-bottom: 16px;
}

.hero h1 {
    margin: 0;
    font-size: 42px;
    font-weight: 900;
}

.hero p {
    margin-top: 9px;
    font-size: 17px;
    opacity: 0.92;
}

.usage-box {
    background: rgba(255,255,255,0.17);
    border: 1px solid rgba(255,255,255,0.28);
    border-radius: 22px;
    padding: 18px;
}

.usage-label {
    font-size: 13px;
    opacity: 0.86;
    margin-bottom: 8px;
}

.usage-number {
    font-size: 28px;
    font-weight: 900;
    margin-bottom: 12px;
}

.progress-track {
    height: 10px;
    border-radius: 999px;
    background: rgba(255,255,255,0.25);
    overflow: hidden;
}

.progress-fill {
    width: 78%;
    height: 100%;
    background: white;
    border-radius: 999px;
}

.usage-meta {
    display: flex;
    justify-content: space-between;
    margin-top: 10px;
    font-size: 12px;
    opacity: 0.9;
}

.current-plan {
    background: rgba(236, 253, 245, 0.9);
    color: #047857;
    padding: 16px 20px;
    border-radius: 20px;
    border: 1px solid #A7F3D0;
    margin-bottom: 24px;
    font-weight: 800;
}

.section-header h2 {
    margin: 0;
    color: #0F172A;
    font-size: 28px;
    font-weight: 900;
}

.section-header p {
    margin-top: 6px;
    color: #64748B;
    font-size: 15px;
}

.package-card {
    position: relative;
    background: white;
    padding: 24px;
    border-radius: 28px;
    border: 1px solid #E2E8F0;
    min-height: 390px;
    box-shadow: 0 14px 35px rgba(15, 23, 42, 0.07);
    transition: all 0.28s ease;
    margin-top: 18px;
}

.package-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 22px 50px rgba(37, 99, 235, 0.18);
    border-color: #60A5FA;
}

.package-card.recommended {
    border: 2px solid #2563EB;
    box-shadow: 0 22px 55px rgba(37, 99, 235, 0.20);
}

.recommend-ribbon {
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
    display: inline-flex;
    background: #DBEAFE;
    color: #2563EB;
    padding: 7px 13px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 18px;
}

.package-icon {
    font-size: 36px;
    margin-bottom: 14px;
}

.package-title {
    font-size: 36px;
    font-weight: 900;
    color: #0F172A;
    margin-bottom: 6px;
}

.package-subtitle {
    color: #64748B;
    font-size: 15px;
    line-height: 1.5;
    min-height: 44px;
    margin-bottom: 16px;
}

.price {
    font-size: 38px;
    font-weight: 900;
    color: #2563EB;
    margin-bottom: 18px;
}

.feature {
    color: #334155;
    font-size: 15px;
    margin-bottom: 10px;
    font-weight: 600;
}

div.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #2563EB, #06B6D4);
    color: white;
    border: none;
    border-radius: 16px;
    padding: 14px 18px;
    font-weight: 900;
    font-size: 15px;
    box-shadow: 0 12px 26px rgba(37, 99, 235, 0.22);
    margin-top: -75px;
    position: relative;
    z-index: 5;
}

div.stButton > button:hover {
    background: linear-gradient(135deg, #1D4ED8, #0891B2);
    color: white;
    transform: translateY(-2px);
}

.button-space {
    height: 86px;
}

.recommend-box {
    margin-top: 34px;
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 26px;
    padding: 22px;
    box-shadow: 0 12px 32px rgba(15, 23, 42, 0.06);
}

.recommend-box h3 {
    margin: 0 0 8px 0;
    color: #0F172A;
    font-size: 22px;
    font-weight: 900;
}

.recommend-box p {
    margin: 0;
    color: #64748B;
    font-size: 15px;
}

@media (max-width: 900px) {
    .hero-grid {
        grid-template-columns: 1fr;
    }

    .hero h1 {
        font-size: 34px;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="back-btn">← Back</div>', unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-grid">
        <div>
            <div class="hero-icon">📶</div>
            <h1>Internet Packages</h1>
            <p>Choose the best plan based on your internet usage.</p>
        </div>

        <div class="usage-box">
            <div class="usage-label">Remaining Data</div>
            <div class="usage-number">4.7 GB / 6 GB</div>
            <div class="progress-track">
                <div class="progress-fill"></div>
            </div>
            <div class="usage-meta">
                <span>78% remaining</span>
                <span>Renews in 12 days</span>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="current-plan">
    ✅ Current Plan: 6 GB Package — Valid until May 25, 2024
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    <h2>Available Packages</h2>
    <p>Pick a plan. The 15 GB package is recommended for most users.</p>
</div>
""", unsafe_allow_html=True)

packages = [
    {
        "badge": "Basic",
        "icon": "📱",
        "title": "6 GB",
        "subtitle": "Light browsing and social media.",
        "price": "5 JD",
        "features": ["6 GB Data", "5G Support", "Valid for 30 Days"],
        "button": "Subscribe 6 GB",
        "recommended": False
    },
    {
        "badge": "Most Popular",
        "icon": "🚀",
        "title": "15 GB",
        "subtitle": "Best value for daily usage.",
        "price": "10 JD",
        "features": ["15 GB Data", "Fast Speed", "Valid for 30 Days"],
        "button": "Subscribe 15 GB",
        "recommended": True
    },
    {
        "badge": "Premium",
        "icon": "🔥",
        "title": "Unlimited",
        "subtitle": "Streaming, gaming, and heavy use.",
        "price": "25 JD",
        "features": ["Unlimited Data", "Priority Network", "Valid for 30 Days"],
        "button": "Subscribe Unlimited",
        "recommended": False
    }
]

cols = st.columns(3, gap="large")

for col, package in zip(cols, packages):
    with col:
        recommended_class = "recommended" if package["recommended"] else ""
        ribbon = '<div class="recommend-ribbon">Recommended</div>' if package["recommended"] else ""

        features_html = "".join(
            [f'<div class="feature">✓ {feature}</div>' for feature in package["features"]]
        )

        st.markdown(f"""
        <div class="package-card {recommended_class}">
            {ribbon}
            <div class="badge">{package["badge"]}</div>
            <div class="package-icon">{package["icon"]}</div>
            <div class="package-title">{package["title"]}</div>
            <div class="package-subtitle">{package["subtitle"]}</div>
            <div class="price">{package["price"]}</div>
            <div class="features">
                {features_html}
            </div>
            <div class="button-space"></div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(package["button"], key=package["button"]):
            st.success(f"You selected the {package['title']} package.")

st.markdown("""
<div class="recommend-box">
    <h3>Recommended For You: 15 GB Package</h3>
    <p>Based on your current usage, the 15 GB plan gives better value than renewing the 6 GB plan repeatedly.</p>
</div>
""", unsafe_allow_html=True)
