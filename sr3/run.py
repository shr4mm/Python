from employee import Employee
from manager import Manager

employee1 = Employee("Дмитро", 33000, 15, 4)
employee2 = Employee("Денис", 20000, 20, 8)
employee3 = Employee("Олексій", 20000, 20, 3)
employee4 = Employee("Олександр", 20000, 20, 10)

manager1 = Manager("Олена", 40000, 26, 10, 5)
manager2 = Manager("Сергій", 50000, 20, 15, 8)

command = [employee1, employee2,employee3,employee4, manager1, manager2]

for i in command:
    print(f"Працівник: {i.get_name()}")
    print(f"Зарплата: {i.calculate_monthly_salary():.2f} грн")
    print(f"Бонус: {i.bonus():.2f} грн")
    if isinstance(i, Manager):
     print(i.report())