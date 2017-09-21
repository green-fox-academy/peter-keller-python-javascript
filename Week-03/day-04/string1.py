# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def letter_changer(word):
    if word == "":
        return ""
    else:
        if word[0] == "x":
            return  "y" + letter_changer(word[1:])
        else: 
            return word[0] + letter_changer(word[1:])


print(letter_changer("xander"))