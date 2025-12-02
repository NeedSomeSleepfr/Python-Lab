
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
