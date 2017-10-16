from tkinter import *
import random
import time

root = Tk()
DIMENSION = 400
canvas = Canvas(root, width=str(DIMENSION), height=str(DIMENSION))
canvas.pack()

def random_color():
  randomness_seed = lambda: random.randint(0,255)
  return '#%02X%02X%02X' % (randomness_seed(),randomness_seed(),randomness_seed())

def draw_carpet(x, y, a):
    if a < 5:
        return 0
    #time.sleep(0.0001)
    #canvas.update()

    canvas.create_rectangle(x+a/3, y+a/3, x+a/3*2, y+a/3*2, fill = random_color())
        
    draw_carpet(x, y, a/3)
    draw_carpet(x+a/3, y, a/3)
    draw_carpet(x+a/3*2, y, a/3)

    draw_carpet(x, y+a/3, a/3)
    draw_carpet(x+a/3*2, y+a/3, a/3)

    draw_carpet(x, y+a/3*2, a/3)
    draw_carpet(x+a/3, y+a/3*2, a/3)
    draw_carpet(x+a/3*2, y+a/3*2, a/3)
        

draw_carpet(0, 0, DIMENSION)

root.mainloop()