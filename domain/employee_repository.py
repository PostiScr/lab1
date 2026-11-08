from abc import ABC, abstractmethod
from domain.employee import Employee

class IRepository(ABC):
    # Работа с хранилищем

    @abstractmethod
    def get_all(self) -> list[Employee]:
        # Получить список всех сотрудников
        pass

    @abstractmethod
    def save_all(self, employees: list[Employee]) -> None:
         # Сохранить список сотрудников
         pass