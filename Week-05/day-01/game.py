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
        
    

class Entity(object):
    def __init__(self):
        self.hero_down = PhotoImage(file = "hero-down.png")
        self.hero_up = PhotoImage(file = "hero-up.png")
        self.hero_left = PhotoImage(file = "hero-left.png")
        self.hero_right = PhotoImage(file = "hero-right.png")
        self.drawing_entity()
        
    def move(self, dx, dy):
        canvas.move(hero.put_entity, dx, dy )
    
    def update_costume(self, costume):
        self.costume = costume
        canvas.itemconfigure(self.put_entity, image=self.costume)

    
    def drawing_entity(self):
        self.put_entity = canvas.create_image(0, 0, anchor = NW, image = self.hero_down)


    def moving(self, e):
        if (e.keysym == 'Up'):
            self.move(0,-72)
            self.update_costume(self.hero_up)
        elif(e.keysym == 'Down'):
            self.move(0,72)
            self.update_costume(self.hero_down)
        elif(e.keysym == 'Left'):
            self.move(-72,0)
            self.update_costume(self.hero_left)
        elif(e.keysym == 'Right'):
            self.move(72,0)
            self.update_costume(self.hero_right)

canvas.pack()

draw_map = DrawMap()
hero = Entity()
root.bind("<KeyPress>", hero.moving)
canvas.focus_set()

root.mainloop()