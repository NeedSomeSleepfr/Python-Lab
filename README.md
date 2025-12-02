# Python-Lab
## Лаб 1
### Задание 1

```
<<<<<<< HEAD
name=input (" ваше имя:" )
Year= int(input( "ваш возраст: "))
print(f" Привет {name}!,  через год тебе будет {Year+1}")
```
![](/images/lab01/img01.PNG)

### Задание 2

```
n1=float(input())
n2=float(input())
sum=n1+n2
res=n1-n2
print(f"{sum:.1f} {res:.1f}")
```
![](/images/lab01/img02.PNG)

### Задание 3

```
Стоимость=float(input())
Скидка=float(input())
НДС=float(input())
X=Стоимость - (Стоимость*Скидка/100)
Y= X* НДС/100
total=X+Y
print(f"Цена после скидки: ")
print(f"НДС: ")
print(f"Итого к оплате: {total:.2f}")
```
![](/images/lab01/img03.PNG)

### Задание 4

```
Min=int(input())
Hour=Min//60
остаток=Min%60
print(f"{Hour}:{остаток:02d}")
```
![](/images/lab01/img04.PNG)

### Задание 5

```
Name=input("Введите ФИО: ")
inic=Name[0].upper()+"."
for i in range(len(Name)):
    if Name[i] == " " and i +1 < len(Name):
        inic = inic + Name [i + 1]. upper () + "."
lage= len (Name.replace(" ",""))
print (f"ФИО:{Name}")
print (f"Инициалы: {inic}")
print (f" Длина: {lage}")
```
![](/images/lab01/img05.PNG)

## Лаб 2
### Задание 1

```
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Список пуст")

    minimum = min(nums)
    maximum = max(nums)
    return (minimum, maximum)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    unique_nums = set(nums)
    sorted_nums = sorted(unique_nums)
    return sorted_nums


def flatten(mat: list[list | tuple]) -> list:
    result_list = []
    for element in mat:
        if type(element) == list or type(element) == tuple:
            for sub_element in element:
                result_list.append(sub_element)
        elif type(element) == str:
            raise TypeError("строка не строка строк матрицы")

        else:
            result_list.append(element)

    return result_list
```
![](/images/lab02/img01.PNG)
![](/images/lab02/img02.PNG)
![](/images/lab02/img03.PNG)

### Задание 2

```
def transpose(mat):
    if not mat:
        return []

    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("Рваная матрица")

    return [list(row) for row in zip(*mat)]


def row_sums(mat):
    if not mat:
        return []

    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("Рваная матрица: строки разной длины")

    sums = []
    for row in mat:
        row_sum = sum(row)
        sums.append(row_sum)

    return sums


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []

    num_cols = len(mat[0])
    for row in mat:
        if len(row) != num_cols:
            raise ValueError("Рваная матрица")

    sums = [0] * num_cols
    for row in mat:
        for j in range(num_cols):
            sums[j] += row[j]

    return sums
```
![](/images/lab02/img04.PNG)
![](/images/lab02/img05.PNG)
![](/images/lab02/img06.PNG)

### Задание 3

```
def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec

    if not fio.strip():
        raise ValueError("ФИО не может быть пустым")
    if not group.strip():
        raise ValueError("Группа не может быть пустой")
    if not isinstance(gpa, (float, int)):
        raise TypeError("GPA должен быть числом")

    # Убираем лишние пробелы и разбиваем ФИО на части
    parts = fio.strip().split()
    parts = [part.strip() for part in parts if part.strip()]

    # Формируем инициалы
    if len(parts) >= 3:
        initials = (
            f"{parts[0].capitalize()} {parts[1][0].upper()}.{parts[2][0].upper()}."
        )
    elif len(parts) == 2:
        initials = f"{parts[0].capitalize()} {parts[1][0].upper()}."
    else:
        initials = parts[0].capitalize()  # На случай, если ФИО некорректно

    # Форматируем GPA с 2 знаками после запятой
    gpa_formatted = f"{gpa:.2f}"

    return f"{initials}, гр. {group}, GPA {gpa_formatted}"
```
![](/images/lab02/img07.PNG)
![](/images/lab02/img08.PNG)

## Лаб 3
### lib/text

```
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
```
![](/images/lab03/img01.PNG)
![](/images/lab03/img02.PNG)
![](/images/lab03/img03.PNG)
![](/images/lab03/img04.PNG)


