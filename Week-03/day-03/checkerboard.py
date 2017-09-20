from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# fill the canvas with a checkerboard pattern.

def checkerboard(square):
    for i in range(0,int(300/square)):
        for j in range(0,int(300/square)):
            if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                teal_line = canvas.create_rectangle(square*i, square*j, square*(i+1), square*(j+1), fill="black")


checkerboard(37.5)
root.mainloop()