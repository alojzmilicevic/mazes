"""
This Class is responsible for drawing a graph.
I didn't want to clutter the graph with rendering so i made this class for it instead.

TODO: Make it so this class receives a vector of absolute coordinates, not relative coordinates like (1,1)
    this class should not have to care about what it's rendering...
"""

import time


def _draw_centered_oval(x, y, diameter, render_target):
    x = x + (diameter / 2)
    y = y + (diameter / 2)

    render_target.create_oval(x, y, x + diameter, y + diameter, fill="#a2eaf2")


class GraphDrawer:
    def __init__(self, graph, cell_size):
        self.__graph = graph
        self.__cell_size = cell_size

    # Calculate the slope between two points.
    # Then draw many small lines between the two points being rendered.
    def draw(self, render_target):
        path = self.__graph.get_path()
        path_length = len(path)

        for i in range(1, path_length):
            x0 = path[i - 1].Position[0] * self.__cell_size
            y0 = path[i - 1].Position[1] * self.__cell_size

            x1 = path[i].Position[0] * self.__cell_size
            y1 = path[i].Position[1] * self.__cell_size

            dx = (x1 - x0)
            dy = (y1 - y0)

            step = max(abs(dx), abs(dy))

            dx = dx / step
            dy = dy / step

            _draw_centered_oval(x0, y0, self.__cell_size / 2, render_target)

            # start at cell_size / 4 because we can skip drawing a line where there is a node
            for j in range(int(self.__cell_size / 4), int(step)):
                x = (x0 + self.__cell_size / 2) + (j * dx)
                y = (y0 + self.__cell_size / 2) + (j * dy)

                render_target.create_line(x, y, x + 2, y + 2)
                time.sleep(0.002)
                render_target.update()

            _draw_centered_oval(x1, y1, self.__cell_size / 2, render_target)
