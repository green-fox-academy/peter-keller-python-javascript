# - Create a function called `factorio`
#   that returns it's input's factorial
n = int(input("Insert number: "))


def factorio(num):
    g = 1
    for i in range(1, (num + 1)):
        g = g * i
    print("Factorio: ", g)


factorio(n)


def recursive_factorio(number):
    if number == 1:
        return 1
    else:
        return number * recursive_factorio(number - 1)


print(recursive_factorio(5))
