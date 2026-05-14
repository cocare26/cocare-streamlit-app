from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional

from cocare import process_message
from database.db_helper import fetch_all


app = FastAPI(
    title="CoCare Backend API",
    description="AI Telecom Support Backend",
    version="1.0.0"
)

# =========================
# CORS
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# =========================
# Chat API
# =========================
@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):

    if not req.message.strip():
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty"
        )

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
            detail=str(e)
        )


# =========================
# Employee Dashboard APIs
# =========================
@app.get("/chat-logs")
def get_chat_logs(limit: int = 100):

    rows = fetch_all(f"""
        SELECT *
        FROM chat_logs
        ORDER BY id DESC
        LIMIT {limit}
    """)

    logs = [dict(row) for row in rows]

    return {
        "count": len(logs),
        "logs": logs
    }


@app.get("/alerts")
def get_alerts():

    rows = fetch_all("""
        SELECT *
        FROM chat_logs
        WHERE network_problem = 1
        OR escalation = 1
        OR notification_type != 'none'
        ORDER BY id DESC
        LIMIT 100
    """)

    alerts = [dict(row) for row in rows]

    return {
        "count": len(alerts),
        "alerts": alerts
    }


@app.get("/stats")
def get_stats():

    total_messages = fetch_all("""
        SELECT COUNT(*) as total
        FROM chat_logs
    """)[0]["total"]

    network_issues = fetch_all("""
        SELECT COUNT(*) as total
        FROM chat_logs
        WHERE network_problem = 1
    """)[0]["total"]

    escalations = fetch_all("""
        SELECT COUNT(*) as total
        FROM chat_logs
        WHERE escalation = 1
    """)[0]["total"]

    internal_notifications = fetch_all("""
        SELECT COUNT(*) as total
        FROM chat_logs
        WHERE notification_type = 'internal_noti'
    """)[0]["total"]

    external_notifications = fetch_all("""
        SELECT COUNT(*) as total
        FROM chat_logs
        WHERE notification_type = 'external_noti'
    """)[0]["total"]

    return {
        "total_messages": total_messages,
        "network_issues": network_issues,
        "escalations": escalations,
        "internal_notifications": internal_notifications,
        "external_notifications": external_notifications
    }


# =========================
# Test Route
# =========================
@app.get("/test-chat")
def test_chat():

    return process_message(
        user_message="My internet is very slow",
        user_id="test_user",
        region="Amman"
    )
