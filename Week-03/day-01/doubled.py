# Create a method that decrypts the duplicated-chars.txt

file_name = "duplicated-chars.txt"


def decrypt(file_name):
    text = ""
    try:
        source = open(file_name, "r")
        lines = source.readlines()
        for line in lines:
            for i in range(0, len(line), 2):
                text += line[i]
        source.close()
    except IOError:
        print("Unable to read the file: ", file_name)
    try:
        destination = open("single-chars.txt", "w")
        destination.write(text)
        destination.close()
    except IOError:
        print("Unable to write files to this location")
def main():
    decrypt("duplicated-chars.txt")
main()

