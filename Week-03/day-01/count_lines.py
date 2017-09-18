# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.
def count_lines():
    try:
        f = open("my-file.txt", "r")
        num_lines = sum(1 for line in open('my-file.txt'))
        print(num_lines)
    except FileNotFoundError:
        print("Unable to read file: my-file.txt")

count_lines()