### text_stats

```
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
```
![](/images/lab03/img05.PNG)

## Лаб 4
### io_txt_csv

```
import csv
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Открывает файл на чтение в указанной кодировке и возвращает содержимое как одну строку.
    Пользователь может выбрать другую кодировку, передав параметр encoding, например: encoding="cp1251".
    """
    p = Path(path)
    with p.open(mode="r", encoding=encoding) as f:
        content = f.read()
    return content.replace("\n", " ")


# Example usage:
current_directory = Path(__file__).parent.parent
root_directory = current_directory.parent
# ok
# print(read_text(f"{root_directory}\\data\\samples\\text_example.txt", encoding="utf-8"))
# FileNotFoundError
# print(read_text(f"{root_directory}\\data\\samples\\text_not_found.txt", encoding="utf-8"))
# UnicodeDecodeError
# print(read_text(f"{root_directory}\\data\\samples\\text_example.txt", encoding="cp1251"))


def write_csv(
    rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    """
    Создаёт/перезаписывает CSV с разделителем ,.
    Если передан header, записывает его первой строкой.
    Проверяет, что каждая строка в rows имеет одинаковую длину (иначе ValueError).
    """
    p = Path(path)
    if header:
        expected_length = len(header)
    elif rows:
        expected_length = len(rows[0])
    else:
        expected_length = 0
    for row in rows:
        if len(row) != expected_length:
            raise ValueError("Все строки должны иметь одинаковую длину")

    with p.open(mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        if header:
            writer.writerow(header)
        writer.writerows(rows)


# Example usage:
# ok
# write_csv([("word","count"),("test",3)], f"{root_directory}\\data\\out\\check.csv")
# ValueError
# write_csv([("word","count"),("test",3,4)], f"{root_directory}\\data\\out\\check.csv")
# edge case: пустым raws С header=("a","b") → файл содержит только заголовок.
# write_csv([], f"{root_directory}\\data\\out\\check.csv", header=("a","b"))
# с пустым rows и header=None → создаётся пустой файл (0 строк).
write_csv([], f"{root_directory}\\data\\out\\check.csv")
```

### text_report

```
import sys
from pathlib import Path
import argparse
from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv


def main():
    parser = argparse.ArgumentParser(
        description="Generate word frequency report from text file."
    )
    parser.add_argument(
        "--in",
        dest="input_path",
        type=str,
        default="data/input.txt",
        help="Path to input text file",
    )
    parser.add_argument(
        "--out",
        dest="output_path",
        type=str,
        default="data/report.csv",
        help="Path to output CSV file",
    )
    parser.add_argument(
        "--encoding",
        dest="encoding",
        type=str,
        default="utf-8",
        help="File encoding (default: utf-8)",
    )
    args = parser.parse_args()

    input_path = Path(args.input_path)
    output_path = Path(args.output_path)
    encoding = args.encoding

    try:
        # Read input file
        input_text = read_text(input_path, encoding=encoding)

        # Normalize and tokenize text
        normalized_text = normalize(input_text)
        tokens = tokenize(normalized_text)

        # Count word frequencies
        freq = count_freq(tokens)

        # Prepare data for CSV
        rows = [(word, count) for word, count in freq.items()]
        rows.sort(key=lambda x: (-x[1], x[0]))  # Sort by count desc, word asc

        # Write to CSV
        write_csv(rows, output_path, header=("word", "count"))

        # Print summary
        total_words = len(tokens)
        unique_words = len(freq)
        top_5 = top_n(freq, n=5)

        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")
        print("Топ-5:")
        for word, count in top_5:
            print(f"{word}:{count}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found.")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: Cannot decode file '{input_path}' with encoding '{encoding}'.")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
![](/images/lab04/img01.PNG)
![](/images/lab04/img02.PNG)
![](/images/lab04/img03.PNG)
![](/images/lab04/img04.PNG)
![](/images/lab04/img05.PNG)
![](/images/lab04/img06.PNG)
![](/images/lab04/img07.PNG)
![](/images/lab04/img08.PNG)
![](/images/lab04/img09.PNG)
![](/images/lab04/img010.PNG)
![](/images/lab04/img011.PNG)

## Лаб 5
### json_cvs

```

