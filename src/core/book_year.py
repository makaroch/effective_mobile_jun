from dataclasses import dataclass
from datetime import date


@dataclass
class BookYear:
    year: int

    def __post_init__(self):
        self.validate()

    def validate(self):
        if not isinstance(self.year, int):
            raise ValueError(f"year может быть только int не {type(self.year)}")
        if self.year > date.today().year:
            raise ValueError(f"year не должен превышать текущий год и должен состоять только из цифр")

    def __str__(self):
        return f"{self.year}"

    def __repr__(self):
        return self.__str__()
