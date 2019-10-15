from tkinter import *
import time
from math import fabs

from breadthFirst import solve as bf_solve

_WIDTH = 1024
_HEIGHT = 1024


class Painter:
    def __init__(self):
        self._tk = Tk()
        self._canvas = Canvas(self._tk, width=_WIDTH, height=_HEIGHT)
        self._canvas.pack()

    def draw(self, maze):
        cell_size = _WIDTH / maze.size()
        size = len(maze.maze)

        nodes = bf_solve(maze)[0]

        for i in range(0, size):
            x, y = self._get_offset(i, maze.size(), cell_size)
            # print("X, Y: (" + str(x) + "," + str(y) + ")") # Remove this if you want to print x, y
            self._canvas.create_rectangle(x, y, x + cell_size, y + cell_size,
                                          fill="white" if maze.maze[i] == 255 else "black")

        for i in range(1, len(nodes)):
            x0 = nodes[i - 1].Position[0]
            y0 = nodes[i - 1].Position[1]

            x1 = nodes[i].Position[0]
            y1 = nodes[i].Position[1]
            '''
            print("prev: ", prev)
            print("cur: ", cur)
            print('cell_size: ', cell_size)
            x0 = prev[0] * 32 + (cell_size / 4)
            y0 = prev[1] * cell_size + (cell_size / 4)

            x1 = cur[0] * cell_size + (3 / 4 * cell_size)
            y1 = cur[1] * cell_size + (3 / 4 * cell_size)

            print("(x0, y0): " + str(x0) + " : " + str(y0))
            dx = (x1 - x0)
            dy = (y1 - y0)
            step = 0

            if fabs(dx) >= fabs(dy):
                step = fabs(dx)
            else:
                step = fabs(dy)

            dx = dx / step
            dy = dy / step

            x = x1
            y = y1

            i = 1

            while i <= step:
                self._canvas.create_oval(x, y, x, y, fill="blue")
                x = x + dx
                y = y + dy
                i += 1
                self._tk.update()
                time.sleep(0.01)
            '''

            node_size = cell_size / 2

            x = x0 * cell_size + node_size / 2
            y = y0 * cell_size + node_size / 2
            x2 = x0 * cell_size + (3 / 4 * cell_size)
            y2 = y0 * cell_size + (3 / 4 * cell_size)

            self._canvas.create_line(cell_size * x0 + cell_size / 2,
                                     cell_size * y0 + cell_size / 2,
                                     cell_size * x1 + cell_size / 2,
                                     cell_size * y1 + cell_size / 2
                                     )

            self._draw_centered_oval(x, y, x2, y2, width=cell_size)

            self._tk.update()
            time.sleep(0.5)

        self._tk.mainloop()

    def _draw_centered_oval(self, x, y, x2, y2, width):
        self._canvas.create_oval(x, y, x2, y2, fill='red')

    def _get_offset(self, i, maze_size, cell_size):
        x = (i * cell_size) % _WIDTH
        y = int(i / maze_size) * cell_size

        return x, y
