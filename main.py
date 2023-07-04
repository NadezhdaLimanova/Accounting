from application.db.people import Employees
from application.salary import Salary
from datetime import datetime
import pyjokes

if __name__=='__main__':
    name = 'Иван'
    surname = 'Смирнов'
    work_days = 18
    salary_rate = 60000

    current_datetime = datetime.now()
    employees = Employees(name, surname)
    salary = Salary(salary_rate, work_days, surname)

    print(employees.get_employees())
    print(salary.calculate_salary())
    print(current_datetime)
    print(pyjokes.get_joke())



