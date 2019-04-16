try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def parabola(x):
    y = x * x / 100
    return y


def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill='black')
    canvas.create_line(0, -y_origin, 0, y_origin, fill='black')


def draw_dot(canvas):
    n = 2
    canvas.update()
    canvas.create_oval(-n, n, n, -n, fill='red')
"""canvas.create_oval(x_origin - n, y_origin - n,
                      x_origin + n, y_origin + n, fill='red'"""


def plot(canvas, x, y):
    canvas.create_line(x, y, x + 1, y + 1, fill='red')


mainWindow = tkinter.Tk()

mainWindow.title('Parabola')
mainWindow.geometry('640x480-10-200')


canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

for x in range(-100, 101):
    y = parabola(x)
    plot(canvas, x, -y)
    #print(y)

draw_axes(canvas)
# draw_dot(canvas)
mainWindow.mainloop()
