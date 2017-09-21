# Given a string, compute recursively a new string where all the 'x' chars have been removed.


def letter_changer(word):
    if word == "":
        return ""
    else:
        if word[0] == "x":
            return  "" + letter_changer(word[1:])
        else: 
            return word[0] + letter_changer(word[1:])


print(letter_changer("xTxhxexrxex xaxrxex xnxox xXx xlxextxtxexrxsx xixnx xtxhxixsx xsxexnxtxexnxcxex"))