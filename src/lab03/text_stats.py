from src.lib.text import normalize, tokenize, count_freq, top_n


def main():
    # Чтение всего ввода до EOF
    input_text = input()
    # print("input_text: ", input_text)

    # Нормализация текста
    normalized_text = normalize(input_text)

    # Токенизация текста
    tokens = tokenize(normalized_text)

    # Подсчёт частот слов
    freq = count_freq(tokens)

    # Вычисление общего количества слов и уникальных слов
    total_words = len(tokens)
    unique_words = len(freq)

    # Получение топ-5 слов по частоте
    top_5 = top_n(freq, n=5)

    # Вывод результатов

    TABLE_OUTPUT = False

    if not TABLE_OUTPUT:
        # Вывод результата в простом формате
        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")
        print("Топ-5:")
        for word, count in top_5:
            print(f"{word}:{count}")
    else:
        # Вывод результата в табличном режиме

        # Формат:
        #
        # слово        | частота
        # ----------------------
        # привет       | 10
        # мир          | 7

        # Ширина столбца «слово» — по максимальной длине слова из топа.

        if top_5:
            max_word_length = max(len(word) for word, count in top_5)
            print("\nТабличный формат:")
            print(f"{'слово'.ljust(max_word_length)} | частота")
            print("-" * (max_word_length + 10))
            for word, count in top_5:
                print(f"{word.ljust(max_word_length)} | {count}")


if __name__ == "__main__":
    main()