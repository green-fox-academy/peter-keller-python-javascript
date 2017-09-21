
# Write a recursive function that takes one parameter: n and counts down from n.

def countdown(number):
    if number == 0:
        print(number)
    else:
        print(number)
        countdown(number - 1)

user_input = int(input("Number to count down from: "))
countdown_of_user_input = countdown(user_input)
