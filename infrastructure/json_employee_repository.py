import json
from pathlib import Path
from dataclasses import asdict

from domain.employee_repository import IRepository
from domain.employee import Employee, Developer, Manager, Designer, Salesman, Intern

class JsonEmployeeRepository(IRepository):
    # Реализация хранения данных о сотрудниках в формате JSON

    def __init__(self, file_path: Path):
        self.file_path = file_path

    def get_all(self) -> list[Employee]:
        # Считать все данные из файла
        if not self.file_path.exists():
            return[]

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("Файл JSON повреждён или пуст")
            return []

        employees = []
        for item in data:
            role = item.pop("role", "Employee")

            match role:
                case "Developer":
                    employees.append(Developer(**item))
                case "Manager":
                    employees.append(Manager(**item))
                case "Designer":
                    employees.append(Designer(**item))
                case "Salesman":
                    employees.append(Salesman(**item))
                case "Intern":
                    employees.append(Intern(**item))
                case _:
                    employees.append(Employee(**item))

        return employees

    def save_all(self, employees: list[Employee]) -> None:
        # Сохрнанение объектов в JSON-файл

        data = []
        for emp in employees:
            emp_dict = {
                "role" : emp.__class__.__name__,
                **asdict(emp)
            }
            data.append(emp_dict)

        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)