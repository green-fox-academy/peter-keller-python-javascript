from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]
def line_to_center(x, y,a,b, color):
    line = canvas.create_line(x, y, a, b, fill=color)

i = 0
while(i <= 150):
    line_to_center(i, 150, 150, 150 - i, "green")
    i += 10

i = 0
while(i <= 150):
    line_to_center(150 + i, 150, 150, i, "green")
    i += 10
i = 0
while(i <= 150):
    line_to_center(i, 150, 150, 150 + i, "green")
    i += 10

i = 0
while(i <= 150):
    line_to_center(150 + i, 150, 150, 300 - i, "green")
    i += 10



root.mainloop()