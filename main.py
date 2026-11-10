from pathlib import Path
from application.employee_service import EmployeeService
from infrastructure.json_employee_repository import JsonEmployeeRepository
from presentation.console import ConsoleApp

def main() -> None:
    data_file = Path(__file__).parent / "employees.json"

    repository = JsonEmployeeRepository(data_file)

    service = EmployeeService(repository)

    app = ConsoleApp(service)
    app.run()

if __name__ == "__main__":
    main()