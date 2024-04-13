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

# application loop
win.mainloop()