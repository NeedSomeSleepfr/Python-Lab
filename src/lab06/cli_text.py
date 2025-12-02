import argparse


def main():
    parser = argparse.ArgumentParser(description="CLI‑утилита лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", description="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", description="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    stats_parser.add_argument(
        "--top", type=int, help="Количество топ‑слов для вывода (по умолчанию 5)"
    )

    args = parser.parse_args()

    if args.command == "cat":
        # cat --input <path> [-n] — вывод содержимого файла построчно (с нумерацией при -n).
        """Реализация команды cat"""
        with open(args.input, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, start=1):
                if args.n:
                    print(f"{i}\t{line.rstrip()}")
                else:
                    print(line.rstrip())
    elif args.command == "stats":
        # stats --input <txt> [--top 5] — анализ частот слов в тексте (использовать функции из src.lib.text).;
        """Реализация команды stats"""
        from src.lib.text import normalize, tokenize, count_freq, top_n

        with open(args.input, "r", encoding="utf-8") as f:
            text = f.read()
        normalized_text = normalize(text)
        tokens = tokenize(normalized_text)
        frequencies = count_freq(tokens)

        if args.top:
            top_words = top_n(frequencies, n=args.top)
            for word, count in top_words:
                print(f"{word}:{count}")
        else:
            print(frequencies)


if __name__ == "__main__":
    main()


# python src/lab06/cli_text.py cat --input data/samples/people.csv
# python src/lab06/cli_text.py cat --input data/samples/people.csv -n
# 1       name,age,city
# 2       Alice,22,SPB
# 3       Bob,25,Moscow
# 4       Carlos,30,Kazan
# 5       Dana,21,SPB
# 6       Andrey,27,Novosibirsk
# python src/lab06/cli_text.py cat --input data/samples/people.csv
# name,age,city
# Alice,22,SPB
# Bob,25,Moscow
# Carlos,30,Kazan
# Dana,21,SPB
# Andrey,27,Novosibirsk