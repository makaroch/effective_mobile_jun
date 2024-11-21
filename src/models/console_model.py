from src.core import ModelBase, Book, Author, BookYear


class ConsoleModel(ModelBase):
    def add_book(self, book: Book) -> dict[str: str]:
        print(book)

    def del_book(self, book_id: str) -> dict[str: str]:
        pass

    def search_book(self, title: str | None = None, author: Author | None = None, year: BookYear | None = None):
        if title is None and author is None and year is None:
            raise ValueError("Все поля поиска пусты")

    def get_all_book(self) -> list[dict[str: str]]:
        pass

    def update_status_book(self, book_id: str) -> dict[str: str]:
        pass
