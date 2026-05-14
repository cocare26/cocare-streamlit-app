from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, Any, Dict
import pandas as pd
import os

from cocare import process_message, CHAT_LOG_PATH


app = FastAPI(
    title="CoCare Backend API",
    description="AI Telecom Support Backend for Chatbot, Analysis, Notifications, and Employee Dashboard",
    version="1.0.0"
)

# يسمح لتطبيق Flutter / Streamlit / Web يتصلوا بالباكند
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # لاحقاً ممكن تحددي رابط التطبيق فقط
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# Request Models
# =========================

class ChatRequest(BaseModel):
    user_id: str = Field(..., example="customer_1")
    message: str = Field(..., example="My internet is very slow")
    region: str = Field(..., example="Amman")


class ChatResponse(BaseModel):
    language: Optional[str] = None
    intent: Optional[str] = None
    intent_confidence: Optional[float] = None
    sentiment: Optional[str] = None
    sentiment_score: Optional[float] = None
    prediction: Optional[int] = None
    response: Optional[str] = None
    followup_response: Optional[str] = None
    issue_type: Optional[str] = None
    network_problem: Optional[bool] = None
    notification_type: Optional[str] = None
    display_channel: Optional[str] = None
    escalation: Optional[bool] = None
    reason: Optional[str] = None
    repeat_count: Optional[int] = None
    area_issue_count: Optional[int] = None
    external_message_ar: Optional[str] = None
    external_message_en: Optional[str] = None
    internal_message_ar: Optional[str] = None
    internal_message_en: Optional[str] = None
    priority: Optional[str] = None
    suggested_action: Optional[str] = None
    show_to_customer: Optional[int] = None
    user_id: Optional[str] = None
    region: Optional[str] = None


# =========================
# Basic Routes
# =========================

@app.get("/")
def home():
    return {
        "app": "CoCare Backend",
        "status": "running",
        "message": "Welcome to CoCare AI Telecom Support API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "CoCare Backend API"
    }


# =========================
# Chatbot API
# =========================

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    """
    يستقبل رسالة العميل من Flutter أو أي واجهة،
    يرسلها إلى process_message،
    ويرجع الرد + التحليل + الإشعارات.
    """

    if not req.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    try:
        result = process_message(
            user_message=req.message,
            user_id=req.user_id,
            region=req.region
        )

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error while processing message: {str(e)}"
        )


# =========================
# Employee Dashboard APIs
# =========================

@app.get("/chat-logs")
def get_chat_logs(limit: int = 100):
    """
    يرجع آخر المحادثات والتحليلات للـ Employee Dashboard.
    """

    if not os.path.exists(CHAT_LOG_PATH):
        return {
            "count": 0,
            "logs": []
        }

    try:
        df = pd.read_csv(CHAT_LOG_PATH, encoding="utf-8-sig")
        df = df.tail(limit)
        df = df.fillna("")

        return {
            "count": len(df),
            "logs": df.to_dict(orient="records")
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error reading chat logs: {str(e)}"
        )


@app.get("/alerts")
def get_alerts():
    """
    يرجع فقط المشاكل والتنبيهات المهمة للموظف.
    """

    if not os.path.exists(CHAT_LOG_PATH):
        return {
            "count": 0,
            "alerts": []
        }

    try:
        df = pd.read_csv(CHAT_LOG_PATH, encoding="utf-8-sig")
        df = df.fillna("")

        if "network_problem" not in df.columns:
            return {
                "count": 0,
                "alerts": []
            }

        alerts = df[
            (df["network_problem"].astype(str).str.lower().isin(["true", "1", "yes"])) |
            (df["notification_type"].astype(str) != "none") |
            (df["escalation"].astype(str).str.lower().isin(["true", "1", "yes"]))
        ]

        return {
            "count": len(alerts),
            "alerts": alerts.tail(100).to_dict(orient="records")
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error reading alerts: {str(e)}"
        )


@app.get("/stats")
def get_stats():
    """
    إحصائيات عامة للداشبورد.
    """

    if not os.path.exists(CHAT_LOG_PATH):
        return {
            "total_messages": 0,
            "network_issues": 0,
            "escalations": 0,
            "internal_notifications": 0,
            "external_notifications": 0
        }

    try:
        df = pd.read_csv(CHAT_LOG_PATH, encoding="utf-8-sig")
        df = df.fillna("")

        total_messages = len(df)

        network_issues = len(
            df[df.get("network_problem", "").astype(str).str.lower().isin(["true", "1", "yes"])]
        ) if "network_problem" in df.columns else 0

        escalations = len(
            df[df.get("escalation", "").astype(str).str.lower().isin(["true", "1", "yes"])]
        ) if "escalation" in df.columns else 0

        internal_notifications = len(
            df[df.get("notification_type", "").astype(str) == "internal_noti"]
        ) if "notification_type" in df.columns else 0

        external_notifications = len(
            df[df.get("notification_type", "").astype(str) == "external_noti"]
        ) if "notification_type" in df.columns else 0

        return {
            "total_messages": total_messages,
            "network_issues": network_issues,
            "escalations": escalations,
            "internal_notifications": internal_notifications,
            "external_notifications": external_notifications
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error calculating stats: {str(e)}"
        )


# =========================
# Test Route
# =========================

@app.get("/test-chat")
def test_chat():
    """
    اختبار سريع بدون Flutter.
    """

    try:
        result = process_message(
            user_message="My internet is very slow",
            user_id="test_user",
            region="Amman"
        )

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Test failed: {str(e)}"
        )
