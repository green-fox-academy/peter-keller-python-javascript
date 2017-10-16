from tkinter import *
import time
root = Tk()

canvas = Canvas(root, width='500', height='500', bg="yellow")
canvas.pack()

def stripes(a, x, y):
    time.sleep(0.01)
    canvas.update()
    if a < 5:
        return 0
    else: 
        lines = canvas.create_line(x+a/3, y, x+a/3, y+a, fill="black")
        lines = canvas.create_line(x+a/3*2, y, x+a/3*2, y+a, fill="black")
        lines = canvas.create_line(x, y+a/3, x+a, y+a/3, fill="black")
        lines = canvas.create_line(x, y+a/3*2, x+a, y+a/3*2, fill="black")
        stripes(a/3, x+a/3, y), stripes(a/3, x+a/3*2, y+a/3), stripes(a/3, x+a/3, y+a/3*2), stripes(a/3, x, y+a/3)
stripes(500, 0, 0)

root.mainloop()