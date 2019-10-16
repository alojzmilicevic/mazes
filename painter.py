from tkinter import *
import time
from breadthFirst import solve as bf_solve

_WIDTH = 1024
_HEIGHT = 1024


def _get_offset(i, maze_size, cell_size):
    x = (i * cell_size) % _WIDTH
    y = int(i / maze_size) * cell_size

    return x, y


# def k(event):
#    if event.keycode == 9:
#        pass


class Painter:
    def __init__(self):
        self._tk = Tk()
        self._canvas = Canvas(self._tk, width=_WIDTH, height=_HEIGHT)
        # self._canvas.focus_set()
        # self._canvas.bind("<Key>", k)
        self._canvas.pack()

    def draw(self, maze):
        cell_size = _WIDTH / maze.size()
        size = len(maze.maze)

        nodes = bf_solve(maze)[0]
        for i in range(0, size):
            x, y = _get_offset(i, maze.size(), cell_size)
            # print("X, Y: (" + str(x) + "," + str(y) + ")") # Remove this if you want to print x, y
            self._canvas.create_rectangle(x, y, x + cell_size, y + cell_size,
                                          fill="white" if maze.maze[i] == 255 else "black")

        for i in range(1, len(nodes)):
            x0 = nodes[i - 1].Position[0] * cell_size
            y0 = nodes[i - 1].Position[1] * cell_size

            x1 = nodes[i].Position[0] * cell_size
            y1 = nodes[i].Position[1] * cell_size

            dx = (x1 - x0)
            dy = (y1 - y0)

            step = max(abs(dx), abs(dy))

            dx = dx / step
            dy = dy / step

            self._draw_centered_oval(x0, y0, diameter=cell_size / 2)

            # start at cell_size / 4 because we can skip drawing a line where there is a node
            for j in range(int(cell_size / 4), int(step)):
                x = (x0 + cell_size / 2) + (j * dx)
                y = (y0 + cell_size / 2) + (j * dy)

                self._canvas.create_line(x, y, x + 2, y + 2)
                time.sleep(0.002)
                self._tk.update()

            self._draw_centered_oval(x1, y1, diameter=cell_size / 2)
        self._tk.mainloop()

    def _draw_centered_oval(self, x, y, diameter):
        x = x + (diameter / 2)
        y = y + (diameter / 2)

        self._canvas.create_oval(x, y, x + diameter, y + diameter, fill="#a2eaf2")
