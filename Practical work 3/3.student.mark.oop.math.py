# ____________________LIBRARIES AND CONFIGS____________________


from dataclasses import dataclass
import math
import traceback
import numpy as np
try:
    import polars as pl
except ModuleNotFoundError:
    import os
    os.system('pip install polars')
pl.Config.set_tbl_hide_column_data_types(True)
pl.Config.set_tbl_hide_dataframe_shape(True)

# ____________________DATA SECTION____________________

num_student: int = 0
num_course: int = 0


@dataclass
class Base(pl.DataFrame):
    """
    Attribute:
        - `_name`: `list[str]`
        - `_id`: `list[str]`
        - `_num_element`: `int`
        - `_table`: `pl.DataFrame`

    Method:
        - `__init__(self, name, id, number)` -> `None`
        - `init_table(self)` -> `pl.DataFrame`
        - `set_number(cls)` -> `int`
        - `add_element(cls, num_elements)` -> `(list[str], list[str])`
        - `get_data(cls)` -> `__init__`
        - `make_table` -> `None`
        - `display` -> `None`
    """

    @property
    def name(self) -> str:
        return self._name

    @property
    def id(self) -> str:
        return self._id

    @property
    def num_elements(self) -> int:
        return self._num_elements

    @property
    def table(self) -> pl.DataFrame:
        return self._table

    @name.setter
    def name(self, input_name):
        self._name = input_name

    @id.setter
    def id(self, input_id):
        self._id = input_id

    @table.setter
    def table(self, input_table):
        self._table = input_table

    @num_elements.setter
    def num_elements(self, input_num_elements):
        self._num_elements = input_num_elements

    def __init__(self, name, id, number):
        self.name: list[str] = name
        self.id: list[str] = id
        self.num_elements: int = number

    # def init_table(self):
    #     self._table: pl.DataFrame = pl.DataFrame(
    #         {
    #             "Names": [],
    #             "Id": []
    #         },
    #         schema={
    #             "Names": pl.Utf8,
    #             "Id": pl.Utf8
    #         }
    #     )

    @classmethod
    def set_number(cls):
        while True:
            number = input("Enter the number of element: ")
            if validate_number(number):
                return int(number)
                break
            else:
                print(
                    f"\"{number}\" is not a valid number. Must be a number and at least 1.\n")

    @classmethod
    def add_element(cls, num_elements):
        input_name, input_id = [], []
        for i in range(num_elements):
            print(f"Element {i+1}: ")
            input_name.append(input("Enter the name: "))
            input_id.append(input("Enter the id: "))
        return (input_name, input_id)

    @classmethod
    def get_data(cls):
        number = cls.set_number()
        name, id = cls.add_element(number)
        B = Base(name, id, number)
        B.table = pl.DataFrame(
            {
                "Names": B.name,
                "Id": B.id
            },
            schema={
                "Names": pl.Utf8,
                "Id": pl.Utf8
            }
        )
        return B

    def make_table(self):
        self.table = self.table.with_columns(
            pl.DataFrame(
                {
                    "Names": self.name,
                    "Id": self.id
                },
                schema={
                    "Names": pl.Utf8,
                    "Id": pl.Utf8
                }
            )
        )

    def display(self):
        print(self.table)


