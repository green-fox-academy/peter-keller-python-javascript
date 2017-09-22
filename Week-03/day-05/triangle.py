from tkinter import *
import random
import time
root = Tk()

canvas = Canvas(root, width='500', height='500')
canvas.pack()

def stripes(a, x, y):
    time.sleep(0.01)
    canvas.update()
    color_scale =["red", "blue", "grey", "orange", "green", "pink", "lime green", "olive drab", "purple", "magenta" ]
    if a <5:
        return 0
    else: 
        lines = canvas.create_line(x, y, x+a/2, y+a, fill=random.choice(color_scale))
        lines = canvas.create_line(x, y, x+a, y, fill=random.choice(color_scale))
        lines = canvas.create_line(x+a/2, y+a, x+a, y, fill=random.choice(color_scale))
        
        stripes(a/2, x,y)
        stripes(a/2, x+a/4,y+a/2)
        stripes(a/2, x+a/2,y)
        
        
stripes(500, 0, 0)

root.mainloop()