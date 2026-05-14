def detect_language(text: str) -> str:
    arabic_count = sum(1 for ch in text if '\u0600' <= ch <= '\u06FF')
    english_count = sum(1 for ch in text if ch.isascii() and ch.isalpha())

    if arabic_count >= english_count:
        return "ar"
    return "en"
