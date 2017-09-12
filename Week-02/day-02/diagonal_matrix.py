# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output
line = ""
for i in range(0,4):
    line=""
    for j in range(0,4):
        if i == j:
            line += "1"
        else:
             line +="0"
        line+=" "
    print(line)