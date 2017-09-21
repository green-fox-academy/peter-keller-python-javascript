from tkinter import *

root = Tk()

canvas = Canvas(root, width='500', height='500', bg="yellow")
canvas.pack()

def stripes(a, x, y):
    if a < 5:
        return 0
    else: 
        lines = canvas.create_line(x+a/3, y, x+a/3, y+a, fill="black")
        lines = canvas.create_line(x+a/3*2, y, x+a/3*2, y+a, fill="black")
        lines = canvas.create_line(x, y+a/3, x+a, y+a/3, fill="black")
        lines = canvas.create_line(x, y+a/3*2, x+a, y+a/3*2, fill="black")
        return stripes(a/3, x+a/3, y), stripes(a/3, x+a/3*2, y+a/3), stripes(a/3, x+a/3, y+a/3*2), stripes(a/3, x, y+a/3)
stripes(500, 0, 0)

root.mainloop()