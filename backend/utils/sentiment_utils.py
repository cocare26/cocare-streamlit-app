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


def normalize_sentiment(label):
    label = str(label).lower().strip()

    if label in ["positive", "pos", "label_2", "2", "ايجابي", "إيجابي"]:
        return "positive"

    if label in ["negative", "neg", "label_0", "0", "سلبي"]:
        return "negative"

    return "neutral"


def predict_sentiment(text: str, lang: str = "ar"):
    text = clean_text(text)

    model = sentiment_model_ar if lang == "ar" else sentiment_model_en

    if model is None:
        return "neutral", 0.0

    try:
        pred = model.predict([text])[0]
        sentiment = normalize_sentiment(pred)

        if hasattr(model, "predict_proba"):
            score = float(max(model.predict_proba([text])[0]))
        else:
            score = 1.0

        return sentiment, score

    except Exception:
        return "neutral", 0.0
