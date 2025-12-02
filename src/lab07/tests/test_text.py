import pytest

from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "not_normalized_text, expected_normalized_text",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("#", "#"),
    ],
)
def test_normalize_ok(not_normalized_text, expected_normalized_text):
    assert normalize(not_normalized_text) == expected_normalized_text


@pytest.mark.parametrize(
    "actual_text, expected_tokens",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("", []),
    ],
)
def test_tokenize_ok(actual_text, expected_tokens):
    assert tokenize(actual_text) == expected_tokens


@pytest.mark.parametrize(
    "tokens, expected_freq",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        (["bb", "aa", "bb", "aa", "cc"], {"aa": 2, "bb": 2, "cc": 1}),
        ([], {}),
    ],
)
def test_count_freq_ok(tokens, expected_freq):
    assert count_freq(tokens) == expected_freq


@pytest.mark.parametrize(
    "freq, n, expected_top_n",
    [
        ({"a": 3, "b": 2, "c": 1}, 2, [("a", 3), ("b", 2)]),
        ({"bb": 2, "aa": 2, "cc": 1}, 2, [("aa", 2), ("bb", 2)]),
        ({"aa": 2, "bb": 2, "cc": 1}, 2, [("aa", 2), ("bb", 2)]),
    ],
)
def test_top_n_ok(freq, n, expected_top_n):
    assert top_n(freq, n) == expected_top_n