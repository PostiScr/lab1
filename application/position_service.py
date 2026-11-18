from domain.position_repository import IPositionRepository
from domain.position import Position
from domain.exceptions import PositionNotFoundError

class PositionService:
    def __init__(self, repository: IPositionRepository):
        self.repository = repository

    def get_all(self) -> list[Position]:
        # Получить список должностей
        return self.repository.get_all()

    def add_position(self, title: str, base_rate: float) -> Position:
        # Добавление новой должности
        positions = self.repository.get_all()
        next_id = max((pos.id for pos in positions), default=0) + 1
        new_pos = Position(id=next_id, title=title, base_rate=base_rate)
        positions.append(new_pos)
        self.repository.save_all(positions)
        return new_pos

    def update_rate(self, position_id: int, new_rate:float) -> None:
        # Изменение базовой ставки
        positions = self.repository.get_all()
        for pos in positions:
            if pos.id == position_id:
                pos.base_rate = new_rate
                self.repository.save_all(positions)
                return
        raise PositionNotFoundError(f"Должность с ID {position_id} не найдена")