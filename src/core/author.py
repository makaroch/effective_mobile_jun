from dataclasses import dataclass


@dataclass
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

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    def __repr__(self):
        return self.__str__()
