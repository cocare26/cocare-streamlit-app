import os
import json
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from utils.text_preprocessing import clean_text


BASE_DIR = "/content/drive/MyDrive/CoCare"

AR_MODEL_PATH = os.path.join(BASE_DIR, "Intent_Ara", "intent_arabic")
EN_MODEL_PATH = os.path.join(BASE_DIR, "intent_Eng", "distilbert_intent_model_only")


# =========================
# LOAD LABEL MAPS
# =========================
def load_label_map(model_path):
    file_path = os.path.join(model_path, "id2label.json")

    if not os.path.exists(file_path):
        return None

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


# =========================
# LOAD MODELS
# =========================
tokenizer_ar = AutoTokenizer.from_pretrained(AR_MODEL_PATH)
model_ar = AutoModelForSequenceClassification.from_pretrained(
    AR_MODEL_PATH
)

tokenizer_en = AutoTokenizer.from_pretrained(EN_MODEL_PATH)
model_en = AutoModelForSequenceClassification.from_pretrained(
    EN_MODEL_PATH
)

id2label_ar = load_label_map(AR_MODEL_PATH)
id2label_en = load_label_map(EN_MODEL_PATH)


# =========================
# PREDICT
# =========================
def predict_with_transformer(text, tokenizer, model, label_map=None):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        outputs = model(**inputs)

    predicted_class = torch.argmax(outputs.logits, dim=1).item()

    # أولًا استخدم json mapping
    if label_map is not None:
        return label_map.get(str(predicted_class), "unknown")

    # fallback
    return "unknown"


def predict_intent(text: str, lang: str) -> str:
    text = clean_text(text)

    if lang == "ar":
        return predict_with_transformer(
            text,
            tokenizer_ar,
            model_ar,
            id2label_ar
        )

    return predict_with_transformer(
        text,
        tokenizer_en,
        model_en,
        id2label_en
    )