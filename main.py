import tkinter

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
attitude = canvas_middle
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
    win.after(100, gravity, )

gravity()

# application loop
win.mainloop()