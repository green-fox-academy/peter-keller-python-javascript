# Create a method that decrypts encoded-lines.txt
file_name_global = 'encoded_lines.txt'

def shift_text_to_right(file_name):
    string = " "  
    try:
        read_in = open(file_name, 'r')
        text = read_in.readlines()
    #print(text)
        for line in text:
            for j in range(len(line)):
                if line[j] != " ":
                    a = chr(ord(line[j])-1)
                #string += chr(a)
                    string + "\n"
                else:
                    string += " "
            string + "\n"
        read_in.close
    except IOError:
        print("fail")
    try:
        write_in = open('encoded_lines_copy_inside.txt', 'w')
        write_in.write(string)
        write_in.close()




    shift_text_to_right(file_name)