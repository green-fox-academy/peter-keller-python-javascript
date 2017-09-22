from tkinter import *
import time
root = Tk()

canvas = Canvas(root, width='600', height='600')
canvas.pack()

def carpet(a, x, y):
    time.sleep(0.0001)
    canvas.update()

    if a < 40:
        return 0
    else: 
        rectangle = canvas.create_rectangle(x+a/4, y+a/4, x+a/4*3, y+a/4*3, fill="", width=a/20)
        
        carpet(a/2, x, y)
        carpet(a/2, x+a/4*2, y)
        carpet(a/2, x, y+a/4*2)
        carpet(a/2,x+a/4*2,y+a/4*2)


carpet(600, 0, 0)

root.mainloop()