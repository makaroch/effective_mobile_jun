from src.core import ViewBase, Book, Author, BookYear, ControllerBase
from .console_menu import ConsoleMenu, ConsoleMenuItem


class ConsoleView(ViewBase):
    def show_main_menu(self, controller: ControllerBase):
        main_menu = ConsoleMenu(
            [
                ConsoleMenuItem("Добавление книги", self.get_info_fo_add_book, args=(controller,)),
                ConsoleMenuItem("Удаление книги", self.get_info_fo_del_book, args=(controller,)),
                ConsoleMenuItem("Поиск книги", self.get_info_fo_search_book, args=(controller,)),
                ConsoleMenuItem("Отображение всех книг", self.show_all_book, args=(controller,)),
                ConsoleMenuItem("Изменение статуса книги", self.get_info_fo_update_status_book, args=(controller,)),
            ],
            title="Главное меню"
        )
        main_menu.draw()

    def save_book(self, title: str, author: Author, year: BookYear, controller: ControllerBase):
        book = Book(title, author, year)
        controller.add_book(book)

    def get_info_fo_add_book(self, controller: ControllerBase):
        try:
            title = input("Введите название книги: ")
            author = self.__get_author_data()
            year = BookYear(input("Введите год издания книги: "))
            self.show_data(
                text=f"Вы ввели следующие данные: "
                     f"Название книги: {title}, Автор {author}, Год издания книги: {year}"
            )
            menu = ConsoleMenu(
                menu_items=[
                    ConsoleMenuItem("Все ок, сохранить!", self.save_book,
                                    args=(title, author, year, controller)),
                    ConsoleMenuItem("Ввести заново!", self.get_info_fo_add_book, args=(controller,)),
                    ConsoleMenuItem("Отмена добавления...", lambda: None),
                ]
            )
            menu.draw()
        except ValueError as e:
            self.show_data((e.__str__()))
        finally:
            self.show_main_menu(controller)

    def get_info_fo_del_book(self):
        pass

    def get_info_fo_search_book(self):
        pass

    def show_all_book(self):
        pass

    def show_data(self, text: str):
        print(text)

    def get_info_fo_update_status_book(self):
        pass

    def __get_author_data(self) -> Author:
        surname = input("Введите Фамилию автора: ").title()
        name = input("Введите Имя автора: ").title()
        patronymic = input("Введите Отчество автора: ").title()
        return Author(surname, name, patronymic)
