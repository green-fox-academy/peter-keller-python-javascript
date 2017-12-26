# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the summ and average of these
# integers like:
#
# summ: 22, Average: 4.4
number = int(input("Amount of numbers: "))
summ = 0
for i in range (0, number):
    summ += int(input("Number: "))
print("summ: " + str(summ) +  " , Average: " + str(summ / number))
