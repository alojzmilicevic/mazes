from image_parser import ImageParser
from breadthFirst import solve as bf_solve
from painter import Painter

file_name = "images/8x8.png"
parser = ImageParser(file_name)
maze = parser.get_maze()

parser.info()
maze.info()

painter = Painter()
painter.draw(maze)
