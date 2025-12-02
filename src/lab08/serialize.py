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