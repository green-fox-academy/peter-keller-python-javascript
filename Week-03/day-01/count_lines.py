# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

file_to_read = "day-01/single-chars.txt"


def count_lines():
    try:
        with open(file_to_read, 'r') as file:
            num_lines = sum(1 for line in file)
        return num_lines
    except FileNotFoundError:
        return "Unable to read file: " + file_to_read


print(count_lines())
