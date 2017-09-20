from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

def horizontal_line(x_coordinate, y_coordinate):
    x_coordinate_extended = x_coordinate + 50
    complete_line = canvas.create_line(x_coordinate, y_coordinate, x_coordinate_extended, y_coordinate, fill="red")
    
horizontal_line(47,140)
horizontal_line(175,53)
horizontal_line(150,120)

root.mainloop()
