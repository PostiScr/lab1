from pathlib import Path
from application.employee_service import EmployeeService
from application.position_service import PositionService
from application.report_service import ReportService
from domain.employee import Employee, Developer, Manager, Designer, Salesman, Intern
from domain.exceptions import EmployeeNotFoundError, InvalidSalaryError, PositionNotFoundError

class ConsoleApp:
    def __init__(self, emp_service: EmployeeService, pos_service: PositionService, report_service: ReportService):
        self.emp_service = emp_service
        self.pos_service = pos_service
        self.report_service = report_service

    def run(self) -> None:
        while True:
            print(">>> СИСТЕМА УПРАВЛЕНИЯ ПЕРСОНАЛОМ <<<")
            print("1. Вывести всех сотрудников")
            print("2. Добавить сотрудника")
            print("3. Изменить должность сотрудника")
            print("4. Удалить сотрудника")
            print("5. Управление должностями")
            print("6. Сформировать отчет по зарплатам")
            print("0. Выход")

            choice = input("Выберите действие: ").strip()

            try:
                match choice:
                    case "1":
                        employees = self.emp_service.get_all()
                        if not employees:
                            print("Список пуст.")
                        for emp in employees:
                            print(f"ID: {emp.id} | Должность: {emp.get_role()} | Имя: {emp.name} | Зарплата: {self.emp_service.calculate_salary(emp.id)}")

                    case "2":
                        self._add_employee_menu()

                    case "3":
                        self._change_employee_position()

                    case "4":
                        emp_id = int(input("Введите ID сотрудника для удаления: "))
                        self.emp_service.delete_employee(emp_id)
                        print("Сотрудник успешно удалён")

                    case "5":
                        self._manage_positions()

                    case "6":
                        self._generate_report()

                    case "0":
                        print("Завершение работы")
                        break

                    case _:
                        print("Неизвестная команда. Попробуйте снова.")

            except EmployeeNotFoundError as e:
                print(f"Ошибка: {e}")
            except PositionNotFoundError as e:
                print(f"Ошибка должности: {e}")
            except InvalidSalaryError as e:
                print(f"Ошибка зарплаты: {e}")
            except ValueError as e:
                print(f"Ошибка ввода: {e}")
            except (KeyboardInterrupt, EOFError):
                print("Программа была прервана")
                break

    def _add_employee_menu(self) -> None:
        # Метод для добавления сотрудников
        emp_id = int(input("ID: "))
        name = input("Имя: ")

        print("Доступные должности:")
        for pos in self.pos_service.get_all():
            print(f"  ID {pos.id}: {pos.title} (ставка {pos.base_rate})")

        position_id = int(input("ID должности: "))
        coefficient = float(input("Личный коэффициент: "))

        print("Выберите роль: ")
        print("1. Разработчик")
        print("2. Менеджер")
        print("3. Дизайнер")
        print("4. Продажник")
        print("5. Стажёр")
        print("6. Без роли ('Сотрудник')")

        role_choice = input("Ввод: ").strip()

        match role_choice:
            case "1":
                lang = input("Язык программирования: ")
                emp = Developer(id=emp_id, name=name, position_id=position_id, coefficient=coefficient, programming_language=lang)
            case "2":
                subs = int(input("Количество подчинённых: "))
                emp = Manager(id=emp_id, name=name, position_id=position_id, coefficient=coefficient, subordinates_count=subs)
            case "3":
                proj = int(input("Количество проектов: "))
                emp = Designer(id=emp_id, name=name, position_id=position_id, coefficient=coefficient, projects_count=proj)
            case "4":
                clients = int(input("Количество клиентов: "))
                emp = Salesman(id=emp_id, name=name, position_id=position_id, coefficient=coefficient, clients_count=clients)
            case "5":
                exp = int(input("Месяцев опыта: "))
                emp = Intern(id=emp_id, name=name, position_id=position_id, coefficient=coefficient, months_of_experience=exp)
            case _:
                emp = Employee(id=emp_id, name=name, position_id=position_id, coefficient=coefficient)

        self.emp_service.add_employee(emp)
        print("Сотрудник успешно добавлен")

    def _change_employee_position(self) -> None:
        emp_id = int(input("Введите ID сотрудника: "))
        
        print("Доступные должности:")
        for pos in self.pos_service.get_all():
            print(f"  ID {pos.id}: {pos.title}")
            
        new_pos_id = int(input("Введите новый ID должности: "))
        self.emp_service.change_position(emp_id, new_pos_id)
        print("Должность успешно изменена")

    def _manage_positions(self) -> None:
        while True:
            print("1. Показать все должности")
            print("2. Добавить должность")
            print("3. Изменить ставку должности")
            print("0. Назад в главное меню")
            choice = input("Выберите действие: ").strip()

            match choice:
                case "0":
                    break
                case "1":
                    for pos in self.pos_service.get_all():
                        print(f"ID: {pos.id} | {pos.title} | Базовая ставка: {pos.base_rate}")
                case "2":
                    title = input("Название должности: ")
                    rate = float(input("Базовая ставка: "))
                    self.pos_service.add_position(title, rate)
                    print("Должность добавлена")
                case "3":
                    pos_id = int(input("ID должности: "))
                    new_rate = float(input("Новая ставка: "))
                    self.pos_service.update_rate(pos_id, new_rate)
                    print("Ставка обновлена!")
                case _:
                    print("Неизвестная команда. Попробуйте снова.")

    def _generate_report(self) -> None:
        min_sal = float(input("Минимальная зарплата: "))
        max_sal = float(input("Максимальная зарплата: "))

        filepath = Path(__file__).parent.parent / "salary_report.txt"
        
        count = self.report_service.generate_salary_report(min_sal, max_sal, filepath)
        
        print(f"\nОтчет успешно сформирован")
        print(f"Найдено сотрудников: {count}")