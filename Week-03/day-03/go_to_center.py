
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.
#given_x_coordinate = 100
#given_y_coordinate = 0

def draw_center(x_coordinate, y_coordinate):
    line_to_center = canvas.create_line(x_coordinate, y_coordinate, 150, 150, fill="red")

draw_center(0,0)
draw_center(300,0)
draw_center(150,300)

root.mainloop()