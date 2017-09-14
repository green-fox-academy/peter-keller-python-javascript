# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4
number = int(input("Amount of numbers: "))
sum = 0
for i in range (0, number):
    sum += int(input("Number: "))
print ("Sum: " + str(sum) +  " , Average: " + str(sum / number))


