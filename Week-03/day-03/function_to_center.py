
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.
x_coordinate = 0
y_coordinate = 0

def line_to_center(x_coordinate, y_coordinate):
    line = canvas.create_line(x_coordinate, y_coordinate, 150, 150, fill="purple")
line_to_center(20, 10)

i = 0
while(i <= 300):
    
    line_to_center(0, i)
    line_to_center(i,0)
    line_to_center(300, i)
    line_to_center(i, 300)
    i += 20

root.mainloop()