class Student(Base):
    """
    Attribute:
        - `name`: `list[str]`
        - `id`: `list[str]`
        - `__dob`: `list[str]`
        - `num_element`: `int`
        - `_table`: `pl.DataFrame`

    Method:
        - `__init__(self, name, id, dob,  number)` -> `None`
        - `init_table(self)` -> `pl.DataFrame`
        - `set_number(cls)` -> `int`
        - `add_element(cls, num_elements)` -> `(list[str], list[str], list[str])`
        - `get_data(cls)` -> `__init__`
        - `make_table` -> `None`
        - `display` -> `None`
    """

    @property
    def dob(self):
        return self.__dob

    @property
    def table(self) -> pl.DataFrame:
        return self._table

    @dob.setter
    def dob(self, input_dob):
        self.__dob = input_dob

    @table.setter
    def table(self, input_table):
        self._table = input_table

    def __init__(self, name, id, dob,  number):
        self.name: list[str] = name
        self.id: list[str] = id
        self.dob: list[str] = dob
        self.num_elements: int = number

    @classmethod
    def set_number(cls):
        while True:
            number = input("Enter the number of students: ")
            if validate_number(number):
                return int(number)
                break
            else:
                print(
                    f"\"{number}\" is not a valid value. Must be a integer and at least 1.\n")

    @classmethod
    def add_element(cls, num_elements):
        input_name, input_id, input_dob = [], [], []
        for i in range(num_elements):
            print(f"Student {i+1}: ")
            input_name.append(input("Enter the name: ").title())
            input_id.append(input("Enter the id: "))
            input_dob.append(input("Enter the date of birth: "))
        return (input_name, input_id, input_dob)

    @classmethod
    def get_data(cls):
        number = cls.set_number()
        name, id, dob = Student.add_element(number)
        S = Student(name, id, dob, number)
        S.table = pl.DataFrame(
            {
                "Students name": S.name,
                "Id": S.id,
                "Date of birth": S.dob
            },
            schema={
                "Students name": pl.Utf8,
                "Id": pl.Utf8,
                "Date of birth": pl.Utf8
            }
        )
        return S

    def make_table(self):
        self.table = pl.DataFrame(
            {
                "Students name": self.name,
                "Id": self.id,
                "Date of birth": self.dob
            },
            schema={
                "Students name": pl.Utf8,
                "Id": pl.Utf8,
                "Date of birth": pl.Utf8
            }
        )

    def display(self):
        print(self.table)


class Course(Base):
    """
    Attribute:
        - `_name`: `list[str]`
        - `_id`: `list[str]`
        - `__credit`: `list[int]`
        - `_num_element`: `int`
        - `_table`: `pl.DataFrame`

    Method:
        - `__init__(self, name, id, dob,  number)` -> `None`
        - `init_table(self)` -> `pl.DataFrame`
        - `set_number(cls)` -> `int`
        - `add_element(cls, num_elements)` -> `(list[str], list[str], list[str])`
        - `get_data(cls)` -> `__init__`
        - `make_table` -> `None`
        - `display` -> `None`
    """

    @ property
    def credit(self):
        return self.__credit

    @property
    def table(self) -> pl.DataFrame:
        return self._table

    @ credit.setter
    def credit(self, input_credit):
        self.__credit = input_credit

    @table.setter
    def table(self, input_table):
        self._table = input_table

    def __init__(self, name, id, credit, number):
        self.name: list[str] = name
        self.id: list[str] = id
        self.credit: list[int] = credit
        self.num_elements: int = number

    # @ classmethod
    # def init_table(self):
    #     self._table: pl.DataFrame = pl.DataFrame(
    #         {
    #             "Courses name": [],
    #             "Id": [],
    #             "Credits": []
    #         },
    #         schema={
    #             "Courses name": pl.Utf8,
    #             "Id": pl.Utf8,
    #             "Credits": pl.Int8
    #         }
    #     )

    @ classmethod
    def set_number(cls):
        while True:
            number = input("Enter the number of courses: ")
            if validate_number(number):
                return int(number)
                break
            else:
                print(
                    f"\"{number}\" is not a valid number. Must be a number and at least 1.\n")

    @classmethod
    def add_element(cls, number):
        input_name, input_id, input_credit = [], [], []
        for i in range(number):
            print(f"Course {i+1}: ")
            input_name.append(input("Enter the name: ").capitalize())
            input_id.append(input("Enter the id: ").capitalize())
            while True:
                credit = input("Enter the credits of the course: ")
                if validate_number(credit):
                    input_credit.append(int(credit))
                    break
                else:
                    print(
                        f"\"{credit}\" is not a valid value. Must be an integer at least 1")
        return (input_name, input_id, input_credit)

    @ classmethod
    def get_data(cls):
        number = cls.set_number()
        name, id, credit = Course.add_element(number)
        C = Course(name, id, credit, number)
        C.table = pl.DataFrame(
            {
                "Courses name": C.name,
                "Id": C.id,
                "Credits": C.credit
            },
            schema={
                "Courses name": pl.Utf8,
                "Id": pl.Utf8,
                "Credits": pl.Int8
            }
        )
        return C

    def make_table(self):
        self.table = pl.DataFrame(
            {
                "Courses name": self.name,
                "Id": self.id,
                "Credits": self.credit
            },
            schema={
                "Courses name": pl.Utf8,
                "Id": pl.Utf8,
                "Credits": pl.Int8
            }
        )

    def display(self):
        return print(self.table)


