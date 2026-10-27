from classroom import Classroom
from student import Student


def create_classroom() -> Classroom:
    classroom = Classroom("Pythonクラス")
    classroom.add_student(Student("田中", [80, 90, 70]))
    classroom.add_student(Student("佐藤", [50, 60, 55]))
    classroom.add_student(Student("鈴木", []))
    return classroom
