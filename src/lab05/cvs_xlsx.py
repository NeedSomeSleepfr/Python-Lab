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