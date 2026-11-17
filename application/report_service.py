from application.employee_service import EmployeeService
from pathlib import Path

class ReportService:
    def __init__(self, employee_service: EmployeeService):
        self.employee_service = employee_service

    def generate_salary_report(self, min_salary: float, max_salary: float, filepath: Path) -> int:
        # Создание отчёта в формате txt. Возвращает количество найденых сотрудников
        employees = self.employee_service.get_all()
        found_count = 0

        with open(filepath, "w", encoding="utf-8") as file:
            file.write("ОТЧЕТ ПО ЗАРПЛАТАМ\n")
            file.write(f"Диапазон: от {min_salary} до {max_salary}\n\n")

            for emp in employees:
                salary = self.employee_service.calculate_salary(emp.id)
                if min_salary <= salary <= max_salary:
                    file.write(f"ID: {emp.id} | {emp.get_role()} | {emp.name} | ЗП: {salary:.2f}\n")
                    found_count += 1

            if found_count == 0:
                file.write("Сотрудников с такой зарплатой не найдено.\n")

        return found_count