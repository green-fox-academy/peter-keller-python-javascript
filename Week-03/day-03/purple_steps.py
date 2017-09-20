from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]

x_coordinate = 0
y_coordinate = 0

def purple_steps(x_coordinate, y_coordinate):
    square = canvas.create_rectangle(x_coordinate, y_coordinate, x_coordinate + 10, y_coordinate + 10, fill="purple")

for i in range(1, 20):
    x_coordinate += 10
    y_coordinate += 10

    purple_steps(x_coordinate, y_coordinate)

root.mainloop()