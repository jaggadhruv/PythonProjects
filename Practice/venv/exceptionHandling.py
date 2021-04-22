print("This script is exception handling script")


def ask_for_int():

    while True:
        try:
            result = int(input("Please enter a number: "))
        except:
            print("The number entered is not an integer")
            continue
        else:
            print("Thank You")
            break
        finally:
            print("End of Run")


def square_string():

    try:
        # for i in ["a","b","c"]:
        #     print(i**2)

        for i in [1,2,3]:
            print(i**2)
    except:
        print("The square of string is not possible")
    finally:
        print("End Run")


def zero_division():
    try:
        x = 5
        y = 1
        result = x/y
    except ZeroDivisionError:
        print("Math Error: Zero Division")
    else:
        print("You have it")
    finally:
        print("All Done")


def ask():

    while True:
        try:
            input_rec = int(input("Please enter an Integer value: "))
            result = input_rec**2
            print(result)
        except:
            print("The number entered is not Integer")
            continue
        else:
            print("Thanks you for response")
            break
        finally:
            print("All checks Done")


def ask1():
    waiting = True

    while waiting:
        try:
            input_rec = int(input("Please enter an Integer value: "))
        except:
            print("The number entered is not Integer")
            continue
        else:
            waiting = False
        finally:
            print("All checks Done")

    result = input_rec ** 2
    print(f"The square of the entered value is {result}")
# -------------------------------------------

# square_string()
# zero_division()
ask1()