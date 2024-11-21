from dataclasses import dataclass

@dataclass(frozen=True)
class Response:
    message: str
    status: int = 200