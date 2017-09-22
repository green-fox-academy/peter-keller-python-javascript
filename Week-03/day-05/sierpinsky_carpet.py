from tkinter import *
import random
import time
root = Tk()

canvas = Canvas(root, width='600', height='600')
canvas.pack()

def carpet(a, x, y):
    time.sleep(0.0001)
    canvas.update()
    color_scale =["red", "blue", "grey", "orange", "yellow", "green", "pink", "lime green", "olive drab", "light sea green", "purple", "cyan", "magenta" ]
    if a < 5:
        return 0
    else: 
        rectangle = canvas.create_rectangle(x+a/3, y+a/3, x+a/3*2, y+a/3*2, fill = random.choice(color_scale))
        
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