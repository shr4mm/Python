from abc import ABC

from success import Success

class DesiredSuccess(Success, ABC):
    def __init__(self, subjects, desired_grades):
        super().__init__(subjects, desired_grades)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)