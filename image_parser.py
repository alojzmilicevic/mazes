#########################################################
# This class is responsible for parsing the image file  #
#########################################################
from PIL import Image


class ImageParser:
    def __init__(self, file_name):
        self.__im = None
        self.__open(file_name)

    def __open(self, file_name):
        try:
            self.__im = Image.open(file_name).convert("RGB")
            print("Image opened successfully...")
        except IOError:
            print("ERROR: Could not open image.")
            print("Exiting with error code 1...")

            exit(1)

    def parse_image(self):
        return list(self.__im.getdata(0)), self.__im.size

    def print_info(self):
        print("\n========== Image information ==========")
        print("  The size of the image is " + str(self.__im.size))
        print("  Image mode: ", self.__im.mode)
        print("=======================================")
