from dataclasses import dataclass
from datetime import date


@dataclass(unsafe_hash=True)
class BookYear:
    """
    Год издания книги
    """
    year: str

    def __post_init__(self):
        self.validate()

    def validate(self):
        if not isinstance(self.year, str):
            raise ValueError(f"year может быть только str не {type(self.year)}")
        if not self.year.isdigit() or int(self.year) > date.today().year:
            raise ValueError(f"year не должен превышать текущий год и должен состоять только из цифр")

    def __str__(self):
        return f"{self.year}"

    def __repr__(self):
        return self.__str__()

