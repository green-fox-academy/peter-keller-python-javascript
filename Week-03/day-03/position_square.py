from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

def square_drawer(x_coordinate, y_coordinate):
    x_coordinate_extended = x_coordinate + 50
    y_coordinate_extended = y_coordinate + 50
    complete_line = canvas.create_rectangle(x_coordinate, y_coordinate, x_coordinate_extended, y_coordinate_extended, fill="red")
    
square_drawer(47,140)
square_drawer(175,53)
square_drawer(150,120)

root.mainloop()

root.mainloop()