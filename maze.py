class Node(object):
    def __init__(self):
        self.__value = 0
        self.__neighbours = []

    def add_neighbour(self, other):
        self.__neighbours.append(other)

    def get_neighbours(self):
        return self.__neighbours

    def get_value(self):
        return self.__value


class Maze:

    def __init__(self, maze):
        self.maze = maze
        self.__cols = len(maze)
        self.__rows = len(maze[1])

        self.__create_graph()

    # Public functions
    def print_maze(self):
        for i in range(self.__rows):
            for j in range(self.__cols):
                print("#  " if self.maze[i][j] == 0 else ".  ", end='')
            print()

    def get_height(self):
        return self.__rows

    def get_width(self):
        return self.__cols

    # Private functions
    def __create_graph(self):

        # Top Row
        for i in range(0, self.__rows):
            if self.maze[0][i] == 1:
                self.start = (0, i)
                break

        # Iterate through the graph and connect all nodes, single pass
        for i in range(1, self.__rows):
            for j in range(1, self.__cols):
                pass

        # Bottom Row
        for i in range(0, self.__rows):
            if self.maze[self.__rows - 1][i] == 1:
                self.end = (self.__rows - 1, i)
                break
