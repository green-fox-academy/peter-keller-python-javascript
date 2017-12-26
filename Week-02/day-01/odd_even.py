# Write a program that reads a number form the standard input,
# Than prints "Odd" if the number is odd, or "Even" it it is even.

number = int(input("Odd or even? Let's find out! "))
if number % 2 == 0:
    print("even")
else:
    print("odd")
