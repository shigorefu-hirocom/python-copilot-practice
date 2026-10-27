from student import Student


class Classroom:
    def __init__(self, name: str):
        self.name = name
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)
