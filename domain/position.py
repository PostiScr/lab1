from dataclasses import dataclass

@dataclass
class Position:
    # Класс для записи базовой ставки для должности
    id: int
    title: str
    base_rate: float