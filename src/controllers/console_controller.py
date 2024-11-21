from calendar import month

from src.core import Book, ControllerBase
from src.models.console_model import ConsoleModel
from src.views.console_view import ConsoleView


class ConsoleController(ControllerBase):
    def __init__(self, view: ConsoleView, model: ConsoleModel):
        self.view = view
        self.model = model

    def get_info_add_bok(self):
        self.view.get_info_fo_add_book(self)

    def add_book(self, book: Book):
        self.model.add_book(book)

    def del_book(self):
        pass

    def search_book(self):
        pass

    def get_all_book(self):
        pass

    def update_status_book(self):
        pass

    def show_main_menu(self):
        self.view.show_main_menu(self)