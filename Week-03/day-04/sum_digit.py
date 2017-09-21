# Given a non-negative int n, return the sum of its digits recursively (no loops). 
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while 
# divide (/) by 10 removes the rightmost digit (126 // 10 is 12).


def sum_of_digits(number):
    if number == 0:
        return 0
    else:
        remaining = number % 10
        summ = remaining + sum_of_digits(number // 10)
        return summ

summ = sum_of_digits(172)
print(summ)