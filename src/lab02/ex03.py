def format_record(rec: tuple[str, str, float]) -> str:
    """
    Форматирует запись студента в строку.

    Аргументы:
    rec -- кортеж (fio: str, group: str, gpa: float)

    Возвращает:
    str -- форматированная строка вида "Фамилия И.И., гр. Группа, GPA X.XX"

    Исключения:
    ValueError -- если ФИО или группа пусты
    TypeError -- если GPA не является числом
    """
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


# Тест-кейсы (минимум)

print(
    format_record(("Иванов Иван Иванович", "BIVT-25", 4.6))
)  # "Иванов И.И., гр. BIVT-25, GPA 4.60"
print(
    format_record(("Петров Пётр", "IKBO-12", 5.0))
)  # "Петров П., гр. IKBO-12, GPA 5.00"
print(
    format_record(("Петров Пётр Петрович", "IKBO-12", 5.0))
)  # "Петров П.П., гр. IKBO-12, GPA 5.00"
print(
    format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))
)  # "Сидорова А.С., гр. ABB-01, GPA 4.00"
print(format_record(("", "ABB-01", 3.5)))  # ValueError
print(format_record(("Иванов Иван", "", 4.0)))  # ValueError
print(format_record(("Иванов Иван", "BIVT-25", "четыре")))  # TypeError