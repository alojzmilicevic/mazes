from PIL import Image, ImageDraw


def show(maze, nodes, file_name):
    width = 16 * 16 * 4
    img = Image.open(file_name).resize((width, width))
    draw = ImageDraw.Draw(img)

    cell_size = width / maze.size()
    for i in range(1, len(nodes)):
        prev = nodes[i - 1]
        cur = nodes[i]

        x = prev.Position[0] * cell_size + (cell_size / 4)
        x2 = prev.Position[0] * cell_size + (3 / 4 * cell_size)
        y = prev.Position[1] * cell_size + (cell_size / 4)
        y2 = prev.Position[1] * cell_size + (3 / 4 * cell_size)

        draw.line([(cell_size * prev.Position[0] + cell_size / 2, cell_size * prev.Position[1] + cell_size / 2),
                   (cell_size * cur.Position[0] + cell_size / 2, cell_size * cur.Position[1] + cell_size / 2)],
                  fill='red', width=9)
        draw.ellipse([x, y, x2, y2], fill='blue')

    img.show()

