from image_parser import ImageParser

parser = ImageParser("8x8.png")
maze = parser.get_maze()
parser.info()

maze.print_maze()
