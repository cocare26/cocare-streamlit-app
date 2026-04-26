# -*- coding: utf-8 -*-

import streamlit as st

st.set_page_config(
    page_title="CoCare Chatbot",
    page_icon="💬",
    layout="centered"
)

st.title("CoCare Chatbot")
st.write("نظام شات بوت ذكي لخدمات الاتصالات")

# =========================
# Import chatbot engine
# =========================

try:
    from chatbot_engine import process_message
    engine_ready = True
    engine_error = ""
except Exception as e:
    process_message = None
    engine_ready = False
    engine_error = str(e)


# =========================
# Sidebar
# =========================

with st.sidebar:
    st.header("حالة النظام")

    if engine_ready:
        st.success("Chatbot engine جاهز")
    else:
        st.error("Chatbot engine غير جاهز")

    with st.expander("تفاصيل الأخطاء"):
        if engine_error:
            st.code(engine_error)


# =========================
# Main UI
# =========================

st.subheader("تجربة الشات بوت")

user_text = st.text_area("اكتبي رسالة العميل هنا", height=120)

use_metrics = st.checkbox("إضافة بيانات الشبكة للتنبؤ بالمشكلة")

metrics = None

if use_metrics:
    col1, col2 = st.columns(2)

    with col1:
        latency = st.number_input("Latency", min_value=0.0, value=0.0)
        packet_loss = st.number_input("Packet loss", min_value=0.0, value=0.0)

    with col2:
        signal_strength = st.number_input("Signal strength", value=0.0)
        connected_users = st.number_input("Connected users", min_value=0, value=0)

    metrics = {
        "latency": latency,
        "packet_loss": packet_loss,
        "signal_strength": signal_strength,
        "connected_users": connected_users,
    }


if st.button("إرسال"):
    if not user_text.strip():
        st.warning("اكتبي رسالة أولاً")

    elif not engine_ready:
        st.error("في مشكلة بتحميل chatbot_engine.py")
        st.code(engine_error)

    else:
        result = process_message(user_text, metrics)

        st.success("تم تحليل الرسالة")

        st.markdown("### الرد")
        st.write(result.get("response", ""))

        st.markdown("### نتائج التحليل")
        st.write("اللغة:", result.get("language"))
        st.write("Intent:", result.get("intent"))
        st.write("Intent confidence:", result.get("intent_confidence"))
        st.write("Sentiment:", result.get("sentiment"))
        st.write("Sentiment score:", result.get("sentiment_score"))
        st.write("Network prediction:", result.get("prediction"))
        st.write("Escalation:", result.get("escalation"))
        st.write("Notification type:", result.get("notification_type"))
