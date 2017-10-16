def is_prime(number):
    if number == 1:
        return False
    for divisor in range(2, int(number / 2)):
        if number % divisor == 0:
            return False
    return True