from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

def predict_intent(message: str):
    msg = message.lower()

    if "network" in msg or "internet slow" in msg or "connection" in msg:
        return "network_test"

    if "usage" in msg or "data" in msg:
        return "internet_usage"

    if "renew" in msg or "package" in msg:
        return "renew_package"

    if "international" in msg or "calls" in msg:
        return "international_calls"

    if "support" in msg or "agent" in msg:
        return "contact_support"

    return "unknown"

responses = {
    "network_test": "I will start a network test. Please wait while I check your connection.",
    "internet_usage": "You can check your remaining internet usage from your account dashboard.",
    "renew_package": "You can renew your package from the renewal section.",
    "international_calls": "International calls service is available in the services menu.",
    "contact_support": "I will connect you with customer support.",
    "unknown": "Sorry, I did not understand your request. Please try again."
}

@app.post("/chat")
def chat(req: ChatRequest):
    intent = predict_intent(req.message)
    reply = responses[intent]

    return {
        "intent": intent,
        "reply": reply
    }
