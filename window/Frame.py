"""
This class is just a tkinter wrapper to hide some of the work.
"""

from tkinter import *


class Frame:
    def __init__(self, size):
        self.__size = size

        self.__tk = Tk()
        self.__tk.title('Maze')
        self._canvas = Canvas(self.__tk, width=size, height=size)
        self._canvas.pack()
        self.__tk.bind("<Escape>", self.close)

    def init(self):
        self.draw()

    def close(self, event):
        self.__tk.withdraw()
        sys.exit()

    def draw(self):
        raise NotImplementedError

    def to_string(self):
        return "Frame: Size (" + str(self.__size) + ", " + str(self.__size) + ")"

    def get_render_target(self):
        return self._canvas

    def run(self):
        self.__tk.mainloop()
