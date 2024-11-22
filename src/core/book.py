from dataclasses import dataclass
from uuid import uuid4
from enum import Enum

from .author import Author
from .book_year import BookYear

@dataclass(unsafe_hash=True)
class BookStatus(Enum):
    IN_STOCK = "IN_STOCK"
    ISSUED = "ISSUED"

    @staticmethod
    def loads_json(value: str) -> "BookStatus":
        if value == BookStatus.IN_STOCK.value:
            return BookStatus.IN_STOCK
        elif value == BookStatus.ISSUED.value:
            return BookStatus.ISSUED
        else:
            raise Exception(f"{BookStatus.__name__} Не валидный json")


@dataclass(unsafe_hash=True)
class Book:
    title: str
    author: Author
    year: BookYear
    status: BookStatus = BookStatus.IN_STOCK
    id: str = uuid4().__str__()

    def __post_init__(self):
        self.validate()

    def validate(self):
        if len(self.title) == 0:
            raise ValueError("Имя книги не может быть пустым")

        if not self.id:
            raise ValueError("id книги не может быть пустым")

    def __str__(self):
        in_stock_ru = "В наличии" if self.status is BookStatus.IN_STOCK else "Выдана"
        return (f"Книга: {self.title} | Автор: {self.author} | "
                f"Год издания: {self.year} | {in_stock_ru} | id: {self.id}")

    def __repr__(self):
        return self.__str__()

    def dumps_json(self) -> dict:
        """
        Сериализация book в dict
        :return: возвращает словарь в формате
            {
                "title": "Python для самых маленьких",
                "author": {
                    "surname": "Иванов",
                    "name": "Иван",
                    "patronymic": "Иванович"
                },
                "year": "2024",
                "status": "IN_STOCK",
                "id": "6c9da0fe-ba4b-4236-9fa2-ab628c023353"
            }
        """
        return {
            "title": self.title,
            "author": self.author.__dict__,
            "year": str(self.year),
            "status": self.status.value,
            "id": self.id,
        }

    @staticmethod
    def loads_json(json: dict) -> "Book":
        """
        Десериализует из json возвращает новый экземпляр Book
        :param dict json: ожидается dict формата
            {
                "title": "Python для самых маленьких",
                "author": {
                    "surname": "Иванов",
                    "name": "Иван",
                    "patronymic": "Иванович"
                },
                "year": "2024",
                "status": "IN_STOCK",
                "id": "6c9da0fe-ba4b-4236-9fa2-ab628c023353"
            }
        :return: новый экземпляр Book
        """
        return Book(
            title=json.get("title", ""),
            author=Author.loads_json(json.get("author", {})),
            year=BookYear(json.get("year", "-1")),
            status=BookStatus.loads_json(json.get("status", '')),
            id=json.get("id", ""),
        )
