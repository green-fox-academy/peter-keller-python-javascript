from tkinter import *
import math
root = Tk()

canvas = Canvas(root, width='820', height='800', )
canvas.pack()



def hexagon_fractal(a, x, y):
    height = math.sqrt(3) / 2 * a
    canvas.create_polygon(x, y, x + a / 2, y - height,
                          x + a * 1.5, y - height,
                          x + a * 2, y,
                          x + a * 1.5, y + height,
                          x + a / 2, y + height,
                          fill="", outline = "black" )
                          
def draw_hexagon(a, x, y,):
    if a < 5:
        return 
    else:
        hexagon_fractal(x, y, a)

        draw_hexagon(x, y, a / 2)
        draw_hexagon(x, y, a / 2)
        draw_hexagon(x, y, a / 2)
        
hexagon_fractal(400, 10, 400)

root.mainloop()