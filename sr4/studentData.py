from abc import ABC

from success import Success
from desired_success import DesiredSuccess

class StudentData:
    def __init__(self, student, real_subjects, real_grades, desired_grades):
        self.student = student
        self.real_success = RealSuccess(real_subjects, real_grades)
        self.desired_success = DesiredSuccess(real_subjects, desired_grades)


    def real_average(self):
        return self.real_success.average_score()
    def desired_average(self):
        return self.desired_success.average_score()

class RealSuccess(Success, ABC):
    def __init__(self, subjects, grades):
      super().__init__(subjects, grades)
    def average_score(self):
      if not self.grades:
        return 0
      return sum(self.grades) / len(self.grades)