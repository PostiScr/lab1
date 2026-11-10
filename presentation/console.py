from application.employee_service import EmployeeService
from domain.employee import Employee, Developer, Manager, Designer, Salesman, Intern
from domain.exceptions import EmployeeNotFoundError, InvalidSalaryError

class ConsoleApp:
    def __init__(self, service: EmployeeService):
        self.service = service

    def run(self) -> None:
        while True:
            print(">>> СИСТЕМА УПРАВЛЕНИЯ ПЕРСОНАЛОМ <<<")
            print("1. Вывести всех сотрудников")
            print("2. Добавить сотрудника")
            print("3. Изменить зарплату")
            print("4. Удалить сотрудника")
            print("0. Выход")

            choiсe = input("Выберите действие: ").strip()

            try:
                match choiсe:
                    case "1":
                        employees = self.service.get_all()
                        if not employees:
                            print("Список пуст.")
                        for emp in employees:
                            print(f"ID: {emp.id} | Должность: {emp.get_role()} | Имя: {emp.name} | Зарплата: {emp.salary}")

                    case "2":
                        self._add_employee_menu()

                    case "3":
                        emp_id = int(input("Введите ID сотрудника: "))
                        new_salary = float(input("Введите новую зарплату: "))
                        self.service.update_salary(emp_id, new_salary)
                        print("Зарплата успешно обновлена")

                    case "4":
                        emp_id = int(input("Введите ID сотрудника для удаления: "))
                        self.service.delete_employee(emp_id)
                        print("Сотрудник успешно удалён")

                    case "0":
                        print("Завершение работы")
                        break

                    case _:
                        print("Неизвестная команда. Попробуйте снова.")

            except EmployeeNotFoundError as e:
                print(f"Ошибка: {e}")
            except InvalidSalaryError as e:
                print(f"Ошибка зарплаты: {e}")
            except ValueError as e:
                print(f"Ошибка ввода: {e}")
            except (KeyboardInterrupt, EOFError):
                print("Программа была прервана")
                break

    def _add_employee_menu(self) -> None:
        # Метод для добавления сотрудников
        print("Выберите должность: ")
        print("1. Разработчик")
        print("2. Менеджер")
        print("3. Дизайнер")
        print("4. Продажник")
        print("5. Стажёр")
        print("6. Без должности ('Сотрудник')")

        role_choice = input("Ввод: ").strip()
        emp_id = int(input("ID: "))
        name = input("Имя: ")
        salary = float(input("Зарплата: "))

        match role_choice:
            case "1":
                lang = input("Язык программирования: ")
                emp = Developer(id=emp_id, name=name, salary=salary, programming_language=lang)
            case "2":
                subs = int(input("Количество подчинённых: "))
                emp = Manager(id=emp_id, name=name, salary=salary, subordinates_count=subs)
            case "3":
                proj = int(input("Количество проектов: "))
                emp = Designer(id=emp_id, name=name, salary=salary, projects_count=proj)
            case "4":
                clients = int(input("Количество клиентов: "))
                emp = Salesman(id=emp_id, name=name, salary=salary, clients_count=clients)
            case "5":
                exp = int(input("Месяцев опыта: "))
                emp = Intern(id=emp_id, name=name, salary=salary, months_of_experience=exp)
            case _:
                emp = Employee(id=emp_id, name=name, salary=salary)

        self.service.add_employee(emp)
        print("Сотрудник успешно добавлен")
