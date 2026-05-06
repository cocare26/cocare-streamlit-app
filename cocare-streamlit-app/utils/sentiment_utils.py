import re
import torch
from transformers import pipeline

AR_MODEL_PATH = "/content/drive/MyDrive/CoCare/Sentiment_Ara"
EN_MODEL_PATH = "/content/drive/MyDrive/CoCare/Sentiment_Eng"

_ar_sentiment = None
_en_sentiment = None


def normalize_text(text):
    text = str(text).strip().lower()
    text = re.sub(r"[أإآٱ]", "ا", text)
    text = re.sub(r"ى", "ي", text)
    text = re.sub(r"ة", "ه", text)
    text = re.sub(r"(.)\1{2,}", r"\1\1", text)  # يقلل التكرار: خراااا -> خراا
    text = re.sub(r"[^\u0600-\u06FFa-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def load_arabic_sentiment_model():
    global _ar_sentiment
    if _ar_sentiment is None:
        device = 0 if torch.cuda.is_available() else -1
        _ar_sentiment = pipeline(
            "text-classification",
            model=AR_MODEL_PATH,
            tokenizer=AR_MODEL_PATH,
            device=device
        )
    return _ar_sentiment


def load_english_sentiment_model():
    global _en_sentiment
    if _en_sentiment is None:
        device = 0 if torch.cuda.is_available() else -1
        _en_sentiment = pipeline(
            "text-classification",
            model=EN_MODEL_PATH,
            tokenizer=EN_MODEL_PATH,
            device=device
        )
    return _en_sentiment


def rule_based_sentiment(text):
    t = normalize_text(text)

    negative_patterns = [
        r"خرا",
        r"زفت",
        r"يقرف",
        r"قرف",
        r"بتخزي",
        r"بخزي",
        r"سيء",
        r"سيئ",
        r"تعبان",
        r"مقرف",
        r"سي جدا",
        r"مش راضي",
        r"زهقت",
        r"طفشت",
        r"مولعه",
        r"مولعة",
        r"خلصني",
        r"مشكله",
        r"مشكلة",
        r"بطي",
        r"ضعيف",
        r"يفصل",
        r"تقطيع",
        r"مش شغال",
        r"ما بشتغل",
        r"يلعن عرض",
        r"قلعاط",
        r"زبالة ",
        r"ماله",
        r"يقطع",
        r"يلعن",
        r"يحرق",
        r"يخي يلا",
        r"بعدين معك",
        r"بعدين مع امك",
        r"بعدين مع اهلك",
        r"مال سماك",
        r"ماله سماه",
        r"يفضح عرض",
        r"حل عن",

    ]

    positive_patterns = [
        r"ممتاز",
        r"رائع",
        r"تمام",
        r"منيح",
        r"شكرا",
        r"يسلمو",
        r"مشكور",
        r"حلو",
        r"كرامة",
        r"مرتب",
        r"روعة",
        r"هيك عاد",
        r"شكرن",
        r"يؤبرني",
        r"يسلمو",
        r"توب التب",
    ]

    for p in negative_patterns:
        if re.search(p, t):
            return "negative", 0.99

    for p in positive_patterns:
        if re.search(p, t):
            return "positive", 0.90

    return None


def normalize_label(label):
    s = str(label).lower().strip()

    if s in ["negative", "neg", "label_0", "0", "سلبي"]:
        return "negative"

    if s in ["positive", "pos", "label_2", "2", "ايجابي", "إيجابي"]:
        return "positive"

    if s in ["neutral", "neu", "label_1", "1", "محايد"]:
        return "neutral"

    return "neutral"


def predict_sentiment(text, lang="ar"):
    lang = str(lang).lower().strip()

    if lang in ["ar", "arabic", "ara"]:
        forced = rule_based_sentiment(text)
        if forced:
            return forced

        clf = load_arabic_sentiment_model()
        pred = clf(normalize_text(text), truncation=True)[0]
        return normalize_label(pred["label"]), float(pred["score"])

    if lang in ["en", "english"]:
        clf = load_english_sentiment_model()
        pred = clf(str(text), truncation=True)[0]
        return normalize_label(pred["label"]), float(pred["score"])

    return "neutral", 1.0
