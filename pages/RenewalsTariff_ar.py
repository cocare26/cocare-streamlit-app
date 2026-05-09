import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="التجديدات والتعرفة",
    page_icon="🔄",
    layout="wide"
)

col1, col2 = st.columns([1, 8])

with col1:
    if st.button("← رجوع"):
        st.switch_page("pages/Customer_ar.py")

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
    display: grid;
    grid-template-columns: 1fr 320px;
    gap: 24px;
    align-items: center;
    box-shadow: 0 18px 45px rgba(37, 99, 235, 0.28);
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

.plan-box {
    background: rgba(255,255,255,0.17);
    border: 1px solid rgba(255,255,255,0.28);
    border-radius: 22px;
    padding: 20px;
}

.plan-label {
    font-size: 13px;
    opacity: 0.88;
}

.plan-name {
    font-size: 30px;
    font-weight: 900;
    margin: 8px 0;
}

.plan-meta {
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

.actions-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 26px;
}

.action-card {
    background: rgba(255,255,255,0.94);
    border-radius: 28px;
    padding: 28px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 14px 35px rgba(15, 23, 42, 0.07);
    min-height: 340px;
    display: flex;
    flex-direction: column;
    transition: all 0.28s ease;
}

.action-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 22px 50px rgba(37, 99, 235, 0.18);
    border-color: #60A5FA;
}

.recommended {
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

.card-icon {
    font-size: 42px;
    margin-bottom: 16px;
}

.card-title {
    color: #0F172A;
    font-size: 28px;
    font-weight: 900;
    margin-bottom: 10px;
}

.card-desc {
    color: #64748B;
    line-height: 1.7;
    font-size: 15px;
    margin-bottom: 18px;
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

.primary-btn {
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

.primary-btn:hover {
    transform: translateY(-2px);
    background: linear-gradient(135deg, #1D4ED8, #0891B2);
}

.offer-card {
    margin-top: 34px;
    background: linear-gradient(135deg, #2563EB, #06B6D4);
    color: white;
    border-radius: 28px;
    padding: 28px;
    box-shadow: 0 18px 45px rgba(37, 99, 235, 0.25);
}

.offer-card h3 {
    margin: 0 0 10px;
    font-size: 28px;
    font-weight: 900;
}

.offer-card p {
    margin: 0 0 20px;
    opacity: 0.92;
    font-size: 15px;
}

.offer-btn {
    background: white;
    color: #2563EB;
    border: none;
    border-radius: 16px;
    padding: 14px 22px;
    font-size: 14px;
    font-weight: 900;
    cursor: pointer;
}

@media(max-width: 900px) {
    .hero,
    .summary-grid,
    .actions-grid {
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
            <div class="icon-box">🔄</div>
            <h1>التجديدات والتعرفة</h1>
            <p>إدارة الاشتراكات، تجديد الباقات، وتفعيل العروض الجديدة.</p>
        </div>

        <div class="plan-box">
            <div class="plan-label">الباقة الحالية</div>
            <div class="plan-name">باقة 15 جيجابايت</div>
            <div class="plan-meta">تتجدد خلال 12 يوم · التجديد التلقائي مفعّل</div>
        </div>
    </div>

    <div class="summary-grid">
        <div class="summary-card">
            <div class="summary-label">الرصيد الحالي</div>
            <div class="summary-value">18 د.أ</div>
        </div>

        <div class="summary-card">
            <div class="summary-label">موعد التجديد القادم</div>
            <div class="summary-value">25 مايو</div>
        </div>

        <div class="summary-card">
            <div class="summary-label">العروض النشطة</div>
            <div class="summary-value">2</div>
        </div>
    </div>

    <div class="section-title">
        <h2>إدارة الباقة</h2>
        <p>جدّد باقتك، غيّر التعرفة، أو فعّل عرضًا جديدًا.</p>
    </div>

    <div class="actions-grid">

        <div class="action-card recommended">
            <div class="badge">مقترح</div>
            <div class="card-icon">🔁</div>
            <div class="card-title">تجديد الباقة</div>
            <div class="card-desc">جدّد باقتك الشهرية الحالية فورًا بدون انقطاع الخدمة.</div>

            <div class="feature">✓ تجديد فوري</div>
            <div class="feature">✓ بدون انقطاع</div>
            <div class="feature">✓ الحفاظ على نفس الإعدادات</div>

            <div class="spacer"></div>

            <button class="primary-btn">جدّد الآن</button>
        </div>

        <div class="action-card">
            <div class="badge">ترقية</div>
            <div class="card-icon">📈</div>
            <div class="card-title">تغيير التعرفة</div>
            <div class="card-desc">انتقل إلى باقة أخرى حسب استهلاكك واحتياجك.</div>

            <div class="feature">✓ خيارات بيانات أكثر</div>
            <div class="feature">✓ أسعار مرنة</div>
            <div class="feature">✓ تفعيل فوري</div>

            <div class="spacer"></div>

            <button class="primary-btn">غيّر الباقة</button>
        </div>

        <div class="action-card">
            <div class="badge">عرض جديد</div>
            <div class="card-icon">🎁</div>
            <div class="card-title">تفعيل عرض</div>
            <div class="card-desc">فعّل عروضًا مؤقتة وباقات إنترنت إضافية.</div>

            <div class="feature">✓ جيجابايت إضافية</div>
            <div class="feature">✓ خصومات لفترة محدودة</div>
            <div class="feature">✓ تفعيل مباشر</div>

            <div class="spacer"></div>

            <button class="primary-btn">عرض العروض</button>
        </div>

    </div>

    <div class="offer-card">
        <h3>عرض خاص: ضعف البيانات في نهاية الأسبوع</h3>
        <p>فعّل العرض الآن واحصل على ضعف استخدام الإنترنت خلال نهاية الأسبوع بدون تكلفة إضافية.</p>
        <button class="offer-btn">تفعيل العرض</button>
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
