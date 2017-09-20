from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]
def line_to_center(x, y,a,b, color):
    line = canvas.create_line(x, y, a, b, fill=color)

i = 0
while(i <= 300):
    line_to_center(0, i, i, 300, "green")
    i += 20

i = 0
while(i <= 300):
    line_to_center(300 - i, 0, 300, 300 - i, "purple")
    i += 20



root.mainloop()