class Mark(pl.DataFrame):
    """
    Attribute:
        - __mark:  dict[str:list[float]]
        - _table: pl.DataFrame

    Method:
        - `init_table(cls)` -> `pl.DataFrame`
        - `add_mark(self, courses: Course, students: Student)` -> `pl.DataFrame`

            Add mark for 1 subject for all students
        - `add_student_index(self, student_list)` -> None

            Add all name of student for `_table
        - ` cal_gpa((self, s: Student, c: Course))
    """

    @ property
    def table(self) -> pl.DataFrame:
        return self._table

    @table.setter
    def table(self, input_table):
        self._table = input_table

    def __init__(self):
        self._table: pl.DataFrame = pl.DataFrame(
            {
                "Students name": []
            },
            schema={
                "Students name": pl.Utf8
            }
        )

    def add_mark(self, courses: Course, students: Student):
        # Enter course
        while True:
            mark_course = input("Enter the course to give mark: ").capitalize()
            if (mark_course in courses.table["Courses name"].to_list()):
                break
            print(f"{mark_course} is not an available course\n")
        mark_list = []
        for x in students.table["Students name"].to_list():
            # Get grades
            while True:
                student_grade = input(f"Enter the mark for {x}: ")
                if validate_mark(student_grade):
                    mark_list.append(round(float(student_grade), 1))
                    break
                else:
                    print(
                        f"\"{student_grade}\" is not a valid value. Must be a number between 0 and 10.\n")
        self.table = self.table.with_columns(
            pl.Series(mark_course, mark_list)
        )

    def add_student_index(self, student_list):
        self.table = pl.DataFrame(
            {
                "Students name": student_list
            }
        )

    def cal_gpa(self, s: Student, c: Course):
        mark = []
        credit = []
        while True:
            student_name = input(
                "Enter the name of the student to see GPA: ").title()
            # get the row of that student for all mark
            if (student_name in s.table["Students name"].to_list()):
                student_mark = self.table.filter(
                    self.table["Students name"] == student_name)
                print(student_mark)
                break
            else:
                print(
                    f"\"{student_name}\" is not in the student list, please try again.")
        # get credit for the marked subjects
        filter_mask = c.table.select(
            pl.col("Courses name").is_in(self.table.columns)
        )[:, 0]
        name_credit = c.table.filter(filter_mask)
        for x in name_credit["Courses name"].to_list():
            mark.append(student_mark[x].item())
            credit.append(
                name_credit.filter(
                    name_credit["Courses name"] == x
                )["Credits"].item()
            )
        print(f"GPA of {student_name} is {np.average(mark, weights=credit):.2f}")

    def display(self):
        print(self.table)


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


def main():
    marks_df = Mark()

    while True:
        choice = input(
            "What do you want to do. Input data(I/i), List data(L/l) or exit(E/e): ").lower()
        if choice == "i":
            while True:
                choice = input(
                    "\nDo you want to input student(S/s), course(C/c) or mark(M/m) data: ").lower()
                if choice == "s":
                    students_df = Student.get_data()
                    # num_student = students_df.num_elements
                    # students_df.make_table()
                    marks_df.add_student_index(
                        students_df.table["Students name"].to_list())
                    break
                elif choice == "c":
                    courses_df = Course.get_data()
                    # num_courses = courses_df._num_elements
                    # courses_df.make_table()
                    break
                elif choice == "m":
                    try:
                        if (students_df.num_elements*courses_df.num_elements != 0):
                            marks_df.add_mark(courses_df, students_df)
                    except NameError:
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
                    try:
                        students_df.display()
                    except:
                        print("There is no data for student to display.\n")
                    break
                elif choice == "c":
                    try:
                        courses_df.display()
                    except:
                        print("There is no data for course to display.\n")
                    break
                elif choice == "m":
                    try:
                        if (students_df.num_elements*courses_df.num_elements != 0) and (marks_df.table.shape[1] > 1):
                            print(marks_df.table)
                        else:
                            print(
                                "There is no data for mark yet, can't list marks now.\n")
                    except NameError:
                        traceback.print_exc()
                        print(
                            "There is no data for student or course now, please try again.\n")
                    break
                elif choice == "g":
                    try:
                        if (students_df.num_elements*courses_df.num_elements != 0) and (marks_df.table.shape[1] > 1):
                            marks_df.cal_gpa(students_df, courses_df)
                        else:
                            print(
                                "There is no data for mark yet, can't list marks now.\n")
                    except NameError:
                        print(
                            "There is no data for student or course now, please try again.\n")
                    break
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
