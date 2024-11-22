from typing import Callable
from dataclasses import dataclass

from src.core import MenuBase


@dataclass(frozen=True)
class ConsoleMenuItem:
    """
    Пункт меню для ConsoleMenu
    description - описание пункта
    funk - вызываемый объект
    args - аргументы для funk
    """
    description: str
    funk: Callable
    args: tuple = tuple()

    def __post_init__(self):
        self.validate()

    def validate(self):
        if not isinstance(self.funk, Callable):
            raise ValueError(f"Атрибут funk должен быть Callable не {type(self.funk)}")

        if not isinstance(self.args, tuple):
            raise ValueError(f"Атрибут args должен быть tuple не {type(self.funk)}")


class ConsoleMenu(MenuBase):
    """
    Консольное меню
    выводит пункты меню в консоль запрашивает ввод у пользователя и вызывает funk у пункта меню
    """
    def __init__(self, menu_items: list[ConsoleMenuItem], title: str | None = None):
        self.menu_items = menu_items
        self.title = title

    def _draw(self) -> None:
        menu = ""
        for index, item in enumerate(self.menu_items):
            menu += f"{index + 1} - {item.description}\n"
        if self.title is not None:
            print(self.title.upper())
        print(menu)

    def _get_user_input(self) -> int:
        start_range = 1
        end_range = len(self.menu_items)
        while True:
            item = input(f"Выберете пункт меню от {start_range} до {end_range}: ")
            if not item.isdigit():
                print("Только числа!")
                continue
            item = int(item)
            if not start_range <= item <= end_range:
                print(f"Нужно выбрать в пределах от {start_range} до {end_range}")
                continue
            return item

    def draw(self) -> None:
        self._draw()
        user_input = self._get_user_input()
        item = self.menu_items[user_input - 1]
        item.funk(*item.args)
