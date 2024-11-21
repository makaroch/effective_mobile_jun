from src.core import ViewBase, Book, Author, BookYear
from .console_menu import ConsoleMenu, ConsoleMenuItem


class ConsoleView(ViewBase):
    def show_main_menu(self, controller: "ConsoleController"):
        main_menu = ConsoleMenu(
            [
                ConsoleMenuItem("Добавление книги", self.get_info_fo_add_book, args=(controller,)),
                ConsoleMenuItem("Удаление книги", self.get_info_fo_del_book, args=(controller,)),
                ConsoleMenuItem("Поиск книги", self.get_info_fo_search_book, args=(controller,)),
                ConsoleMenuItem("Отображение всех книг", self.show_all_book, args=(controller,)),
                ConsoleMenuItem("Изменение статуса книги", self.get_info_fo_update_status_book, args=(controller,)),
                ConsoleMenuItem("Выйти", lambda: print("\nВсего ХО-РО-ШЕГО!")),
            ],
            title="\nГлавное меню"
        )
        main_menu.draw()

    def save_book(self, title: str, author: Author, year: BookYear, controller: "ConsoleController"):
        book = Book(title.strip().title(), author, year)
        controller.add_book(book)

    def get_info_fo_add_book(self, controller: "ConsoleController"):
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

    def get_info_fo_del_book(self, controller: "ConsoleController"):
        book_id = input("Введите id книги для удаления: ")
        controller.del_book(book_id)
        self.show_main_menu(controller)

    def get_info_fo_search_book(self):
        pass

    def show_all_book(self, controller: "ConsoleController"):
        books = controller.get_all_book()
        for book in books:
            self.show_data(book)
        self.show_main_menu(controller)

    def show_data(self, text: str, status: int = 200):
        print(text)

    def get_info_fo_update_status_book(self):
        pass

    def __get_author_data(self) -> Author:
        surname = input("Введите Фамилию автора: ").title()
        name = input("Введите Имя автора: ").title()
        patronymic = input("Введите Отчество автора: ").title()
        return Author(surname, name, patronymic)
