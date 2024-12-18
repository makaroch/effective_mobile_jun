from datetime import date
from unittest import TestCase

from unittest import TestCase
from src.core.book_year import BookYear


class TestBookYear(TestCase):
    def test_year_initialization(self):
        year = BookYear("2023")
        self.assertEqual(year.year, "2023")

    def test_year_validation_invalid_format(self):
        with self.assertRaises(ValueError):
            BookYear("invalid")

    def test_year_validation_future_year(self):
        future_year = str(date.today().year + 1)
        with self.assertRaises(ValueError):
            BookYear(future_year)

    def test_str_representation(self):
        year = BookYear("2023")
        self.assertEqual(str(year), "2023")
