#########################################################
# This is a utility file that contains some useful      #
# utility functions                                     #
#########################################################


# Prints a matrix to console
def print_matrix(matrix, width, height):

    print("Printing image...")
    for i in range(width):
        for j in range(height):
            print(". " if matrix[i][j] == 0 else "o ", end='')
        print()
