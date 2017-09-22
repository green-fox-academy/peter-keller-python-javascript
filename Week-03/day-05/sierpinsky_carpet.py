from tkinter import *
import time
root = Tk()

canvas = Canvas(root, width='600', height='600')
canvas.pack()

def carpet(a, x, y):
    time.sleep(0.0001)
    canvas.update()
    if a < 5:
        return 0
    else: 
        rectangle = canvas.create_rectangle(x+a/3, y+a/3, x+a/3*2, y+a/3*2, fill="black")

        carpet(a/3, x, y)
        carpet(a/3, x+a/3, y)
        carpet(a/3, x+a/3*2, y)

        carpet(a/3, x, y+a/3)
        carpet(a/3, x+a/3*2, y+a/3)

        carpet(a/3, x, y+a/3*2)
        carpet(a/3, x+a/3, y+a/3*2)
        carpet(a/3, x+a/3*2, y+a/3*2)
        

carpet(600, 0, 0)

root.mainloop()