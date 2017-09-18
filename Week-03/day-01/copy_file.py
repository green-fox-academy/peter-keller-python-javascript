# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

original_file = "sample.txt"
file_to_copy = "sample2.txt"

def copy_file():
    flag = True
    try:
        original_file_open = open(original_file, 'r')
        text = original_file_open.read

        file_to_copy_open = open(file_to_copy, 'w')
        file_to_copy_open.write(text)

        original_file_open.close()
        file_to_copy_open.close()

        print(flag)
    except FileNotFoundError:
        flag = False
        print(flag)

copy_file()