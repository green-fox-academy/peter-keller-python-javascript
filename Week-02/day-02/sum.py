# - Write a function called `sum` that sum all the numbers
#   until the given parameter
n = int(input("Please insert a number"))

def sum(num):
    for i in range(1, num):
        print(i)

sum(n)