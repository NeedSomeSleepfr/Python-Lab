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