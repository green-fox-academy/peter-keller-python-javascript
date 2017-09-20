from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# divide the canvas into 4 equal parts
# and repeat this pattern in each quarter:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]
def line_to_center(x, y,a,b, color):
    line = canvas.create_line(x, y, a, b, fill=color)

i = 0
while(i <= 150):
    line_to_center(0, i, i, 150, "green")
    i += 10

i = 0
while(i <= 150):
    line_to_center(150 - i, 0, 150, 150 - i, "purple")
    i += 10

i = 0
while(i <= 150):
    line_to_center(150, i, 150 + i, 150, "green")
    i += 10

i = 0
while(i <= 150):
    line_to_center(150 + i, 0, 300, i, "purple")
    i += 10

i = 0
while(i <= 150):
    line_to_center(0, 150 + i, i, 300 , "green")
    i += 10

i = 0
while(i <= 150):
    line_to_center(i, 150, 150, 150 + i, "purple")
    i += 10

i = 0
while(i <= 150):
    line_to_center(150,150 + i,150 + i, 300, "green")
    i += 10

i = 0
while(i <= 150):
    line_to_center(150 + i, 150, 300, 150 + i, "purple")
    i += 10



root.mainloop()
