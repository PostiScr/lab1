from dataclasses import dataclass

@dataclass
class Employee:
    # Базовый класс для всех сотрудников
    id: int
    name: str
    salary: float

    def get_role(self) -> str:
        # Возвращает должность
        return "Сотрудник"

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