from tkinter import *
import random
import time

root = Tk()
CANVAS_DIMENSTION = 600
canvas = Canvas(root, width=str(CANVAS_DIMENSTION), height=str(CANVAS_DIMENSTION))
canvas.pack()

def random_color():
  randomness_seed = lambda: random.randint(0,255)
  return '#%02X%02X%02X' % (randomness_seed(),randomness_seed(),randomness_seed())

def frange(start, end, jump):
  while start < end:
    yield start
    start += jump

def draw_square(x, y, dimension):
  canvas.create_rectangle(x, y, x + dimension, y + dimension, fill = random_color())

def is_center_tile(x, y, x_offset, y_offset, tile_dimension):
  return x == x_offset + tile_dimension and y == y_offset + tile_dimension

def draw_carpet(x_offset, y_offset, carpet_dimension):
    if carpet_dimension < 5:
        return 0
    time.sleep(0.0001)
    canvas.update()
    
    tile_dimension = carpet_dimension / 3
    for x in frange(x_offset, x_offset + carpet_dimension, tile_dimension):
        for y in frange(y_offset, y_offset + carpet_dimension, tile_dimension):
            if is_center_tile(x, y, x_offset, y_offset, tile_dimension):
                draw_square(x, y, tile_dimension)
            else:
                draw_carpet(x, y, tile_dimension)
        
draw_carpet(0, 0, CANVAS_DIMENSTION)

root.mainloop()