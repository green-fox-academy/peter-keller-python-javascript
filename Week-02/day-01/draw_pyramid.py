# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was
number = int(input("Insert number: "))
star = "*"
space = " "
m = 0
for n in range (1 + (number+1)):
    if n % 2 == 1 and n != 0:
            print(space*(number//2-m) + star*(n))
            m += 1
