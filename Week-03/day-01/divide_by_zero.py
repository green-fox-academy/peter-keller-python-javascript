# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

number = int(input("Please insert a number: "))

def divide_num():
    try:
        result = 10 / number
        print(result)
    except ZeroDivisionError:
        print("Can't divide by zero")

divide_num()

