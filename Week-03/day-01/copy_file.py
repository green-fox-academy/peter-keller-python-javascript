# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

original_file = "day-01/sample.txt"
file_to_copy = "day-01/sample2.txt"


def copy_file():
    flag = True
    try:
        with open(original_file, 'r') as file:
            text = file.read()
        with open(file_to_copy, 'w') as file1:
            file1.write(text)
        print(flag)
    except FileNotFoundError:
        flag = False
        print(flag)


copy_file()
