import os
import json
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from utils.text_preprocessing import clean_text


BASE_DIR = "/content/drive/MyDrive/CoCare"

AR_MODEL_PATH = os.path.join(BASE_DIR, "Intent_Ara", "intent_arabic")
EN_MODEL_PATH = os.path.join(BASE_DIR, "intent_Eng", "distilbert_intent_model_only")


def load_label_map(model_path):
    file_path = os.path.join(model_path, "id2label.json")

    if not os.path.exists(file_path):
        return None

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


tokenizer_ar = AutoTokenizer.from_pretrained(AR_MODEL_PATH, local_files_only=True)
model_ar = AutoModelForSequenceClassification.from_pretrained(AR_MODEL_PATH, local_files_only=True)

tokenizer_en = AutoTokenizer.from_pretrained(EN_MODEL_PATH, local_files_only=True)
model_en = AutoModelForSequenceClassification.from_pretrained(EN_MODEL_PATH, local_files_only=True)

model_ar.eval()
model_en.eval()

id2label_ar = load_label_map(AR_MODEL_PATH)
id2label_en = load_label_map(EN_MODEL_PATH)


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

    probs = F.softmax(outputs.logits, dim=1)
    confidence, predicted_class = torch.max(probs, dim=1)

    predicted_class = predicted_class.item()
    confidence = float(confidence.item())

    if label_map is not None:
        intent = label_map.get(str(predicted_class), "unknown")
    else:
        intent = "unknown"

    return intent, confidence


def predict_intent(text: str, lang: str = "ar"):
    text = clean_text(text)

    if lang == "ar":
        return predict_with_transformer(text, tokenizer_ar, model_ar, id2label_ar)

    return predict_with_transformer(text, tokenizer_en, model_en, id2label_en)
