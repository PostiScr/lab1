from pathlib import Path
from application.employee_service import EmployeeService
from application.position_service import PositionService
from application.report_service import ReportService
from infrastructure.json_employee_repository import JsonEmployeeRepository
from infrastructure.json_positions_repository import JsonPositionRepository
from presentation.console import ConsoleApp

def main() -> None:
    data_file = Path(__file__).parent / "employees.json"

    emp_rep = JsonEmployeeRepository(data_file / "employees.json")
    pos_rep = JsonPositionRepository(data_file / "positions.json")

    emp_service = EmployeeService(emp_rep, pos_rep)
    pos_service = PositionService(pos_rep)
    report_service = ReportService(emp_service)

    if not pos_service.get_all():
        print("Первый запуск: создание базовых должностей...")
        base_positions = [
            ("Сотрудник", 40000.0),
            ("Разработчик", 80000.0),
            ("Менеджер", 70000.0),
            ("Дизайнер", 60000.0),
            ("Продажник", 50000.0),
            ("Стажёр", 20000.0)
        ]
        for title, rate in base_positions:
            pos_service.add_position(title, rate)
        print("Базовые должности успешно созданы")

    app = ConsoleApp(emp_service, pos_service, report_service)
    app.run()

if __name__ == "__main__":
    main()