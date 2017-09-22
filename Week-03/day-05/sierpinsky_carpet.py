from tkinter import *
import random
import time
root = Tk()

canvas = Canvas(root, width='600', height='600')
canvas.pack()

def carpet(x, y, a):
    time.sleep(0.0001)
    canvas.update()
    
    if a < 0:
        return
    else: 
        r = lambda: random.randint(0,255)
        random_color = '#%02X%02X%02X' % (r(),r(),r())
        rectangle = canvas.create_rectangle(x+a/3, y+a/3, x+a/3*2, y+a/3*2, fill = random_color)
        
        carpet(x, y, a/3)
        carpet(x+a/3, y, a/3)
        carpet(x+a/3*2, y, a/3)

        carpet(x, y+a/3, a/3)
        carpet(x+a/3*2, y+a/3, a/3)

        carpet(x, y+a/3*2, a/3)
        carpet(x+a/3, y+a/3*2, a/3)
        carpet(x+a/3*2, y+a/3*2, a/3)
        

carpet(0, 0, 600)

root.mainloop()