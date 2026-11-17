from dataclasses import dataclass
from domain.position import Position

@dataclass
class Employee:
    # Базовый класс для всех сотрудников
    id: int
    name: str
    position_id: int
    coefficent: float

    def get_role(self) -> str:
        # Возвращает должность
        return "Сотрудник"

    def calculate_salary(self, position: Position) -> float:
        # Вычисление зарплаты
        return position.base_rate * self.coefficient


@dataclass
class Developer(Employee):
    # Разработчик (наследник Employee)
    programming_language: str = "Python"

    def get_role(self) -> str:
        return "Разработчик"

@dataclass
class Manager(Employee):
    # Менеджер (наследник Employee)
    subordinates_count: int = 0

    def get_role(self) -> str:
        return "Менеджер"

@dataclass
class Designer(Employee):
    # Дизайнер (наследник Employee)
    projects_count: int = 0

    def get_role(self) -> str:
        return "Дизайнер"

@dataclass
class Salesman(Employee):
    # Продажник (наследник Employee)
    clients_count: int = 0

    def get_role(self) -> str:
        return "Продажник"

@dataclass
class Intern(Employee):
    # Стажёр (наследник Employee)
    months_of_experience: int = 0

    def get_role(self) -> str:
        return "Стажёр"