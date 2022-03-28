import random


def fileToMatrix(filePath):
    """
    Reads a file and returns a matrix of the contents
    """
    with open(filePath) as f:
        matrix = []
        for line in f:
            matrix.append(list(map(int, line.split())))
        return matrix


def randomMatrix():
    """
    Returns a random matrix with no repeated numbers
    """
    list = random.sample(range(1,17), 16)
    return arrayToMatrix(list)


def printMatrix(matrix):
    """
    Prints a matrix
    """
    for row in matrix:
        for col in row:
            if (col >= 1 and col <= 15):
                print("[" + str(col).rjust(2, ' '), end=']')
            else:
                print("[  ]", end="")
        print()


def matrixToArray(matrix):
    """
    Converts a matrix to an array
    """
    array = []
    for row in matrix:
        for col in row:
            array.append(col)
    return array


def arrayToMatrix(array):
    """
    Converts an array to a matrix
    """
    matrix = []
    for i in range(4):
        matrix.append(array[i*4:i*4+4])
    return matrix


def findMatrixIndex(matrix, value):
    """
    Finds the index of a value in a matrix
    """
    for row in range(4):
        for col in range(4):
            if matrix[row][col] == value:
                return row, col
    return None


