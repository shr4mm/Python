from student import Student
from desired_success import DesiredSuccess
from studentData import StudentData
from database import Database


def main():
    db = Database()
    student = Student("Кузьменко Олександр", "ІСД-32", "2006-02-01", "Київ")

    subjects = ["Нейро", "Python", "Voip"]
    real_grades = [85, 90, 78]
    desired_grades = [95, 98, 92]

    data = StudentData(student, subjects, real_grades, desired_grades)
    db.insert_student(
        pib=data.student.get_pib(),
        group_number=data.student.get_group_number(),
        birth_date=student.get_birth_date(),
        avg_real=data.real_average(),
        avg_desired=data.desired_average(),
    )

    for row in db.get_all_students():
     print(row)
if __name__ == "__main__":
    main()
