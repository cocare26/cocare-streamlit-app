import streamlit as st

st.set_page_config(page_title="Internet Packages", layout="wide")

st.markdown("""
<style>
body {
    background-color: #F5F9FF;
}

.main {
    background: linear-gradient(180deg, #EEF6FF 0%, #FFFFFF 100%);
}

.back-btn {
    display: inline-block;
    padding: 10px 18px;
    border-radius: 14px;
    border: 1px solid #2563EB;
    color: #2563EB;
    font-weight: 600;
    margin-bottom: 25px;
}

.hero {
    background: linear-gradient(135deg, #2563EB, #06B6D4);
    padding: 28px;
    border-radius: 28px;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0 12px 30px rgba(37, 99, 235, 0.25);
}

.hero h1 {
    margin: 0;
    font-size: 38px;
    font-weight: 800;
}

.hero p {
    margin-top: 8px;
    font-size: 17px;
    opacity: 0.9;
}

.package-card {
    background: white;
    padding: 26px;
    border-radius: 26px;
    box-shadow: 0 10px 25px rgba(15, 23, 42, 0.08);
    border: 1px solid #E5E7EB;
    min-height: 310px;
    transition: 0.25s ease;
}

.package-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 16px 35px rgba(37, 99, 235, 0.18);
    border-color: #2563EB;
}

.badge {
    display: inline-block;
    background: #DBEAFE;
    color: #2563EB;
    padding: 7px 13px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 18px;
}

.package-title {
    font-size: 30px;
    font-weight: 800;
    color: #0F172A;
    margin-bottom: 6px;
}

.package-subtitle {
    color: #64748B;
    font-size: 15px;
    margin-bottom: 18px;
}

.price {
    font-size: 34px;
    font-weight: 900;
    color: #2563EB;
    margin-bottom: 18px;
}

.feature {
    color: #334155;
    font-size: 15px;
    margin-bottom: 8px;
}

.subscribe-btn {
    margin-top: 22px;
}

div.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #2563EB, #06B6D4);
    color: white;
    border: none;
    border-radius: 16px;
    padding: 13px 18px;
    font-weight: 800;
    font-size: 15px;
}

div.stButton > button:hover {
    background: linear-gradient(135deg, #1D4ED8, #0891B2);
    color: white;
}

.current-plan {
    background: #ECFDF5;
    color: #047857;
    padding: 18px 22px;
    border-radius: 22px;
    border: 1px solid #A7F3D0;
    margin-bottom: 26px;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="back-btn">← Back</div>', unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>📶 Internet Packages</h1>
    <p>Choose the best internet plan for your daily usage.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="current-plan">
    ✅ Current Plan: 6 GB Package — Valid until May 25, 2024
</div>
""", unsafe_allow_html=True)

packages = [
    {
        "badge": "Basic",
        "title": "6 GB",
        "subtitle": "Good for light browsing and social media.",
        "price": "5 JD",
        "features": ["✔ 6 GB Data", "✔ 5G Support", "✔ Valid for 30 Days"],
        "button": "Subscribe 6 GB"
    },
    {
        "badge": "Most Popular",
        "title": "15 GB",
        "subtitle": "Best choice for daily internet users.",
        "price": "10 JD",
        "features": ["✔ 15 GB Data", "✔ Fast Speed", "✔ Valid for 30 Days"],
        "button": "Subscribe 15 GB"
    },
    {
        "badge": "Premium",
        "title": "Unlimited",
        "subtitle": "For heavy usage, streaming, and gaming.",
        "price": "25 JD",
        "features": ["✔ Unlimited Data", "✔ Priority Network", "✔ Valid for 30 Days"],
        "button": "Subscribe Unlimited"
    }
]

cols = st.columns(3)

for col, package in zip(cols, packages):
    with col:
        st.markdown(f"""
        <div class="package-card">
            <div class="badge">{package["badge"]}</div>
            <div class="package-title">{package["title"]}</div>
            <div class="package-subtitle">{package["subtitle"]}</div>
            <div class="price">{package["price"]}</div>
            <div>
                {''.join([f'<div class="feature">{feature}</div>' for feature in package["features"]])}
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(package["button"]):
            st.success(f"You selected {package['title']} package.")
