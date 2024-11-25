import unittest
from unittest import TestCase
from unittest.mock import MagicMock
from src.views.console_menu import ConsoleMenu, ConsoleMenuItem

class TestConsoleMenu(TestCase):

    def setUp(self):
        self.mock_function = MagicMock()
        self.menu_items = [
            ConsoleMenuItem(description="Item 1", funk=self.mock_function, args=(1,)),
            ConsoleMenuItem(description="Item 2", funk=self.mock_function, args=(2,))
        ]
        self.menu = ConsoleMenu(menu_items=self.menu_items, title="Test Menu")

    def test_draw(self):
        with unittest.mock.patch('builtins.input', return_value='1'):
            self.menu.draw()
            self.mock_function.assert_called_once_with(1)

    def test_get_user_input_invalid(self):
        with unittest.mock.patch('builtins.input', side_effect=['invalid', '3', '1']):
            self.menu.draw()
            self.mock_function.assert_called_once_with(1)

    def test_get_user_input_valid(self):
        with unittest.mock.patch('builtins.input', return_value='2'):
            self.menu.draw()
            self.mock_function.assert_called_once_with(2)