# Объявление Исключений

class EmployeeNotFoundError(Exception):
    # Сотрудник не найден
    pass

class InvalidSalaryError(Exception):
    # указана некоррекстная зарплата
    pass

class PositionNotFoundError(Exception):
    # Должность не найдена
    pass