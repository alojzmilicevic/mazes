#########################################################
# This class is responsible for parsing the image file  #
#########################################################
from PIL import Image
from maze import Maze


class ImageParser:
    def __init__(self, file_name):
        self.im = None
        self.__open(file_name)

    def __open(self, file_name):
        try:
            self.im = Image.open(file_name).convert("RGB")
            print("Image opened successfully...")

            return self.im
        except IOError:
            print("ERROR: Could not open image.")
            print("Exiting with error code 1...")

            exit(1)

        return None

    def get_maze(self):
        return Maze(self.im)

    def info(self):
        print("\n========== Image information ==========")
        print("  The size of the image is " + str(self.im.size))
        print("  Image mode: ", self.im.mode)
        print("=======================================")
