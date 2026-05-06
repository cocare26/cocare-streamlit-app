import re
import torch
from transformers import pipeline

AR_MODEL_PATH = "/content/drive/MyDrive/CoCare/Intent_Ara/xlmr_intent_model_13_balanced"
EN_MODEL_PATH = "/content/drive/MyDrive/CoCare/intent_Eng/distilbert_intent_model_only"

_ar_clf = None
_en_clf = None


def normalize_text(text):
    text = str(text).strip().lower()
    text = re.sub(r"[أإآٱ]", "ا", text)
    text = re.sub(r"ى", "ي", text)
    text = re.sub(r"ة", "ه", text)
    text = re.sub(r"[^\u0600-\u06FFa-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def load_arabic_model():
    global _ar_clf
    if _ar_clf is None:
        device = 0 if torch.cuda.is_available() else -1
        _ar_clf = pipeline(
            "text-classification",
            model=AR_MODEL_PATH,
            tokenizer=AR_MODEL_PATH,
            device=device
        )
    return _ar_clf


def load_english_model():
    global _en_clf
    if _en_clf is None:
        device = 0 if torch.cuda.is_available() else -1
        _en_clf = pipeline(
            "text-classification",
            model=EN_MODEL_PATH,
            tokenizer=EN_MODEL_PATH,
            device=device
        )
    return _en_clf


def rule_based_override(text):
    t = normalize_text(text)

    if t in ["هاي", "هلا", "مرحبا", "اهلا", "اهلين", "السلام عليكم", "كيفك", "hi", "hello", "hey"]:
        return "greeting"

    if t in ["باي", "مع السلامه", "مع السلامة", "سلام", "bye", "goodbye"]:
        return "goodbye"

    if t in ["شكرا", "شكرن", "يسلمو", "مشكور", "يعطيك العافيه", "thanks", "thank you"]:
        return "feedback"

    if re.search(r"(النت|الانترنت|الشبكه|الشبكة|التصفح).*(بطي|سيء|زفت|بخزي|بعلق|تقطيع|ضعيف)", t):
        return "slow_internet"

    if re.search(r"(ما في|مافي|معدوم|خارج الخدمه|خارج الخدمة).*(شبكه|شبكة|اشاره|اشارة|تغطيه|تغطية)", t):
        return "no_signal"

    if re.search(r"(حاله|حالة|وضع|افحص|تحقق).*(الشبكه|الشبكة|النت|الخدمه|الخدمة)", t):
        return "network_status"

    if re.search(r"(دفع|دفعت|فاتوره|فاتورة|رصيد|شحن|شحنت|خصم|انخصم)", t):
        return "payment_issue"

    if re.search(r"(دعم|تقني|فني|مساعده|مساعدة|اصلح|حل)", t):
        return "technical_support"

    return None


def predict_intent(text, lang="ar"):
    lang = str(lang).lower().strip()

    if lang in ["ar", "arabic", "ara"]:
        forced = rule_based_override(text)
        if forced:
            return forced, 0.99

        clf = load_arabic_model()
        pred = clf(normalize_text(text), truncation=True)[0]
        return str(pred["label"]).strip().lower(), float(pred["score"])

    if lang in ["en", "english"]:
        clf = load_english_model()
        pred = clf(str(text), truncation=True)[0]
        return str(pred["label"]).strip().lower(), float(pred["score"])

    return "unknown", 1.0
