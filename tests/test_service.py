import unittest
from application.employee_service import EmployeeService
from domain.employee import Developer, Employee
from domain.employee_repository import IRepository
from domain.exceptions import EmployeeNotFoundError, InvalidSalaryError

class InMemoryRepository(IRepository):
    # Репозиторий для тестов
    def __init__(self):
        self.employees = []

    def get_all(self) -> list[Employee]:
        return self.employees

    def save_all(self, employees: list[Employee]) -> None:
        self.employees = employees

class EmployeeServiceTest(unittest.TestCase):
    def setUp(self):
        self.service = EmployeeService(InMemoryRepository())

    def test_add_employee_success(self):
        emp = Developer(id=1, name="Иван", salary=50000, programming_language="Python")
        self.service.add_employee(emp)

        self.assertEqual(len(self.service.get_all()), 1)
        self.assertEqual(self.service.get_all()[0].name, "Иван")

    def test_add_employee_invalid_salary(self):
        emp = Employee(id=1, name="Петр", salary=-100)

        with self.assertRaises(InvalidSalaryError):
            self.service.add_employee(emp)

    def test_add_duplicate_id(self):
        emp1 = Employee(id=1, name="Иван", salary=100)
        emp2 = Employee(id=1, name="Петр", salary=200)
        self.service.add_employee(emp1)

        with self.assertRaises(ValueError):
            self.service.add_employee(emp2)

    def test_delete_non_existent_employee(self):
        with self.assertRaises(EmployeeNotFoundError):
            self.service.delete_employee(999)

if __name__ == "__main__":
    unittest.main()
      