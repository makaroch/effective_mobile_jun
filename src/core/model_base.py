from abc import ABC, abstractmethod

from src.core import Author, BookYear, Book


class ModelBase(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> "Response":
        pass

    @abstractmethod
    def del_book(self, book_id: str) -> "Response":
        pass

    @abstractmethod
    def search_book(self, title: str | None = None, author: Author | None = None, year: BookYear | None = None):
        if title is None and author is None and year is None:
            raise ValueError("Все поля поиска пусты")

    @abstractmethod
    def get_all_book(self) -> list[Book]:
        pass

    @abstractmethod
    def update_status_book(self, book_id: str, status: str) -> "Response":
        pass
