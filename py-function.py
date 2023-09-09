# def say_my_name(name, surname):


#     print("Hello {} {}!".format(name,surname))
# say_my_name(input("Enter your name : "), input("Enter your surname : "))


# def return_my_name():
#     name = input("Enter your name : ")
#     surname = input("Enter your surname : ")
#
#     return "Hello {} {}!".format(name, surname)
#
#
# print(return_my_name())


def max_number(number1, number2, number3):
    if number1 >= number2 and number1 >= number3:
        return number1
    elif number2 >= number1 and number2 >= number3:
        return number2
    else:
        return number3

print(max_number(42,42,4))
