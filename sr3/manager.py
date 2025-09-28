from employee import Employee


class Manager(Employee):
    premium=3000
    def __init__(self, name, salary, days_worked,bonus=0 ,number_of_subordinates=0):
        super().__init__(name,salary,days_worked,bonus)
        self._number_of_subordinates = number_of_subordinates

    def get_number_of_subordinates(self):
        return self._number_of_subordinates

    def set_number_of_subordinates(self, number):
     self._number_of_subordinates = number

    def bonus(self):
        return super().bonus()+ (self._number_of_subordinates * Manager.premium)

    def report(self):
        return f"Менеджер {self._name} керує {self._number_of_subordinates} співробітниками."