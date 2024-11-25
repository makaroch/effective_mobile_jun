from unittest import TestCase

from src.core import Author


class TestAuthor(TestCase):
    def test_create_author(self):
        author = Author('Пупкин', 'Вася', 'Петрович')
        self.assertEqual(author.surname, 'Пупкин')
        self.assertEqual(author.name, 'Вася')
        self.assertEqual(author.patronymic, 'Петрович')

    def test_validate_author(self):
        with self.assertRaises(ValueError):
            author = Author('Пупкин', 'Вася', '')

    def test_str_author(self):
        author = Author('Пупкин', 'Вася', 'Петрович')
        self.assertEqual(str(author), 'Пупкин В.П.')

    def test_loads_json_author(self):
        json_author = {
            'surname': 'Пупкин',
            'name': 'Вася',
            'patronymic': 'Петрович'
        }
        author = Author.loads_json(json_author)
        self.assertEqual(author.surname, 'Пупкин')
        self.assertEqual(author.name, 'Вася')
        self.assertEqual(author.patronymic, 'Петрович')

    def test_loads_json_author_empty(self):
        json_author = {
            'surname': '',
            'name': '',
            'patronymic': ''
        }
        with self.assertRaises(ValueError):
            author = Author.loads_json(json_author)
