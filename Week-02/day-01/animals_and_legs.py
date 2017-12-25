# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The seconf represents the number of pigs the farmer has
# It should print how many legs all the animals have
chicken = int(input("Number of chickens: "))
pig = int(input("Number of pigs: "))
chicken_legs = chicken * 2
pig_legs = pig * 4
legs = chicken_legs + pig_legs
print(legs)
