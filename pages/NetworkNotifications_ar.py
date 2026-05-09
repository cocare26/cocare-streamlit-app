import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="مركز التنبيهات",
    page_icon="🔔",
    layout="wide"
)

# ---------------- BACK BUTTON ---------------- #

col1, col2 = st.columns([1, 8])

with col1:
    if st.button("← رجوع"):
        st.switch_page("pages/Customer_ar.py")

# ---------------- HTML UI ---------------- #

html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>

<style>

@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&display=swap');

* {
    box-sizing: border-box;
    font-family: 'Cairo', sans-serif;
}

body {
    margin: 0;
    padding: 28px;

    direction: rtl;
    text-align: right;

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

    grid-template-columns: auto 1fr 58px;

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

    line-height: 1.7;
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

            <h1>مركز التنبيهات</h1>

            <p>
                تابع تنبيهات الخدمة، تحديثات الباقات، وحالة الشبكة بشكل مباشر.
            </p>

        </div>

        <div class="status-box">

            <div class="status-label">
                الحالة الحالية
            </div>

            <div class="status-number">
                جميع الأنظمة تعمل
            </div>

            <div class="status-meta">
                الشبكة مستقرة · عمّان · تغطية ممتازة
            </div>

        </div>

    </div>

    <div class="summary-grid">

        <div class="summary-card">
            <div class="summary-label">التنبيهات غير المقروءة</div>
            <div class="summary-value">3</div>
        </div>

        <div class="summary-card">
            <div class="summary-label">قوة الإشارة</div>
            <div class="summary-value">ممتازة</div>
        </div>

        <div class="summary-card">
            <div class="summary-label">حالة الشبكة</div>
            <div class="summary-value">مستقرة</div>
        </div>

    </div>

    <div class="section-title">

        <h2>آخر التنبيهات</h2>

        <p>
            آخر التحديثات المتعلقة بخدمتك واتصال الإنترنت.
        </p>

    </div>

    <div class="notifications">

        <div class="notification info">

            <div class="n-time">
                اليوم
            </div>

            <div>

                <div class="n-title">
                    صيانة مجدولة
                </div>

                <div class="n-desc">
                    يوجد صيانة للشبكة في عمّان الليلة من الساعة 1 صباحًا حتى 3 صباحًا.
                </div>

                <div class="badge">
                    صيانة
                </div>

            </div>

            <div class="n-icon">🛠️</div>

        </div>

        <div class="notification warning">

            <div class="n-time">
                قبل ساعتين
            </div>

            <div>

                <div class="n-title">
                    تم اكتشاف ضعف في الإشارة
                </div>

                <div class="n-desc">
                    جودة الإشارة أقل من المعتاد في منطقتك.
                </div>

                <div class="badge">
                    تحذير
                </div>

            </div>

            <div class="n-icon">⚠️</div>

        </div>

        <div class="notification success">

            <div class="n-time">
                أمس
            </div>

            <div>

                <div class="n-title">
                    تم تجديد الباقة بنجاح
                </div>

                <div class="n-desc">
                    تم تجديد باقة الإنترنت الخاصة بك بنجاح.
                </div>

                <div class="badge">
                    ناجح
                </div>

            </div>

            <div class="n-icon">✅</div>

        </div>

    </div>

    <div class="network-card">

        <h3>
            أداء الشبكة
        </h3>

        <div class="metrics">

            <div class="metric">
                <div class="metric-label">فقدان الحزم</div>
                <div class="metric-value">0%</div>
            </div>

            <div class="metric">
                <div class="metric-label">الاستجابة</div>
                <div class="metric-value">19 ms</div>
            </div>

            <div class="metric">
                <div class="metric-label">الإشارة</div>
                <div class="metric-value">-68 dBm</div>
            </div>

            <div class="metric">
                <div class="metric-label">التغطية</div>
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
