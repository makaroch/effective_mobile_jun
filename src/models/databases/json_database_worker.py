import os
import json

from src.core import Book, Author, BookYear, Response, BookStatus
from src.core.database_worker_base import DatabaseWorkerBase


class JsonDatabaseWorker(DatabaseWorkerBase):

    def __init__(self, path_to_db: str = "json_database.json"):
        self.path_to_db = path_to_db
        self.__create_db_if_not_exists()

    def __create_db_if_not_exists(self):
        if not os.path.isfile(self.path_to_db):
            with open(self.path_to_db, "w", encoding="utf-8") as f:
                json.dump([], f)

    def add_book(self, book: Book):
        books = self.__read_jsondb()
        books.append(book)
        self.__save_jsondb(books)

    def del_book(self, book_id: str) -> Response:
        books = self.__read_jsondb()
        for index, book in enumerate(books):
            if book.id == book_id:
                books.pop(index)
                self.__save_jsondb(books)
                return Response(message=f"{book}\nКнига удалена!")
        return Response(message="Книга с таким id не найдена", status=404)

    def search_book(self, title: str | None = None, author: Author | None = None, year: BookYear | None = None):
        pass

    def get_all_book(self) -> list[Book]:
        return self.__read_jsondb()

    def update_status_book(self, book_id: str, status: BookStatus) -> Response:
        books = self.__read_jsondb()
        for book in books:
            if book.id == book_id:
                book.status = status
                self.__save_jsondb(books)
                return Response(f"{book}\nУспешно изменено!")
        return Response(message="Книга с таким id не найдена", status=404)

    def __read_jsondb(self) -> list[Book]:
        with open(self.path_to_db, "r", encoding="utf-8") as f:
            data = json.load(f)

        return [Book.loads_json(book) for book in data]

    def __save_jsondb(self, books: list[Book]):
        save_data = [book.dumps_json() for book in books]
        with open(self.path_to_db, "w", encoding="utf-8") as f:
            return json.dump(save_data, f, indent=4)
