# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4
sum = 0
for i in range(0, 5):
    sum += int(input("number" + str(i+1)+" : "))
print ("sum: " + str(sum) + ", Average: " + str(sum / i-1))

