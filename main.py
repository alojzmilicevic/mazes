from image_parser import ImageParser
from breadthFirst import solve as bf_solve
from drawModule import show as draw_maze
from painter import Painter

file_name = "images/8x8.png"
parser = ImageParser(file_name)
maze = parser.get_maze()

parser.info()
maze.info()

# draw_maze(maze, bf_solve(maze)[0], file_name)

painter = Painter()
painter.draw(maze)
