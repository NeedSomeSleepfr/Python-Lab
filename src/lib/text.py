import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    # Заменяем невидимые управляющие символы на пробелы
    text = "".join(" " if c.isspace() else c for c in text)
    # Схлопываем повторяющиеся пробелы в один
    parts = text.split()
    normalized_text = " ".join(parts)
    return normalized_text


# Тест-кейсы:

# print(normalize("ПрИвЕт\nМИр\t"))  # "привет мир"
# print(normalize("ёжик, Ёлка"))      # "ежик, елка"
# print(normalize("Hello\r\nWorld"))  # "hello world"
# print(normalize("  двойные   пробелы  "))  # "двойные пробелы"

def tokenize(text: str) -> list[str]:
    # Регулярное выражение для поиска слов с учётом дефиса внутри слова
    pattern = r"\b\w+(?:-\w+)*\b"
    words = re.findall(pattern, text)
    return words


# print(tokenize("привет мир"))  # ["привет", "мир"]
# print(tokenize("hello,world!!!"))  # ["hello", "world"]
# print(tokenize("по-настоящему круто"))  # ["по-настоящему", "круто"]
# print(tokenize("2025 год"))  # ["2025", "год"]
# print(tokenize("emoji 😀 не слово"))  # ["emoji", "не", "слово"]


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq


# print(count_freq(["a","b","a","c","b","a"]))  # {"a":3,"b":2,"c":1}
# print(count_freq(["bb","aa","bb","aa","cc"]))  # {"aa":2,"bb":2,"cc":1}


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:n]

# print(top_n({"a":3,"b":2,"c":1}, n=2))  # [("a",3), ("b",2)]
# print(top_n({'bb': 2, 'aa': 2, 'cc': 1}, n=2))  # [("a",3), ("b",2)]