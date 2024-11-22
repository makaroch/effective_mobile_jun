from src.core import ModelBase, Book, Author, BookYear, Response, BookStatus
from .databases.db import DB


class ConsoleModel(ModelBase):
    def add_book(self, book: Book) -> Response:
        DB.add_book(book)
        return Response("Книга добавлена!", status=201)

    def del_book(self, book_id: str) -> Response:
        return DB.del_book(book_id)

    def search_book(self, title: str | None = None, author: Author | None = None,
                    year: BookYear | None = None) -> list[Book]:
        super().search_book(title, author, year)
        return DB.search_book(title, author, year)

    def get_all_book(self) -> list[Book]:
        return DB.get_all_book()

    def update_status_book(self, book_id: str, status: BookStatus) -> Response:
        return DB.update_status_book(book_id, status)
