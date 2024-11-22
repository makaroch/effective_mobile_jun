from src.core import ViewBase, Book, Author, BookYear, BookStatus
from .menu_factory import m_factory


class ConsoleView(ViewBase):
    def show_main_menu(self, controller: "ConsoleController"):
        m_factory(
            ("Добавление книги", self.get_info_fo_add_book, (controller,)),
            ("Удаление книги", self.get_info_fo_del_book, (controller,)),
            ("Поиск книги", self.get_info_fo_search_book, (controller,)),
            ("Отображение всех книг", self.show_all_book, (controller,)),
            ("Изменение статуса книги", self.get_info_fo_update_status_book, (controller,)),
            ("Выйти", lambda: exit("\nВсего ХО-РО-ШЕ-ГО!")),
            title="\nГлавное меню"
        ).draw()

    def save_book(self, title: str, author: Author, year: BookYear, controller: "ConsoleController"):
        book = Book(title.strip().title(), author, year)
        response = controller.add_book(book)
        self.show_info(response.message, response.status)

    def get_info_fo_add_book(self, controller: "ConsoleController"):
        try:
            title = input("Введите название книги: ").title()
            author = self.__get_info_and_create_author()
            year = self.__get_info_and_create_year()
            self.show_info(
                text=f"Вы ввели следующие данные: "
                     f"Название книги: {title}, Автор {author}, Год издания книги: {year}"
            )
            m_factory(
                ("Все ок, сохранить!", self.save_book, (title, author, year, controller)),
                ("Ввести заново!", self.get_info_fo_add_book, (controller,)),
                ("Отмена добавления...", lambda: None),
                title="Подменю добавления книги"
            ).draw()
        except ValueError as e:
            self.show_info(e.__str__(), status=400)

    def get_info_fo_del_book(self, controller: "ConsoleController"):
        book_id = input("Введите id книги для удаления: ")
        response = controller.del_book(book_id)
        self.show_info(response.message, response.status)

    def search_book(self, title: str | None, author: Author | None,
                    year: BookYear | None, controller: "ControllerBase"):
        response = controller.search_book(title, author, year)
        if response:
            self.show_info(response)
        else:
            self.show_info("Не найдено ни одной книги", status=400)

    def get_info_fo_search_book(self, controller: "ControllerBase"):
        try:
            print("Если вы не хотите искать по одному из пунктов нажмите enter ничего не вводя")
            title = input("Введите название книги: ").title()
            author = self.__get_author_data()
            year = self.__get_year_data()
            if not title:
                title = None

            if not author[0]:
                author = None
            else:
                author = self.__create_author(*author)
            if not year:
                year = None
            else:
                year = self.__create_year(year)
            self.search_book(title, author, year, controller)
        except ValueError as e:
            self.show_info(e.__str__(), status=400)

    def show_all_book(self, controller: "ConsoleController"):
        books = controller.get_all_book()
        for book in books:
            self.show_info(book)

    def update_status_book(self, book_id: str, status: BookStatus, controller: "ConsoleController"):
        response = controller.update_status_book(book_id, status)
        self.show_info(response.message, response.status)

    def get_info_fo_update_status_book(self, controller: "ConsoleController"):
        book_id = input("Введите id книги для изменения статуса: ")
        m_factory(
            ("Изменить статус книги на 'в наличии'", self.update_status_book,
             (book_id, BookStatus.IN_STOCK, controller)),
            ("Изменить статус книги на 'выдана'", self.update_status_book, (book_id, BookStatus.ISSUED, controller)),
            title="Статус книги"
        ).draw()

    def show_info(self, text: str, status: int = 200):
        if 200 <= status <= 299:
            print(f"\x1b[0;30;42m{text}\x1b[0m")
        elif 400 <= status <= 499:
            print(f'\x1b[0;31;40m{text}\x1b[0m')
        else:
            print(text)

    def __get_author_data(self) -> tuple[str, str, str]:
        surname = input("Введите Фамилию автора: ").title()
        name = input("Введите Имя автора: ").title()
        patronymic = input("Введите Отчество автора: ").title()
        return surname, name, patronymic

    def __create_author(self, surname, name, patronymic):
        return Author(surname, name, patronymic)

    def __get_info_and_create_author(self):
        return self.__create_author(*self.__get_author_data())

    def __get_year_data(self):
        return input("Введите год издания книги: ")

    def __create_year(self, year: str):
        return BookYear(year)

    def __get_info_and_create_year(self):
        return self.__create_year(self.__get_year_data())
