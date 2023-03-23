from test_code import *

# def validate_number(x: int):
#     try:
#         return (int(str(x)) >= 1)
#     except ValueError:
#         return False

# def get_num_student():
#     while True:
#         x = input("Enter the number of student: ")
#         if validate_number(x):
#             return x
#         print(f"\"{x}\" must be an integer and at least 1.\n")

x = get_num("student")

print(x)
    