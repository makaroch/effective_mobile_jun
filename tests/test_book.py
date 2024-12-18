from unittest import TestCase

from src.core import Book, Author, BookYear, BookStatus


class TestBook(TestCase):

    def test_validate_title(self):
        with self.assertRaises(ValueError):
            Book("", author=Author("Иванов", "Иван", "Иванович"), year=BookYear("2024"))

    def test_validate_id(self):
        with self.assertRaises(ValueError):
            Book("Python для самых маленьких", author=Author("Иванов", "Иван", "Иванович"), year=BookYear("2024"), id="")

    def test_dumps_json(self):
        book = Book("Python для самых маленьких", author=Author("Иванов", "Иван", "Иванович"), year=BookYear("2024"))
        expected = {
            "title": "Python для самых маленьких",
            "author": {
                "surname": "Иванов",
                "name": "Иван",
                "patronymic": "Иванович"
            },
            "year": "2024",
            "status": "IN_STOCK",
            "id": book.id
        }
        self.assertDictEqual(book.dumps_json(), expected)

    def test_loads_json(self):
        book = Book.loads_json(
            {
                "title": "Python для самых маленьких",
                "author": {
                    "surname": "Иванов",
                    "name": "Иван",
                    "patronymic": "Иванович"
                },
                "year": "2024",
                "status": "IN_STOCK",
                "id": "123"
            }
        )
        self.assertEqual(book.title, "Python для самых маленьких")
        self.assertEqual(book.author.surname, "Иванов")
        self.assertEqual(book.year.year, "2024")
        self.assertEqual(book.status, BookStatus.IN_STOCK)
        self.assertEqual(book.id, "123")
