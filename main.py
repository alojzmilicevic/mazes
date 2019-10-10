from image_parser import ImageParser
from collections import deque
from PIL import Image, ImageDraw

parser = ImageParser("combo400.png")
maze = parser.get_maze()
parser.info()

maze.print_maze()
img = Image.open('combo400.png')
new_img = img.resize((16 * 16 * 4, 16 * 16 * 4))


def solve(maze):
    start = maze.start
    end = maze.end
    width = maze.width
    height = maze.height

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


nodes = solve(maze)[0]

draw = ImageDraw.Draw(new_img)

sz = 16 * 16 * 4 / maze.height
for i in range(1, len(nodes)):
    prev = nodes[i - 1]
    cur = nodes[i]

    draw.line([(sz * prev.Position[0] + sz / 2, sz * prev.Position[1] + sz / 2),
               (sz * cur.Position[0] + sz / 2, sz * cur.Position[1] + sz / 2)], width=10)
new_img.save("car_resized.png", "PNG", optimize=True)
new_img.show()
