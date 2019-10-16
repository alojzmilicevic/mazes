from tkinter import *
import time

width = 1024
height = 1024

tk = Tk()
canvas = Canvas(tk, width=width, height=height)
canvas.pack()

points = [(1, 0), (1, 3), (0, 3), (3, 2), (3, 3)]
cell_size = 32

for i in range(1, len(points)):
    x0 = points[i - 1][0] * cell_size
    y0 = points[i - 1][1] * cell_size

    x1 = points[i][0] * cell_size
    y1 = points[i][1] * cell_size

    dx = (x1 - x0)
    dy = (y1 - y0)

    step = max(abs(dx), abs(dy))

    dX = dx / step
    dY = dy / step

    for j in range(0, step):
        x = (x0 + cell_size / 2) + (j * dX)
        y = (y0 + cell_size / 2) + (j * dY)

        canvas.create_line(x, y, x + 1, y + 1)
        time.sleep(0.01)
        tk.update()

        print(x, y)


tk.mainloop()
