from tkinter import *
from PIL import Image, ImageTk
from map_file import Map


root = Tk()
size = 720
map = Map()
root.configure(background ='black')
canvas = Canvas(root, width=size, height=size,bg="white",bd=0)
canvas.pack()
class DrawMap():
    def __init__(self):
        self.image1 = PhotoImage(file = 'floor.png')
        self.image2 = PhotoImage(file = 'wall.Png')
        self.draw_map()
        
    def draw_map(self):
        for y in range(len(map.map)):
            for x in range(len(map.map)):
                if map.map[y][x] == 0:
                    canvas.create_image(x*72, y*72, anchor = NW, image = self.image1)
                elif map.map[y][x] == 1:
                    canvas.create_image(x*72, y*72, anchor = NW, image = self.image2)
        
class DrawEntity:
    def __init__(self):
        self.hero = PhotoImage(file = "hero-down.png")
        self.drawing_entity()
    
    def drawing_entity(self):
        canvas.create_image(0, 0, anchor = NW, image = self.hero)

    
canvas.pack()

draw_map = DrawMap()
drawing_entity = DrawEntity()
canvas.focus_set()

root.mainloop()