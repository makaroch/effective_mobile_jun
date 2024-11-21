from abc import ABC, abstractmethod

from src.core import Book, Author, BookYear


class DatabaseWorkerBase(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> dict[str: str]:
        pass

    @abstractmethod
    def del_book(self, book_id: str) -> dict[str: str]:
        pass

    @abstractmethod
    def search_book(self, title: str | None = None, author: Author | None = None, year: BookYear | None = None):
        pass

    @abstractmethod
    def get_all_book(self) -> list[dict[str: str]]:
        pass

    @abstractmethod
    def update_status_book(self, book_id: str) -> dict[str: str]:
        pass
