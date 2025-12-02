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