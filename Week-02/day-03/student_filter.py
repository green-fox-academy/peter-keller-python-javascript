

students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints: 
#  - how many candies they have on average

def candies():
    names = []
    for line in students:
        names.append(line['name'])
        if line['candies'] > 4:
            print(line['name'] + " has more than the given amount, he/she has " + str(line['candies']) + " candies")

def average():
    summ = 0
    for line in students:
        summ += line['candies']
    print("Average: " , summ/4)

candies()
average()