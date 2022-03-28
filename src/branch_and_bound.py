import util


def Kurang(i, matrix):
    """
    KURANG(i) = banyaknya ubin bernomor j 
    sedemikian sehingga j < i dan POSISI(j) > POSISI(i). 
    POSISI(i) = posisi ubin bernomor i pada susunan
    yang diperiksa.
    """
    array = util.matrixToArray(matrix)
    sum = 0;
    for j in array:
        if j < i and array.index(j) > array.index(i):
            sum += 1
    return sum


def isSolvable(matrix):
    """
    Menentukan apakah puzzle (dalam bentuk matrix) ini bisa diselesaikan
    """
    array = util.matrixToArray(matrix)
    total = 0
    for i in array:
        total += Kurang(i, matrix)
    i, j = findEmptyCellIdx(matrix)
    if (i + j) % 2 == 0:
        total += 1
    if total % 2 == 0:
        return True
    else:
        return False


def isEmptyCell(x):
    return x < 1 and x > 15


def findEmptyCellIdx(matrix):
    """
    Finds the index of the empty cell in a matrix
    """
    for row in range(4):
        for col in range(4):
            if (isEmptyCell(matrix[row][col])):
                return row, col
    return None


def cellNotInPlace(matrix):
    """
    Menghitung jumlah ubin / sel yang tidak pada tempatnya saat ini
    """
    array = util.matrixToArray(matrix)
    count = 0
    for i in range(16):
        if (not isEmptyCell(array[i])) and (array[i] != i + 1) :
            count += 1
    return count


def cost(matrix, depth):
    """
    Menghitung cost / biaya dari suatu state
    """
    return cellNotInPlace(matrix)+depth


def swap(direction, matrix):
    """
    Swap two elements in a matrix
    """
    i, j = findEmptyCellIdx(matrix)
    if direction == "left" and j > 0:
        matrix[i][j], matrix[i][j-1] = matrix[i][j-1], matrix[i][j]
    elif direction == "right" and j < 3:
        matrix[i][j], matrix[i][j+1] = matrix[i][j+1], matrix[i][j]
    elif direction == "up" and i > 0:
        matrix[i][j], matrix[i-1][j] = matrix[i-1][j], matrix[i][j]
    elif direction == "down" and i < 3:
        matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]
    return matrix

def BnB(matrix, depth=0):
    """
    Branch and Bound
    """
    if isSolvable(matrix):
        if cellNotInPlace(matrix) == 0:
            return depth
        else:
            for direction in ["left", "right", "up", "down"]:
                matrix = swap(direction, matrix)
                depth += 1
                result = BnB(matrix, depth)
                if result != None:
                    return result
                matrix = swap(direction, matrix)
                depth -= 1
    return None