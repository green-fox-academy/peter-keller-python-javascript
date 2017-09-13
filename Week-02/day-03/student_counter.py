students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

# create a function that takes a list of students and prints: 
# - how many candies are owned by students

# create a function that takes a list of students and prints:
# - Sum of the age of people who have lass than 5 candies

def candy():
    candy = 0
    for i in range (0,len(students)):
        print(students[i]['name'] + ":" + str(students[i]['candies']))

candy()

def age(students):
    age_counter = 0
    for student in students:
        if student["candies"] < 5:
            age_counter += student["age"]
    print(age_counter)

age(students)