import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    неверный тип файла, пустой JSON или CSV → ValueError.
    осутствующий файл → FileNotFoundError
    """

    # Проверка существования файла
    json_file = Path(json_path)
    if not json_file.is_file():
        raise FileNotFoundError(f"Файл не найден: {json_path}")

    # Проверка типа файла
    if json_file.suffix.lower() != ".json":
        raise ValueError("Неверный тип файла, ожидается JSON файл")

    # Чтение JSON-файла
    with json_file.open(encoding="utf-8") as f:
        data = json.load(f)

    # Проверка на пустой JSON или неверный формат
    if (
        not isinstance(data, list)
        or not data
        or not all(isinstance(item, dict) for item in data)
    ):
        raise ValueError("Неверный формат JSON или пустой JSON")

    # Определение заголовков (ключей)
    headers = set()
    for item in data:
        headers.update(item.keys())
    headers = list(headers)

    # Запись в CSV-файл
    with open(csv_path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for item in data:
            writer.writerow({key: item.get(key, "") for key in headers})


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """

    # Проверка существования файла
    csv_file = Path(csv_path)
    if not csv_file.is_file():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    # Проверка типа файла
    if csv_file.suffix.lower() != ".csv":
        raise ValueError("Неверный тип файла, ожидается CSV файл")

    # Чтение CSV-файла
    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)

    # Проверка на пустой CSV или отсутствие заголовка
    if not data:
        raise ValueError("Пустой CSV файл или отсутствует заголовок")

    # Запись в JSON-файл
    with open(json_path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# Пример использования:
current_directory = Path(__file__).parent.parent
root_directory = current_directory.parent

# Пример использования:
# ok
# json_to_csv(f'{root_directory}\\data\\samples\\people.json', f'{root_directory}\\data\\out\\people_from_json.csv')
# ValueError
# json_to_csv(f'{root_directory}\\data\\samples\\people.csv', f'{root_directory}\\data\\out\\people_from_json.csv')
# FileNotFoundError
# json_to_csv(f'{root_directory}\\data\\samples\\not_existing_file.json', f'{root_directory}\\data\\out\\people_from_json.csv')
# ok
# csv_to_json(f'{root_directory}\\data\\samples\\people.csv',
# f'{root_directory}\\data\\out\\people_from_csv.json')
# ValueError
# csv_to_json(f'{root_directory}\\data\\samples\\people.json',
#             f'{root_directory}\\data\\out\\people_from_csv.json')
# FileNotFoundError
# csv_to_json(f'{root_directory}\\data\\samples\\not_existing_file.csv',
#             f'{root_directory}\\data\\out\\people_from_csv.json')
```
![](/images/lab05/img01.PNG)
![](/images/lab05/img01_1.PNG)
![](/images/lab05/img02.PNG)
![](/images/lab05/img03.PNG)
![](/images/lab05/img04.PNG)
![](/images/lab05/img04_1.PNG)
![](/images/lab05/img05.PNG)

### cvs_xlsx

```
from openpyxl import Workbook
import csv
from pathlib import Path


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """

    # Проверка существования файла
    csv_file = Path(csv_path)
    if not csv_file.is_file():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    # Проверка типа файла
    if csv_file.suffix.lower() != ".csv":
        raise ValueError("Неверный тип файла, ожидается CSV файл")

    # Чтение CSV-файла и запись в XLSX
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            ws.append(row)

    # Автоширина колонок
    for col in ws.columns:
        max_length = 8  # Минимальная ширина
        column = col[0].column_letter  # Получаем букву колонки
        for cell in col:
            try:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            except:
                pass
        adjusted_width = max_length + 2
        ws.column_dimensions[column].width = adjusted_width

    # Сохранение XLSX-файла
    wb.save(xlsx_path)


# Пример использования:
current_directory = Path(__file__).parent.parent
root_directory = current_directory.parent

# ok
# csv_to_xlsx(f'{root_directory}\\data\\samples\\people.csv',
#             f'{root_directory}\\data\\out\\people_from_csv.xlsx')
# ValueError
# csv_to_xlsx(f'{root_directory}\\data\\samples\\people.json',
# f'{root_directory}\\data\\out\\people_from_csv.xlsx')
# FileNotFoundError
# csv_to_xlsx(f"{root_directory}\\data\\samples\\not_existed.csv",
# f"{root_directory}\\data\\out\\people_from_csv.xlsx")
```
![](/images/lab05/img06.PNG)
![](/images/lab05/img07.PNG)
![](/images/lab05/img08.PNG)

## Лаб 6
### cli_convert

```
import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.cvs_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv", description="Конвертация JSON в CSV")
    p1.add_argument("--in", dest="input", required=True, help="Входной JSON файл")
    p1.add_argument("--out", dest="output", required=True, help="Выходной CSV файл")

    p2 = sub.add_parser("csv2json", description="Конвертация CSV в JSON")
    p2.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    p2.add_argument("--out", dest="output", required=True, help="Выходной JSON файл")

    p3 = sub.add_parser("csv2xlsx", description="Конвертация CSV в XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    p3.add_argument("--out", dest="output", required=True, help="Выходной XLSX файл")

    args = parser.parse_args()

    """
        Вызываем код в зависимости от аргументов.
    """
    if args.cmd == "json2csv":
        json_to_csv(args.input, args.output)
    elif args.cmd == "csv2json":
        csv_to_json(args.input, args.output)
    elif args.cmd == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)


if __name__ == "__main__":
    main()
```

### cli_text

```
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
```
![](/images/lab06/img01.PNG)
![](/images/lab06/img02.PNG)
![](/images/lab06/img03.PNG)
![](/images/lab06/img04.PNG)

## Лаб 7
### test_json_csv

```
import json
from pathlib import Path

from src.lab05.json_csv import json_to_csv, csv_to_json

current_directory_path = Path(__file__).parent.parent
root_directory_path = current_directory_path.parent.parent
samples_directory_path = f"{root_directory_path}/data/samples"


def test_json_to_csv_ok(tmp_path):
    people_json_path = f"{samples_directory_path}/people.json"
    output_csv_path = f"{tmp_path}/people.csv"
    json_to_csv(people_json_path, output_csv_path)
    with open(people_json_path) as people_json_file:
        people_json = json.load(people_json_file)  # list of dicts
    with open(output_csv_path) as output_csv_file:
        output_csv_list = output_csv_file.readlines()
    header_line_str = output_csv_list[0].rstrip("\n\r")
    splitted_headers = header_line_str.split(",")
    headers_set = set(splitted_headers)
    json_keys_set = set(people_json[0].keys())
    assert headers_set == json_keys_set
    assert len(output_csv_list) == len(people_json) + 1  # +1 for header


def test_json_to_csv_file_not_found():
    not_existing_json_path = f"{samples_directory_path}/not_existing_file.json"
    output_csv_path = "output.csv"
    try:
        json_to_csv(not_existing_json_path, output_csv_path)
    except FileNotFoundError as e:
        assert str(e) == f"Файл не найден: {not_existing_json_path}"
    else:
        assert False, "Expected FileNotFoundError was not raised"


def test_json_to_csv_input_file_not_json(tmp_path):
    invalid_json_path = f"{samples_directory_path}/people.csv"
    output_csv_path = f"{tmp_path}/output.csv"
    try:
        json_to_csv(invalid_json_path, output_csv_path)
    except ValueError as e:
        assert str(e) == "Неверный тип файла, ожидается JSON файл"
    else:
        assert False, "Expected ValueError was not raised"


def test_csv_to_json_ok(tmp_path):
    people_csv_path = f"{samples_directory_path}/people.csv"
    output_json_path = f"{tmp_path}/people.json"
    csv_to_json(people_csv_path, output_json_path)
    with open(people_csv_path) as people_csv_file:
        people_csv = people_csv_file.readlines()
    with open(output_json_path) as output_json_file:
        output_json = json.load(output_json_file)  # list of dicts
    header_line_str = people_csv[0].rstrip("\n\r")
    splitted_headers = header_line_str.split(",")
    headers_set = set(splitted_headers)
    json_keys_set = set(output_json[0].keys())
    assert headers_set == json_keys_set
    assert len(output_json) == len(people_csv) - 1  # -1 for header


def test_csv_to_json_file_not_found():
    not_existing_csv_path = f"{samples_directory_path}/not_existing_file.csv"
    output_json_path = "output.json"
    try:
        csv_to_json(not_existing_csv_path, output_json_path)
    except FileNotFoundError as e:
        assert str(e) == f"Файл не найден: {not_existing_csv_path}"
    else:
        assert False, "Expected FileNotFoundError was not raised"


# входной файл не csv формата → ожидаем ValueError;
def test_csv_to_json_input_file_not_csv(tmp_path):
    invalid_csv_path = f"{samples_directory_path}/people.json"
    output_json_path = f"{tmp_path}/output.json"
    try:
        csv_to_json(invalid_csv_path, output_json_path)
    except ValueError as e:
        assert str(e) == "Неверный тип файла, ожидается CSV файл"
    else:
        assert False, "Expected ValueError was not raised"
```

### test_text

```
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
```
![](/images/lab07/img01.PNG)
![](/images/lab07/img02.PNG)
![](/images/lab07/img03.PNG)

## Лаб 8
### models

```
import re
from dataclasses import dataclass
from datetime import datetime, date
from typing import ClassVar


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    DATE_FORMAT: ClassVar[str] = "%Y-%m-%d"
    DATE_REGEX: ClassVar[re.Pattern] = re.compile(r"^\d{4}-\d{2}-\d{2}$")

    def __post_init__(self):
        # Validate birthdate format
        if not self.DATE_REGEX.match(self.birthdate):
            raise ValueError(f"Invalid date format for birthdate: {self.birthdate}. Expected YYYY-MM-DD.")
        try:
            datetime.strptime(self.birthdate, self.DATE_FORMAT)
        except ValueError:
            raise ValueError(f"Invalid date value for birthdate: {self.birthdate}.")

        # Validate gpa range
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA must be between 0 and 5. Given: {self.gpa}")

    def age(self) -> int:
        birth_date = datetime.strptime(self.birthdate, self.DATE_FORMAT).date()
        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"],
        )

    def __str__(self) -> str:
        return f"{self.fio}, gr. {self.group}, GPA {self.gpa:.1f}"
```

### serialize

```
import json
from pathlib import Path
from typing import List
from src.lab08.models import Student


def students_to_json(students: List[Student], path: str) -> None:
    data = [s.to_dict() for s in students]
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path: str) -> List[Student]:
    with open(path, mode="r", encoding="utf-8") as f:
        data = json.load(f)
    students = [Student.from_dict(item) for item in data]
    return students

# Пример использования:
current_directory = Path(__file__).parent.parent
root_directory = current_directory.parent

students = [
    Student(fio="Иванов Иван Иванович", birthdate="2000-12-15", group="SE-01", gpa=4.5),
    Student(fio="Петров Петр Петрович", birthdate="1999-05-20", group="SE-02", gpa=3.8),
]
students_to_json(students, f"{root_directory}\\data\\lab08\\students_output.json")

loaded_students = students_from_json(f"{root_directory}\\data\\lab08\\students_input.json")
for student in loaded_students:
    print(student)
```
![](/images/lab08/img01.PNG)
![](/images/lab08/img02.PNG)
![](/images/lab08/img03.PNG)
=======
Name= input("ваше имя:" )
Year= int(input("ваш возраст:"))
print(f"Привет {Name}!, через год тебе будет {Year+1}")
```
<![alt text](01.1.png)>

### Задание 2

```
n1=float(input("Номер 1 ="))
n2=float(input("Номер 2 ="))
sum=n1+n2
res=n1-n2
print(f"Cложение={sum:.1f}, вычитание={res:.1f}")
```

### Задание 3

```
Цена=float(input("Цена продукта:"))
Скидка=float(input("Скидка:"))
НДС=float(input("НДС:"))
X= Цена - (Цена*Скидка/100)
Y= X* НДС/100
total=X+Y
print(f"Цена после скидки: {X}")
print(f"НДС: {Y}")
print(f"Итого к оплате: {total:.2f}")
```

### Задание 4

```
Минуты=int(input("Минуты: "))
Часы=Min//60
остаток=Min%60
print(f"{Часы}:{остаток:02d}")
```

### Задание 5

```
Name=input("Введите ФИО: ")
inic=Name[0].upper()+"."
for i in range(len(Name)):
    if Name[i] == " " and i +1 < len(Name):
        inic = inic + Name [i + 1]. upper () + "."
lage= len (Name.replace(" ",""))
print (f"ФИО:{Name}")
print (f"Инициалы: {inic}")
print (f"Длина: {lage}")
```
>>>>>>> a4cae7d5639e2a27fbf34d0d92eb8218d24fdfd2
