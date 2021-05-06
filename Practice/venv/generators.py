print("This is Generator Script")
import random


def create_cubes(n):
    result = []

    for num in range(n):
        result.append(num**3)
    return result


def create_cube_2(n):

    for num in range(n):
        yield num**3


def number_square(n):

    result = []

    for num in range(n):
        result.append(num**2)

    return result


def number_square_2(n):
    for num in range(n):
        yield num**2


def random_func(low,high,n):
    for num in range(n):
        yield random.randint(low,high)



#
# print(create_cubes(10))
# print(list(create_cube_2(5)))
#
# print(number_square(4))
# print(list(number_square_2(5)))

print(list(random_func(2,12,10)))

