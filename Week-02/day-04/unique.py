numbers = [1, 11, 34, 11, 52, 61, 1, 34]


def remove_duplicates():
    a = []
    for i in numbers:
        if i not in a:
            a.append(i)
    return a


print(remove_duplicates())
