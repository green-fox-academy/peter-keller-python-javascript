# Write a program that asks for two numbers and prints the bigger one
number = int(input())
number2 = int(input())
if number > number2:
    print("First number is bigger")
elif number2 > number:
    print("Second number is bigger")
else:
    print("They are equal")