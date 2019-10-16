from models.graph_drawer import GraphDrawer


class Graph:
    class Node:
        def __init__(self, position):
            self.Position = position
            self.Neighbours = [None, None, None, None]

    def __init__(self, data, rows, cell_size):
        self.__data = data
        self.__rows = rows
        self.__create_graph()
        self.__path = []
        self.__graph_drawer = GraphDrawer(self, cell_size)

    # Private functions
    def __create_graph(self):
        # Iterate through the graph and connect all nodes, single pass
        topnodes = [None] * self.__rows
        self.start = None
        self.end = None
        count = 0

        # Start row
        for x in range(1, self.__rows - 1):
            if self.__data[x] > 0:
                self.start = Graph.Node((x, 0))
                topnodes[x] = self.start
                count += 1
                break

        for y in range(1, self.__rows - 1):
            rowoffset = y * self.__rows
            rowaboveoffset = rowoffset - self.__rows
            rowbelowoffset = rowoffset + self.__rows

            prv = False
            cur = False
            nxt = self.__data[rowoffset + 1] > 0

            leftnode = None

            for x in range(1, self.__rows - 1):
                prv = cur
                cur = nxt
                nxt = self.__data[rowoffset + x + 1] > 0

                n = None
                if not cur:
                    continue

                if prv:
                    if nxt:
                        # PATH PATH PATH
                        # om det finns något över / under
                        if self.__data[rowaboveoffset + x] > 0 or self.__data[rowbelowoffset + x] > 0:
                            n = Graph.Node((x, y))
                            leftnode.Neighbours[1] = n
                            n.Neighbours[3] = leftnode
                            leftnode = n

                    else:
                        pass
                        # PATH PATH WALL
                        n = Graph.Node((x, y))
                        leftnode.Neighbours[1] = n
                        n.Neighbours[3] = leftnode
                        leftnode = None

                else:
                    if nxt:
                        # WALL PATH PATH
                        n = Graph.Node((x, y))
                        leftnode = n

                    else:
                        # WALL PATH WALL
                        if self.__data[rowaboveoffset + x] == 0 or self.__data[rowbelowoffset + x] == 0:
                            # Check above or below
                            n = Graph.Node((x, y))

                if n is not None:
                    # Clear above, connect to waiting top node
                    if self.__data[rowaboveoffset + x] > 0:
                        t = topnodes[x]
                        t.Neighbours[2] = n
                        n.Neighbours[0] = t

                    # If clear below, put this new node in the top row for the next connection
                    if self.__data[rowbelowoffset + x] > 0:
                        topnodes[x] = n
                    else:
                        topnodes[x] = None

                    count += 1

        rowoffset = (self.__rows - 1) * self.__rows
        for x in range(1, self.__rows - 1):
            if self.__data[rowoffset + x] > 0:
                self.end = Graph.Node((x, self.__rows - 1))
                t = topnodes[x]
                t.Neighbours[2] = self.end
                self.end.Neighbours[0] = t
                count += 1
                break

        self.__count = count

    def get_path(self):
        return self.__path

    def draw(self, render_target):
        self.__graph_drawer.draw(render_target)

    def solve(self, solver):
        self.__path = solver(self)[0]

    def get_path(self):
        return self.__path

    def size(self):
        return 0 if self.__count is None else self.__count

    def print_info(self):
        if self.__count is None:
            return
        print('\n========= Graph Information =========')
        print('     Number of nodes created: ' + str(self.__count))
        print('=====================================')
