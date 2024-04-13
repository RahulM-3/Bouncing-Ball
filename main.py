import tkinter
import random

# Window setup
win = tkinter.Tk()
win.title("Bouncing Ball")
win.geometry("450x400")

# Canvas
canvas = tkinter.Canvas(win, width=450, height=400)
canvas.pack()
#find the middle of the canvas
canvas_middle = [int(canvas['width'])/2, int(canvas['height'])/2]

# X and Y axis
canvas.create_line(225, 0, 225, 400)
canvas.create_line(0, 200, 450, 200)

# Outer Boundary
radius = 150
canvas.create_oval(canvas_middle[0] - radius, canvas_middle[1] - radius, canvas_middle[0] + radius, canvas_middle[1] + radius, width=3)

# Ball
attitude = [int(canvas['width'])/2, int(canvas['height'])/2]
ballradius = 20
x0 = attitude[0]-ballradius
y0 = attitude[1]-ballradius
x1 = attitude[0]+ballradius
y1 = attitude[1]+ballradius
ball = canvas.create_oval(x0, y0, x1, y1, fill="blue")

# Gravity
def gravity():
    attitude[1] += 9.807
    x0 = attitude[0]-ballradius
    y0 = attitude[1]-ballradius
    x1 = attitude[0]+ballradius
    y1 = attitude[1]+ballradius
    canvas.coords(ball, x0, y0, x1, y1)
    win.after(100, gravity)

def collision():
    ballcoords = canvas.coords(ball)
    #print("center", canvas_middle)
    #print("ballcoords", ballcoords, "\n")
    if (abs(ballcoords[3]-canvas_middle[1]) >= 147):
        print("Collided")
        attitude[1] -= 100
        if(random.randint(0, 2)):
            attitude[0] += 100
        else:
            attitude[0] -= 100
    win.after(100,collision)

collision()
gravity()

# application loop
win.mainloop()