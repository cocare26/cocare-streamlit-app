import joblib
from utils.text_preprocessing import clean_text

SENTIMENT_MODEL_AR_PATH = "Sentiment_Ara/model.pkl"
SENTIMENT_MODEL_EN_PATH = "Sentiment_Eng/model.pkl"

try:
    sentiment_model_ar = joblib.load(SENTIMENT_MODEL_AR_PATH)
except Exception:
    sentiment_model_ar = None

try:
    sentiment_model_en = joblib.load(SENTIMENT_MODEL_EN_PATH)
except Exception:
    sentiment_model_en = None


def predict_sentiment(text: str, lang: str) -> str:
    text = clean_text(text)

    if lang == "ar":
        if sentiment_model_ar is None:
            return "neutral"
        return sentiment_model_ar.predict([text])[0]

    if sentiment_model_en is None:
        return "neutral"
    return sentiment_model_en.predict([text])[0]