from abc import ABC, abstractmethod


class MenuBase(ABC):
    @abstractmethod
    def _draw(self):
        pass

    @abstractmethod
    def _get_user_input(self):
        pass

    @abstractmethod
    def draw(self):
        pass
