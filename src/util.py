"""
Utility Functions: Input/Output & Transformation
"""

import random
import heapq

from numpy import array


def fileToMatrix(filePath):
    """
    Reads a file and returns a matrix of the contents
    """
    try :
        open(filePath, "r")
    except FileNotFoundError:
        return None
    with open(filePath) as f:
        matrix = []
        for line in f:
            row = []
            for i in line.split():
                if (i.isnumeric()): 
                    if (int(i) >= 1 or int(i) <= 15):
                        row.append(int(i))
                else:   # empty tile in 15 puzzle problem
                    row.append(16)
            matrix.append(row)
        return matrix


def randomMatrix():
    """
    Returns a random matrix with no repeated numbers (1 to 16)
    """
    list = random.sample(range(1,17), 16)
    return arrayToMatrix(list)


def isMatrixValid(matrix):
    """
    Checks if the matrix is valid
    """
    array = matrixToArray(matrix)
    # Checks if the matrix member is unique
    unique = len(array) == len(set(array))
    # Checks the number of empty tiles
    empty_tile = sum(1 for i in array if (i < 1 or i > 15))
    return unique and empty_tile == 1


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


def matrixToString(matrix):
    """
    Converts a matrix to a string
    """
    string = ""
    for row in matrix:
        for col in row:
            string += str(col) + " "
    return string


def copyMatrix(matrix):
    """
    Returns a copy of a matrix
    """
    copy = []
    for row in matrix:
        copy.append(row.copy())
    return copy


def findMatrixIndex(matrix, value):
    """
    Finds the index of a value in a matrix
    """
    for row in range(4):
        for col in range(4):
            if matrix[row][col] == value:
                return row, col
    # value not found
    return None


def printMatrix(matrix):
    """
    Prints a matrix as a 15 puzzle board
    """
    print("+--------------+")
    for row in matrix:
        for col in row:
            if (col >= 1 and col <= 15):
                print("[" + str(col).rjust(2, ' '), end=']')
            else: # empty tile in 15 puzzle problem
                print("[  ]", end="")
        print()
    print("+--------------+\n")


def printMenu():
    """
    Prints the menu for the main program
    """
    while (True):
        print("-----------------------------")
        print("CHOOSE AN OPTION (1/2/3):")
        print("1. Read matrix from text file")
        print("2. Generate a random matrix")
        print("3. Exit")
        choice = input("CHOICE: ")
        print("-----------------------------")
        if choice == "1" or choice == "2" or choice == "3":
            break
        print("Invalid choice, please insert 1/2/3!\n")
    print()
    return choice


def printIsSolvableInfo(is_solvable, kurang, x, total):
    """
    Prints the information about the solvability of a matrix
    """
    # Prints the value of Kurang(i) for each tile i
    while (len(kurang) > 0):
        temp = heapq.heappop(kurang)
        print("KURANG({})".format("-" if (temp[0]<1 or temp[0]>15) else temp[0]).ljust(19) + "= " + str(temp[1]).rjust(2))
    # Prints the x value indicating where the empty tile is
    print("X                  =  " + str(x))
    print("-"*23,"+")
    # Prints the value of SUM(Kurang(i))+x
    print("SUM(KURANG(i)) + X = {}".format(total))
    # Prints the solvability of the matrix
    if is_solvable:
        print("Puzzle is solvable!\n")
    else:
        print("Puzzle is not solvable!\n")