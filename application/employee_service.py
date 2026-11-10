from domain.employee_repository import IRepository
from domain.employee import Employee
from domain.exceptions import EmployeeNotFoundError, InvalidSalaryError

class EmployeeService:
    def __init__(self, repository: IRepository):
        self.repository = repository

    def get_all(self) -> list[Employee]:
        # Получить список всех сотрудников
        return self.repository.get_all()

    def add_employee(self, employee: Employee) -> None:
        # Добавление нового сотрудника
        if employee.salary <= 0:
            raise InvalidSalaryError("Зарлата должна быть больше нуля")
        if employee.id <= 0:
            raise ValueError("ID должен быть положительным числом")

        employees = self.repository.get_all()

        if any(e.id == employee.id for e in employees):
            raise ValueError(f"Сотрудник с ID {employee.id} уже существует")

        employees.append(employee)
        self.repository.save_all(employees)

    def update_salary(self, emp_id: int, new_salary: float) -> None:
        # Изменение зарплаты сотрудника
        if new_salary <= 0:
            raise InvalidSalaryError("Зарплата должна быть больше нуля")

        employees = self.repository.get_all()
        for emp in employees:
            if emp.id == emp_id:
                emp.salary = new_salary
                self.repository.save_all(employees)
                return

        raise EmployeeNotFoundError(f"Сотрудник с ID {emp_id} не найден")

    def delete_employee(self, emp_id: int) -> None:
        # Удаление сотрудника
        employees = self.repository.get_all()

        filtered = [e for e in employees if e.id != emp_id]

        if len(filtered) == len(employees):
            raise EmployeeNotFoundError(f"Сотрудник с ID {emp_id} не найден")

        self.repository.save_all(filtered)