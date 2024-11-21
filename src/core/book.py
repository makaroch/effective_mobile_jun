from dataclasses import dataclass
from uuid import uuid4
from enum import Enum

from .author import Author
from .book_year import BookYear


class BookStatus(Enum):
    IN_STOCK = "IN_STOCK"
    ISSUED = "ISSUED"


@dataclass
class Book:
    title: str
    author: Author
    year: BookYear
    status: BookStatus = BookStatus.IN_STOCK
    id: uuid4 = uuid4()

    def __post_init__(self):
        self.validate()

    def validate(self):
        if len(self.title) == 0:
            raise ValueError("Имя книги не может быть пустым")

    def __str__(self):
        in_stock_ru = "да" if self.status is BookStatus.IN_STOCK else "нет"
        return (f"Книга: {self.title}, Автор: {self.author}, "
                f"Год издания: {self.year}, В наличии: {in_stock_ru}, id: {self.id}")

    def __repr__(self):
        return self.__str__()

    def dumps_json(self) -> dict:
        return {
            "title": self.title,
            "author": self.author.__dict__,
            "year": str(self.year),
            "status": self.status.value,
            "id": self.id.__str__(),
        }
