from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps-3d/r4.png]

def purple_steps():
    x_coordinate = 0
    y_coordinate = 0
    size = 10
    for i in range(1, 7):
        x_coordinate_extended = x_coordinate + size
        y_coordinate_extended = y_coordinate + size
        square = canvas.create_rectangle(x_coordinate, y_coordinate, x_coordinate + size, y_coordinate + size, fill="purple")
        size += 10
        x_coordinate = x_coordinate_extended
        y_coordinate = y_coordinate_extended
purple_steps()

root.mainloop()
