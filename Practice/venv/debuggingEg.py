print("This is example file for debugging script")
import pdb
import time
import timeit


x = [1,2,3]
y = 2
z = 3

result = y+z


def func_1(n):
    return [str(num) for num in range(n)]

func_1(10)
