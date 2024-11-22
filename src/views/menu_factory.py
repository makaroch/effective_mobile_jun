from .console_menu import ConsoleMenu, ConsoleMenuItem


def m_factory(*menu_items, title: str | None = None) -> ConsoleMenu:
    """
    Фабрика консольных менюшек возвращает готовое меню
    :param tuple menu_items:
        кортежи необходимые для создания пунктов меню, один кортеж описывает один пункт меню
        поддерживается следующие форматы:
            ("description, Callable, *args),
            ("description, Callable),
                где description - описание пункта меню, Callable - вызываемый объект, *args - аргументы для Callable
        например: следующий кортеж ("пункт1", lambda x: print(x), (1,))
        создаст пункт меню с названием пункт1 при выборе которого в консоль будет печататься 1
    :raises: :class: `ValueError` при не верном кортеже
    :param str or None title: заголовок меню
    :return: консольное меню
    :rtype: ConsoleMenu
    """
    items = []
    for item in menu_items:
        if len(item) == 3:
            console_menu_item = ConsoleMenuItem(description=item[0], funk=item[1], args=item[2])
        elif len(item) == 2:
            console_menu_item = ConsoleMenuItem(description=item[0], funk=item[1])
        else:
            raise ValueError("Неверный кортеж данных")
        items.append(console_menu_item)
    return ConsoleMenu(menu_items=items, title=title)
