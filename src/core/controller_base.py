from abc import ABC, abstractmethod


class ControllerBase(ABC):
    @abstractmethod
    def add_book(self):
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
