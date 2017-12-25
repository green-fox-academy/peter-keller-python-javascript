# Crate a program that draws a chess table like this
#
# % % % % 
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % % 
#  % % % %
#
character = ""
for i in range(0, 8):
    for j in range(0, 8):
        if i % 2 == 0:
            if j % 2 == 0:
                character += "%"
            else:
                character += " "
        else:
            if j % 2 == 0:
                character += " "
            else:
                character += "%"
    print (character + "\n")
    character = ""