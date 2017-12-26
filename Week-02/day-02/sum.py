# - Write a function called `sum` that sum all the numbers
#   until the given parameter
sum_to = int(input("Please insert a number: "))


def sum_numbers(numbers):
    for i in range(1, numbers):
        print(i)


sum_numbers(sum_to)
