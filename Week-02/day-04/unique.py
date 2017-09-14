numbers = [1, 11, 34, 11, 52, 61, 1, 34]

def remove_duplicates(x):
    a = []
    for i in numbers:
        if i not in a:
            a.append(i)
    return a

print(remove_duplicates([1,2,2,3,3,4]))