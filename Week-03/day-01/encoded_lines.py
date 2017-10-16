# Create a method that decrypts encoded-lines.txt


def decrypt(file_name):
    text = ""
    try:
        source = open(file_name, "r")
        lines = source.readlines()
        for line in lines:
            for i in range(len(line)-1):
                if line[i] != " ": 
                    text += chr(ord(line[i]) - 1)
                else:
                    text += " "
            text += "\n"
        source.close()
    except IOError:
        print("Unable to read the file: ", file_name)
    try:
        destination = open("decoded.txt", "w")
        destination.write(text)
        destination.close()
    except IOError:
        print("Unable to write files to this location")
def main():
    decrypt("encoded_lines.txt")
main()
