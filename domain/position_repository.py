from abc import ABC, abstractmethod
from domain.position import Position

class IPositionRepository(ABC):
    # Работа с хранилищем должностей

    @abstractmethod
    def get_all(self) -> list[Position]:
        # Получить список должностей
        pass

    @abstractmethod
    def save_all(self, positions: list[Position]) -> None:
        # Сохранить список должностей
        pass