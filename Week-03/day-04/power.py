# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def number_power(number, power):
    if number == 0:
        return 0
    elif power == 0:
        return 1
    else:
        return number * number_power(number, power - 1)


print(number_power(3,3))