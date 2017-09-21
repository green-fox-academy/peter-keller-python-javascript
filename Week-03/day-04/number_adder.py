# Write a recursive function that takes one parameter: n and counts down from n.


def number_adder(number):
    if number == 0:
        return 0
    else: 
        return number + number_adder(number - 1)

print(number_adder(5))