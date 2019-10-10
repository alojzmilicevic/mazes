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

        topnodes = [None] * self.height
        self.start = None
        self.end = None
        count = 0

        # Start row
        for x in range(1, self.width - 1):
            if self.maze[x] > 0:
                self.start = Maze.Node((x, 0))
                topnodes[x] = self.start
                count += 1
                break

        for y in range(1, self.height - 1):
            rowoffset = y * self.width
            rowaboveoffset = rowoffset - self.width
            rowbelowoffset = rowoffset + self.width

            prv = False
            cur = False
            nxt = self.maze[rowoffset + 1] > 0

            leftnode = None

            for x in range(1, self.width - 1):
                prv = cur
                cur = nxt
                nxt = self.maze[rowoffset + x + 1] > 0

                n = None
                if not cur:
                    continue

                if prv:
                    if nxt:
                        # PATH PATH PATH
                        # om det finns något över / under
                        if self.maze[rowaboveoffset + x] > 0 or self.maze[rowbelowoffset + x] > 0:
                            n = Maze.Node((x, y))
                            leftnode.Neighbours[1] = n
                            n.Neighbours[3] = leftnode
                            leftnode = n
                            self.xx.append(x)
                            self.yy.append(y)
                    else:
                        pass
                        # PATH PATH WALL
                        n = Maze.Node((x, y))
                        leftnode.Neighbours[1] = n
                        n.Neighbours[3] = leftnode
                        leftnode = None
                        self.xx.append(x)
                        self.yy.append(y)
                else:
                    if nxt:
                        # WALL PATH PATH
                        n = Maze.Node((x, y))
                        leftnode = n
                        self.xx.append(x)
                        self.yy.append(y)
                    else:
                        # WALL PATH WALL
                        if self.maze[rowaboveoffset + x] == 0 or self.maze[rowbelowoffset + x] == 0:
                            # Check above or below
                            n = Maze.Node((x, y))
                            self.xx.append(x)
                            self.yy.append(y)

                if n is not None:
                    # Clear above, connect to waiting top node
                    if self.maze[rowaboveoffset + x] > 0:
                        t = topnodes[x]
                        t.Neighbours[2] = n
                        n.Neighbours[0] = t

                    # If clear below, put this new node in the top row for the next connection
                    if self.maze[rowbelowoffset + x] > 0:
                        topnodes[x] = n
                    else:
                        topnodes[x] = None

                    count += 1

        rowoffset = (self.height - 1) * self.width
        for x in range(1, self.width - 1):
            if self.maze[rowoffset + x] > 0:
                self.end = Maze.Node((x, self.height - 1))
                t = topnodes[x]
                t.Neighbours[2] = self.end
                self.end.Neighbours[0] = t
                count += 1
                break

        self.count = count
