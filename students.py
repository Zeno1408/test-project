from typing import Any
from pprint import pprint


class Student:
    def __init__(self, students: list[dict[str, Any]]) -> None:
        self.students = students

    def display_students(self) -> list[dict[str, Any]]:
        return self.students

    def search_student(self, student_id: int):
        if any(d.get("id") == student_id for d in self.students):
            return f"Student with student_id {student_id} found."
        return f"Student with student_id {student_id} not found."

    def add_student(self, new_student: dict):
        if new_student not in self.students:
            self.students.append(new_student)
            return self.students

    def delete_student(self, student_id: int):
        for x in self.students:
            if x["id"] == student_id:
                self.students.pop(student_id - 1)
        return self.students


if __name__ == "__main__":
    STUDENTS_LIST = [
        {"id": 1, "Name": "Aditya Dilip", "Age": 24},
        {"id": 2, "Name": "Sanjana Shylesh", "Age": 23},
        {"id": 3, "Name": "Aiman Sarin", "Age": 24},
        {"id": 4, "Name": "Rakesh Dama", "Age": 23},
        {"id": 5, "Name": "Suraj Kumar", "Age": 24},
    ]
    student = Student(STUDENTS_LIST)
    new_student = {"id": 6, "Name": "Shrey Shylesh", "Age": 25}
    # display = student.display_students()
    search = student.search_student(4)
    # add = student.add_student(new_student)
    # delete = student.delete_student(4)
    pprint(search)
