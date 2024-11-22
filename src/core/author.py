from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Author:
    surname: str
    name: str
    patronymic: str

    def __post_init__(self):
        self.validate()

    def validate(self):
        for k, v in self.__dict__.items():
            if not isinstance(v, str):
                raise ValueError(f"Все поля Author должны быть str, {k} type: {type(v)}")
            if len(v) == 0:
                raise ValueError(f'{self.__class__.__name__}: {k} не может быть пустым')

    def __str__(self):
        return f"{self.surname} {self.name[0]}.{self.patronymic[0]}."

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def loads_json(json: dict) -> "Author":
        return Author(
            surname=json.get("surname", ""),
            name=json.get("name", ""),
            patronymic=json.get("patronymic", ""),
        )
