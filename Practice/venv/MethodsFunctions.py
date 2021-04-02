print('This is Methods and Functions File')
import math


def return_even_list(list):

    even_list = []

    for num in list:
        if num%2==0:
            even_list.append(num)
        else:
            pass

    return even_list


list1 = [1,11,111,1111]
even_numbers = return_even_list(list1)
print(even_numbers)

# ----------------------------------------------------
def employee_of_month(list_data):
    work_hour = 0
    name_employee = ""

    for employee,hour in list_data:
        if hour > work_hour:
            work_hour = hour
            name_employee = employee
        else:
            pass

    return (name_employee,work_hour)


hour_list = [("Abby",80),("Jolie",55),("Bob",87)]
print(employee_of_month(hour_list))

# ----------------------------------------------------

def best_number(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)

print(best_number(4,5))

# ----------------------------------------------------

def word_check(string1,string2):
    if string1[0] == string2[0]:
        return True
    else:
        return False

print(word_check("Dog","Dracula"))

# ----------------------------------------------------

def within_ten(n):
    if (n >= 90 and n <= 110) or (n >= 190 and n<= 210):
        return True
    else:
        return False

print(within_ten(205))

# ----------------------------------------------------

def reverse_name(string):
    listName = string.split()
    reversed_listName = listName[::-1]
    return ' '.join(reversed_listName)

print(reverse_name("I am Home"))

# ----------------------------------------------------

def find_33(n):
    for i in range(0,len(n)):
        if n[i] == 3 and n[i + 1] == 3:
            return True

    return False

arr = [1,3,3,3]
print(find_33(arr))

# ----------------------------------------------------

def paper_doll(string):
    result = ""
    for char in string:
        result = result + char*3
    return result


stringEnter = "Doll"
print(paper_doll(stringEnter))

# ----------------------------------------------------

def blackjack(a,b,c):

    sum3 = sum([a,b,c])

    if sum3 <= 21:
        return sum3

    if sum3 > 21 and (a == 11 or b == 11 or c == 11):
        return sum3 - 10

    if sum3 > 21:
        return "BUST"

print(blackjack(9,9,9))

# ----------------------------------------------------

def spy_game(enterList):
    checkList = []
    for num in enterList:
        if num == 0 or num == 7:
            checkList.append(num)


    if checkList == [0,0,7]:
        return True
    else:
        return False

print(spy_game([1,7,2,0,4,5,0]))

# ----------------------------------------------------

def count_prime(num):
    numL = range(1,num + 1)
    num_list = []
    for i in numL:
        if i%1 == 0 and i%i == 0 and i >= 2:
            num_list.append(i)
        else:
            pass

    return num_list

print(count_prime(5))

# ----------------------------------------------------

def vol_sphere(r):
    vol = (4/3)*math.pi*(r**3)
    return vol

print(vol_sphere(2))

# ----------------------------------------------------

def range_check(num,high,low):
    if num >= low and num <= high:
        return True
    else:
        return False

print(range_check(5,7,2))

# ----------------------------------------------------

def upper_lower(string):
    count = 0
    for alp in string:
        if alp.isupper():
            count = count+1
        else:
            count = count

    return count

print(upper_lower("This Man Is Awesome"))

# ----------------------------------------------------

def unique_identifier(list):
    checkList = set(list)
    uniqueList = []
    for item in checkList:
        uniqueList.append(item)

    return uniqueList

print(unique_identifier([1,1,1,1,2,2,2,3,3,4,5]))

# ----------------------------------------------------

def multiply_number(list):
    mul = 1
    listLen = range(1,len(list)+1)
    for item in list:
        mul = mul * item
    return mul

print(multiply_number([1,2,3,4,5,6]))

# ----------------------------------------------------

def palindrome(string):
    string = string.replace(" ","")
    reverseString =  string[::-1]

    if string == reverseString:
        status = True
    else:
        status = False

    return (status,reverseString)

status,reverseString = palindrome("nurses run")
print(status,reverseString)

# ----------------------------------------------------







