from abc import ABC, abstractmethod

from src.core import Book


class ControllerBase(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def del_book(self):
        pass

    @abstractmethod
    def search_book(self):
        pass

    @abstractmethod
    def get_all_book(self):
        pass

    @abstractmethod
    def update_status_book(self):
        pass
