from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.
green_rectangle = canvas.create_rectangle(0, 20, 150, 150, fill='green')
red_rectangle = canvas.create_rectangle(150, 0, 210, 300, fill='red')
yellow_rectangle = canvas.create_rectangle(0, 150, 150, 300, fill='yellow')
blue_rectangle = canvas.create_rectangle(100, 150, 180, 300, fill='blue')

root.mainloop()