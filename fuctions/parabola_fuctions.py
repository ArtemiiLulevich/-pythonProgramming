import math
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def parabola(page, size):
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)


def circle(page, radius, g, h, colour="black"):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=colour, width=1)

    # for x in range(g * 100, (g + radius) * 100):
    #     x /= 100
    #     y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill='black')
    page.create_line(0, -y_origin, 0, y_origin, fill='black')


"""def draw_dot(canvas):
    n = 2
    canvas.update()
    canvas.create_oval(-n, n, n, -n, fill='red')
    canvas.create_oval(x_origin - n, y_origin - n,
                      x_origin + n, y_origin + n, fill='red'"""


def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill='red')


mainWindow = tkinter.Tk()
mainWindow.title('Parabola')
mainWindow.geometry('640x480-10-200')

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axes(canvas)
parabola(canvas, 100)
parabola(canvas, 200)
# parabola(canvas, 300)

circle(canvas, 100, 100, 100, 'red')
circle(canvas, 100, 100, -100)
circle(canvas, 100, -100, 100)
circle(canvas, 100, -100, -100)
# circle(canvas, 10, 30, 30)
# draw_dot(canvas)
mainWindow.mainloop()
