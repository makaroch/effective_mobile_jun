from src.views.console_view import ConsoleView
from src.models.console_model import ConsoleModel
from src.controllers.console_controller import ConsoleController


def main():
    view = ConsoleView()
    model = ConsoleModel()
    controller = ConsoleController(view, model)
    while True:
        controller.show_main_menu()


if __name__ == '__main__':
    main()
