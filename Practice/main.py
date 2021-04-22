# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import dataStructure
import Statements
import MethodsFunctions
import oopPractice
import polymorphism
import specialMethods
import OOPPractice1
from OOPPractice2 import BankAccount
import exceptionHandling
import cap
import test_cap


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# ------------------------------------------------------------
my_account1 = BankAccount("Jose", 100)
print(my_account1)

my_account1.deposit(50)
my_account1.withdraw(75)

my_account1.withdraw(500)