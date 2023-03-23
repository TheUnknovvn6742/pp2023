# ____________________LIBRARIES AND CONFIGS____________________

from dataclasses import dataclass
import math
import numpy as np
try:
    import polars as pl
except ModuleNotFoundError:
    import os
    os.system('pip install polars')
pl.Config.set_tbl_hide_column_data_types(True)
pl.Config.set_tbl_hide_dataframe_shape(True)

# ____________________DATA SECTION____________________

students = []
students_name = []
courses = []
courses_name = []
num_student: int
num_courses: int


@dataclass
class Base:
    _name: str
    _id: str

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @name.setter
    def name(self, input_name):
        self._name = input_name

    @id.setter
    def id(self, input_id):
        self._id = input_id

    def __repr__(self) -> str:
        return f"""Student {self.name}:
        Id: {self.id}"""

    @classmethod
    def get_input(cls):
        input_name = input("Enter the name: ")
        input_id = input("Enter the id: ")
        return Base(input_name, input_id)


class Student(Base):
    __dob: str

    @property
    def dob(self):
        return self.__dob

    @dob.setter
    def dob(self, input_dob):
        self.__dob = input_dob

    @classmethod
    def get_input(cls):
        print("Enter the data for student.\n")
        x = super().get_input()
        input_dob = input("Enter the date of birth: ")
        return Student(x.name.title(), x.id, input_dob)

    def __init__(self, input_name, input_id, input_dob):
        self.id = input_id
        self.name = input_name
        self.dob = input_dob

    def __repr__(self) -> str:
        return f"""{super().__repr__()}
        Date of birth: {self.dob}"""


# @dataclass
class Course(Base):

    __credit: int

    @property
    def credit(self):
        return self.__credit
    
    @credit.setter
    def credit(self, input_credit):
        self.credit = input_credit

    def __init__(self, input_name, input_id, input_credit):
        self.id = input_id
        self.name = input_name
        self.dob = input_credit

    @classmethod
    def get_input(cls):
        print("Enter the data for course.\n")
        x = super().get_input()
        while True:
            input_credit = input("Enter the number of credit for this course: ")
            if validate_number(input_credit):
                break
            else:
                print(f"\"{input_credit}\" is not a valid value. Must be an integer and at least 1.\n")
        return Course(x.name.capitalize(), x.id, input_credit)

    def __repr__(self) -> str:
        return f"""Course {self.name}:
        Id: {self.id}"""


class Mark(pl.DataFrame):
    def add_subject(self, subject_name, mark_list):
        return self.with_columns(
            [
                pl.Series(subject_name, mark_list)
            ]
        )

    def add_student(self, student_list):
        return self.select(
            [
                pl.Series("Name", student_list),
                pl.all()
            ]
        )


# ____________________FUNCTION SECTION____________________

def validate_number(x: str):
    try:
        return (int(str(x)) >= 1)
    except ValueError:
        return False


def validate_mark(x: str):
    try:
        return (float(str(x)) >= 0) and (float(str(x)) <= 10)
    except ValueError:
        return False


def get_num(input_type: str) -> str:
    while True:
        if (input_type == "student"):
            x = input("Enter the number of students: ")
        elif (input_type == "course"):
            x = input("Enter the number of courses: ")
        if validate_number(x):
            return int(x)
        print(f"\"{x}\" is not a valid value. Must be an integer and at least 1.\n")


def enter_students(num_student, students, students_name):
    # Enter each student
    for i in range(num_student):
        print(f"Student {i+1}")
        students.append(Student.get_input())
        students_name.append(students[-1].name)
        print()


def enter_course(num_course, courses, courses_name):
    # Enter each course
    for i in range(num_course):
        print(f"Course {i+1}")
        courses.append(Course.get_input())
        courses_name.append(courses[-1].name)
        print()


def enter_mark(c: Mark):
    # Enter course
    while True:
        mark_course = input("Enter the course to give mark: ").capitalize()
        if (mark_course in courses_name):
            break
        print(f"{mark_course} is not an available course\n")
    mark_list = []
    for x in students_name:
        # Get grades
        while True:
            student_grade = input(f"Enter the mark for {x}: ")
            if validate_mark(student_grade):
                mark_list.append(round(student_grade, 1))
                break
            else:
                print(
                    f"\"{student_grade}\" is not a valid value. Must be a number between 0 and 10.\n")
    return c.add_subject(mark_course, mark_list)


def list_students(students):
    if (len(students) == 0):
        print("There is no data for students to list yet.\n")
    else:
        print(f"\nThere are {len(students)} students")
        for student in students:
            print(student)


def list_courses(courses):
    if (len(courses) == 0):
        print("\nThere is no data for courses to list yet.\n")
    else:
        print(f"There are {len(courses)} courses")
        for course in courses:
            print(course)


def list_mark(c: Mark):
    while True:
        mark_course = input("Enter the course to give mark: ").capitalize()
        if (mark_course in c.columns):
            break
        print(
            f"{mark_course} is not an available course or not a course that has mark\n")
    print(c.select(["Name", mark_course]))


def main():
    marks = Mark()
    while True:
        choice = input(
            "What do you want to do. Input data(I/i), List data(L/l) or exit(E/e): ").lower()
        if choice == "i":
            while True:
                choice = input(
                    "\nDo you want to input student(S/s), course(C/c) or mark(M/m) data: ").lower()
                if choice == "s":
                    num_student = get_num("student")
                    enter_students(num_student, students, students_name)
                    marks = marks.add_student(students_name)
                    break
                elif choice == "c":
                    num_course = get_num("course")
                    enter_course(num_course, courses, courses_name)
                    break
                elif choice == "m":
                    if (len(students_name)*len(courses_name) != 0):
                        marks = enter_mark(marks)
                    else:
                        print(
                            "There is no data for either student or course, can't enter mark now.\n")
                    break
                else:
                    print(
                        f"Option {choice} is not available, please try again.\n")
        elif choice == "l":
            while True:
                choice = input(
                    "\nWhich do you want to list, student(S/s), course(C/c), mark(M/m) or GPA(G/g) data: ").lower()
                if choice == "s":
                    list_students(students)
                    break
                elif choice == "c":
                    list_courses(courses)
                    break
                elif choice == "m":
                    if (len(students_name)*len(courses_name) != 0) and (marks.shape[1] > 1):
                        list_mark(marks)
                    else:
                        print(
                            "There is no data for either student or course or there is no data for mark yet, can't list marks now.\n")
                    break
                elif choice == "g":
                    pass
                else:
                    print(
                        f"Option {choice} is not available, please try again.")
                pass
        elif choice == "e":
            print("Thanks for using. Goodbye!\n")
            exit()
        else:
            print(f"Option \"{choice}\" is not available, please try again.\n")


# ___________________MAIN SECTION___________________

if __name__ == "__main__":
    main()
