# Create a method that decrypts reversed-order.txt

#file_name = "reversed-order.txt"

def decrypt(file_name):
    text = ""
    try:
        source = open(file_name, "r")
        lines = source.readlines()
        for i in range(len(lines)-1, -1, -1):
            text += lines[i]
            if i == len(lines)-1:     
                text += "\n"
        source.close()
    except IOError:
        print("Unable to read the file: ", file_name)
    try:
        destination = open("normal-order.txt", "w")
        destination.write(text)
        destination.close()
    except IOError:
        print("Unable to write files to this location")
def main():
    decrypt("reversed-order.txt")
main()

