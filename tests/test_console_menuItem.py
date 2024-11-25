import unittest
from unittest.mock import MagicMock
from src.views.console_menu import ConsoleMenuItem


class TestConsoleMenuItem(unittest.TestCase):

    def test_validate(self):
        with self.assertRaises(ValueError):
            ConsoleMenuItem(description="item", funk="not callable")

        with self.assertRaises(ValueError):
            ConsoleMenuItem(description="item", funk=lambda x: x, args="not tuple")

    def test_validate_success(self):
        ConsoleMenuItem(description="item", funk=lambda x: x, args=("tuple",))
