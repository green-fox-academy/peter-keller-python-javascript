# - Create a function called `factorio`
#   that returns it's input's factorial
n = int(input("Insert number: "))


def factorio(num):
    g = 1
    for i in range(1, (num + 1)):
        g = g * i
    print("Factorio: ", g)


factorio(n)
