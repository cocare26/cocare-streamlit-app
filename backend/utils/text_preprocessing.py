import re


def normalize_arabic(text: str) -> str:
    text = re.sub(r"[إأآا]", "ا", text)
    text = re.sub(r"ى", "ي", text)
    text = re.sub(r"ة", "ه", text)
    text = re.sub(r"ؤ", "و", text)
    text = re.sub(r"ئ", "ي", text)
    text = re.sub(r"ـ", "", text)

    # إزالة التكرار المبالغ فيه للحروف
    text = re.sub(r"(.)\1{2,}", r"\1", text)

    return text


ARABIC_SLANG_MAP = {
    "بخزي": "سيء",
    "بعلق": "بطيء",
    "بقطع": "منقطع",
    "معلق": "بطيء",
    "خربان": "مشكله",
}


def normalize_slang(text: str) -> str:
    for slang, formal in ARABIC_SLANG_MAP.items():
        text = text.replace(slang, formal)
    return text


def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""

    text = text.strip()
    text = normalize_arabic(text)
    text = normalize_slang(text)
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"(.)\1+", r"\1", text)
    
    return text.lower().strip()