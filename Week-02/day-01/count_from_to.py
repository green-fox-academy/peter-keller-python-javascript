# Create a program that asks for two numbers
# If the second number is not bigger than the first one it should print:
# "The second number should be bigger"
#
# If it is bigger it should count from the first number to the second by one
# 
# example:
#
# first number: 3, second number: 6, should print:
#
# 3
# 4
# 5
starting_number = int(input("Starting number: "))
ending_number = int(input("Last number: "))
if ending_number <= starting_number:
    print("The second number should be bigger")
else:
    for i in range(starting_number, ending_number + 1):
        print(i)
