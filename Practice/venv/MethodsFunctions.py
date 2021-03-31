print('This is Methods and Functions File')

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