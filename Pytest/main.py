# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Functions import mathFunc
from Functions import test_mathFunc


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# ---------------------------------------
# Execution Script


my_sum = mathFunc.add_two_num(8, 2)
print(my_sum)

my_mul = mathFunc.mul_two_num(25, 2)
print(my_mul)

my_stringAdd = mathFunc.add_string("Hello", "World")
print(my_stringAdd)

my_stringMul = mathFunc.mul_string("Hello", 3)
print(my_stringMul)
