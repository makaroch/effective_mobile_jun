from src.core import Book, ControllerBase, Response
from src.models.console_model import ConsoleModel
from src.views.console_view import ConsoleView


class ConsoleController(ControllerBase):
    def __init__(self, view: ConsoleView, model: ConsoleModel):
        self.view = view
        self.model = model

    def get_info_add_bok(self):
        self.view.get_info_fo_add_book(self)

    def add_book(self, book: Book):
        response = self.model.add_book(book)
        self.view.show_data(response.message, response.status)

    def del_book(self, book_id):
        response = self.model.del_book(book_id)
        self.view.show_data(response.message, response.status)

    def search_book(self):
        pass

    def get_all_book(self):
        return self.model.get_all_book()

    def update_status_book(self):
        pass

    def show_main_menu(self):
        self.view.show_main_menu(self)
