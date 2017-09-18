# Open a file called "my-file.txt"
# Write your name in it as a single line
# If the program is unable to write the file,
# then it should print an error message like: "Unable to write file: my-file.txt"


def my_name():
    try:
        filesource = open("my-file.txt", "w")
        filesource.write ("Peter Keller")
        filesource.close
    except FileNotFoundError:
        print("Unable to write file: my-file.txt")

my_name()