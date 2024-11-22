from src.core import Book, ControllerBase, BookStatus, Author, BookYear
from src.models.console_model import ConsoleModel
from src.views.console_view import ConsoleView


class ConsoleController(ControllerBase):
    def __init__(self, view: ConsoleView, model: ConsoleModel):
        self.view = view
        self.model = model

    def add_book(self, book: Book):
        return self.model.add_book(book)

    def del_book(self, book_id):
        return self.model.del_book(book_id)

    def search_book(self, title: str | None = None, author: Author | None = None,
                    year: BookYear | None = None) -> list[Book]:
        return self.model.search_book(title, author, year)

    def get_all_book(self):
        return self.model.get_all_book()

    def update_status_book(self, book_id: str, status: BookStatus):
        return self.model.update_status_book(book_id, status)

    def show_main_menu(self):
        self.view.show_main_menu(self)
