from domain.employee_repository import IRepository
from domain.position_repository import IPositionRepository
from domain.employee import Employee
from domain.exceptions import EmployeeNotFoundError, PositionNotFoundError

class EmployeeService:
    def __init__(self, repository: IRepository, pos_repository: IPositionRepository):
        self.repository = repository
        self.pos_repository = pos_repository

    def get_all(self) -> list[Employee]:
        # Получить список всех сотрудников
        return self.repository.get_all()

    def add_employee(self, employee: Employee) -> None:
        # Добавление нового сотрудника
        if employee.id <= 0:
            raise ValueError("ID должен быть положительным числом")

        employees = self.repository.get_all()

        if any(e.id == employee.id for e in employees):
            raise ValueError(f"Сотрудник с ID {employee.id} уже существует")

        positions = self.pos_repository.get_all()
        if not any(p.id == employee.position_id for p in positions):
            raise PositionNotFoundError(f"Должности с ID {employee.position_id} не существует")

        employees.append(employee)
        self.repository.save_all(employees)

    def change_position(self, emp_id: int, new_pos_id: int) -> None:
        # Изменение должности
        positions = self.repository.get_all()
        if not any(p.id == new_pos_id for p in positions):
            raise PositionNotFoundError(f"Должности с ID {new_pos_id} не существует")

        employees = self.repository.get_all()
        for emp in employees:
            if emp.id == emp_id:
                emp.position_id = new_pos_id
                self.repository.save_all(employees)
                return
        raise EmployeeNotFoundError(f"Сотрудник с ID {emp_id} не найден")

    def calculate_salary(self, emp_id: int) -> float:
        # Вычисление зарплаты
        employees = self.repository.get_all()
        for emp in employees:
            if emp.id == emp_id:
                positions = self.position_repo.get_all()
                for pos in positions:
                    if pos.id == emp.position_id:
                        return emp.calculate_salary(pos)
                raise PositionNotFoundError(f"Должности с ID {emp.position_id} не существует")
        raise EmployeeNotFoundError(f"Сотрудник с ID {emp_id} не найден")

    def delete_employee(self, emp_id: int) -> None:
        # Удаление сотрудника
        employees = self.repository.get_all()

        filtered = [e for e in employees if e.id != emp_id]

        if len(filtered) == len(employees):
            raise EmployeeNotFoundError(f"Сотрудник с ID {emp_id} не найден")

        self.repository.save_all(filtered)