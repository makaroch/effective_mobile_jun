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
            author = self.__get_author_data()
            year = BookYear(input("Введите год издания книги: "))
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
            self.show_info((e.__str__()))

    def get_info_fo_del_book(self, controller: "ConsoleController"):
        book_id = input("Введите id книги для удаления: ")
        response = controller.del_book(book_id)
        self.show_info(response.message, response.status)

    def get_info_fo_search_book(self, controller: "ControllerBase"):
        pass

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
        print(text)

    def __get_author_data(self) -> Author:
        surname = input("Введите Фамилию автора: ").title()
        name = input("Введите Имя автора: ").title()
        patronymic = input("Введите Отчество автора: ").title()
        return Author(surname, name, patronymic)
