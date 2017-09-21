# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def star_adder(word):
    if word == "":
        return ""
    else:
        if len(word) == 1:
            return  word[0] + star_adder(word[1:])
        else: 
            return word[0] + "*" + star_adder(word[1:])


print(star_adder("Stars and stuff"))