class Maze:
    class Node:
        def __init__(self, position):
            self.Position = position
            self.Neighbours = [None, None, None, None]

    def __init__(self, maze):
        self.maze = list(maze.getdata(0))
        self.width = maze.size[0]
        self.height = maze.size[1]
        self.__create_graph()

    # Public functions
    def print_maze(self):
        rows = 0

        offset = (len(str(self.width)) - len(str(rows)) + 1)
        print(" " * (offset - 1), end='')
        for i in range(0, self.width):
            if i + 1 <= 10:
                print("  " + str(i + 1), end='')
            else:
                print(" " + str(i + 1), end='')

        for i in range(0, len(self.maze)):
            if i % self.width == 0:
                print()
                rows += 1
                print(str(rows), end=' ' * (len(str(self.width)) - len(str(rows)) + 1))

            is_node = False
            for j in range(0, len(self.yy)):
                if self.yy[j] == rows - 1 and self.xx[j] == i % self.width:
                    print("x  ", end='')
                    is_node = True

            if not is_node:
                if self.maze[i] > 0:
                    print(".  ", end='')
                else:
                    print("#  ", end='')

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    # Private functions
    def __create_graph(self):
        # Iterate through the graph and connect all nodes, single pass

        self.xx = []
        self.yy = []

        for y in range(0, self.height):
            if self.maze[y] > 0:
                self.xx.append(y)
                self.yy.append(0)

        for y in range(1, self.height - 1):
            rowoffset = y * self.width
            rowaboveoffset = rowoffset - self.width
            rowbelowoffset = rowoffset + self.width

            prv = False
            cur = False
            nxt = self.maze[rowoffset + 1] > 0

            for x in range(1, self.width - 1):
                prv = cur
                cur = nxt
                nxt = self.maze[rowoffset + x + 1] > 0

                if not cur:
                    continue

                if prv:
                    if nxt:
                        # PATH PATH PATH
                        # om det finns något över / under
                        if self.maze[rowaboveoffset + x] > 0 or self.maze[rowbelowoffset + x] > 0:
                            self.xx.append(x)
                            self.yy.append(y)
                    else:
                        pass
                        # PATH PATH WALL
                        self.xx.append(x)
                        self.yy.append(y)
                else:
                    if nxt:
                        # WALL PATH PATH
                        self.xx.append(x)
                        self.yy.append(y)
                    else:
                        # WALL PATH WALL
                        if self.maze[rowaboveoffset + x] == 0 or self.maze[rowbelowoffset + x] == 0:
                            # Check above or below
                            self.xx.append(x)
                            self.yy.append(y)

        for y in range(self.height * self.width - self.height, self.height * self.width):
            if self.maze[y] > 0:
                self.xx.append(y % self.height)
                self.yy.append(self.height - 1)
