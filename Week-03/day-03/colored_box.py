from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

first_line = canvas.create_line(100, 100, 200, 100, fill="red")
second_line = canvas.create_line(100, 100, 100, 200, fill="yellow")
third_line = canvas.create_line(200, 100, 200, 200, fill="green")
fourth_line = canvas.create_line(100, 200, 200, 200, fill="blue")
# draw a box that has different colored lines on each edge.

root.mainloop()