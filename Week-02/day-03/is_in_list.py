# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
needed_numbers = [4, 8, 12, 12452436]
result = []

def check(numbers):
    for i in range(len(needed_numbers)):
        result.append(False)
    i = 0
    for num1 in needed_numbers:
        for num2 in list_of_numbers:
            if num1 == num2:
                result[i] = True
        i += 1
    for answer in result:
        if answer == False:
            return False
        return True
    
print(check(list_of_numbers))

