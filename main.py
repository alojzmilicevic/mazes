from image_parser import ImageParser
from window.Frame import Frame
from maze import Maze
from breadthFirst import solve as bf

SIZE = 1024

file_name = "images/8x8.png"
parser = ImageParser(file_name)
data = parser.parse_image()
maze = Maze(data, SIZE)
maze.solve(solver=bf)

parser.print_info()
maze.print_info()


class Window(Frame):
    def draw(self):
        render_target = self.get_render_target()
        maze.draw(render_target)
        self.run()


window = Window(SIZE)
window.init()
