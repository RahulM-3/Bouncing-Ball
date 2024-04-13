import tkinter

# Window setup
win = tkinter.Tk()
win.title("Bouncing Ball")
win.geometry("450x400")

# X and Y axis
canvas = tkinter.Canvas(win, width=450, height=400)
canvas.pack()
canvas.create_line(225, 0, 225, 400)
canvas.create_line(0, 200, 450, 200)

radius = 150 #set the arc radius
canvas_middle = [int(canvas['width'])/2, int(canvas['height'])/2] #find the middle of the canvas
canvas.create_oval(canvas_middle[0] - radius, canvas_middle[1] - radius, canvas_middle[0] + radius, canvas_middle[1] + radius, width = 3)

ballradius = 20
canvas.create_oval
canvas.create_oval(canvas_middle[0] - ballradius, canvas_middle[1] - ballradius, canvas_middle[0] + ballradius, canvas_middle[1] + ballradius, fill="blue")

# application loop
win.mainloop()