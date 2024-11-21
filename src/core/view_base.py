from abc import ABC, abstractmethod

from src.core import Book


class ViewBase(ABC):
    @abstractmethod
    def get_info_fo_add_book(self) -> Book:
        pass

    @abstractmethod
    def get_info_fo_del_book(self):
        pass

    @abstractmethod
    def get_info_fo_search_book(self):
        pass

    @abstractmethod
    def show_all_book(self):
        pass

    @abstractmethod
    def show_data(self, text: str):
        pass

    @abstractmethod
    def get_info_fo_update_status_book(self):
        pass
