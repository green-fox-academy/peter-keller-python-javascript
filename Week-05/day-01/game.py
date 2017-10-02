from tkinter import *
from PIL import Image, ImageTk
from thingy import Map


size = 720
root = Tk()
map = Map()
image1 = PhotoImage(file = 'floor.png')
image2 = PhotoImage(file = 'wall.Png')

root.configure(background ='black')
canvas = Canvas(root, width=size, height=size,bg="white",bd=0)
canvas.pack()


for y in range(len(map.map)):
    for x in range(len(map.map)):
        if map.map[y][x] == 0:
            canvas.create_image(x*72, y*72, anchor = NW, image = image1)
        elif map.map[y][x] == 1:
            canvas.create_image(x*72, y*72, anchor = NW, image = image2)
        

canvas.pack()

# Select the canvas to be in focused so it actually recieves the key hittings
canvas.focus_set()

root.mainloop()