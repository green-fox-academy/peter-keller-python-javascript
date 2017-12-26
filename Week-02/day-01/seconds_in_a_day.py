current_hours = 14
current_minutes = 34
current_seconds = 42

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented bt the variables
secondsaday = 60 * 60 * 24

currenthour = 14 * 60 * 60
currentminute = 34 * 60

currenttime = currenthour + currentminute + current_seconds
remaining = (secondsaday - currenttime)
print(remaining)
