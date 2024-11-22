from dataclasses import dataclass

@dataclass(frozen=True)
class Response:
    """
    Сущность в виде гномика(Описание ответа сервера)
    """
    message: str
    status: int = 200