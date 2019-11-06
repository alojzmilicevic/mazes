"""
This class represents the maze object, and the corresponding graph of that maze.
It is responsible for drawing the maze and the graph.

TODO: If this class gets too big break out the rendering and put it in a separate component (see graph_drawer)
"""
from graph import Graph


class Maze:
    def __init__(self, data, size):
        self.__maze = data[0]
        self.__rows = data[1][0]
        self.__cell_size = size / self.__rows
        self.__size = size
        self.__graph = Graph(self.__maze, self.__rows, self.__cell_size)

    def draw(self, render_target):
        for i in range(0, len(self.__maze)):
            x = (i * self.__cell_size) % self.__size
            y = int(i / self.__rows) * self.__cell_size
            # print("X, Y: (" + str(x) + "," + str(y) + ")") # Remove this if you want to print x, y
            render_target.create_rectangle(x, y, x + self.__cell_size, y + self.__cell_size,
                                           fill="white" if self.__maze[i] == 255 else "black")

        self.__graph.draw(render_target)

    def solve(self, solver):
        self.__graph.solve(solver)

    def print_info(self):
        self.__graph.print_info()
