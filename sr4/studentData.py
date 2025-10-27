
from success import Success
from desired_success import DesiredSuccess

class StudentData:
    def __init__(self, student, real_subjects, real_grades, desired_grades):
        self.student = student
        self.real_success = Success(real_subjects, real_grades)
        self.desired_success = DesiredSuccess(real_subjects, desired_grades)

    def real_average(self):
        if not self.real_success.grades:
            return 0
        return sum(self.real_success.grades) / len(self.real_success.grades)

    def desired_average(self):
        return self.desired_success.average_grade()