# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

file_to_read = "day-01/single-chars.txt"


def count_lines():
    lines = 0
    try:
        with open(file_to_read, 'r') as file:
            for line in file:
                if len(line) >= 2:
                    lines += 1
            return lines
    except FileNotFoundError:
        return 0

print(count_lines())
