from collections import deque


def solve(maze):
    print('Solving maze using breadth first...')

    start = maze.start
    end = maze.end
    width = maze.size()
    height = maze.size()

    queue = deque([start])
    prev = [None] * (width * height)
    visited = [False] * (width * height)

    count = 0

    completed = False

    visited[start.Position[0] * width + start.Position[1]] = True

    while queue:
        count += 1
        current = queue.pop()

        if current == end:
            completed = True
            break

        for n in current.Neighbours:
            if n is not None:
                npos = n.Position[0] * width + n.Position[1]
                if not visited[npos]:
                    queue.appendleft(n)
                    visited[npos] = True
                    prev[npos] = current

    path = deque()
    current = end
    while current is not None:
        path.appendleft(current)
        current = prev[current.Position[0] * width + current.Position[1]]

    return [path, [count, len(path), completed]]
