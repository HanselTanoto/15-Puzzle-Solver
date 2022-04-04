"""
Branch and Bound Algorithm to Solve 15-Puzzle
"""

import sys
import util
import heapq


class node:
    """
    Node class for the branch and bound algorithm. Represents a tile in the 15 puzzle board.
    Attributes:
        cost        : cost of the node = sum of the cost from root to goal node through this node
        idx         : index of the node in branch and bound tree
        depth       : depth of the node
        matrix      : the matrix of the node
        direction   : direction taken to reach this node
        parent      : parent of the node
    """
    ## CONSTRUCTOR
    def __init__(self, cost=None, idx=0, depth=None, matrix=None, direction=None, parent=None):
        self.cost = cost
        self.idx = idx
        self.depth = depth
        self.matrix = matrix
        self.direction = direction
        self.parent = parent
    
    ## __lt__ (LESS THAN OPERATOR) OVERLOAD
    def __lt__(self, other):
        return self.cost < other.cost
    
    ## __repr__ OVERLOAD
    def __repr__(self):
        return "node(cost={}, idx={}, depth={}, matrix={}, direction={})".format(self.cost, self.idx, self.depth, self.matrix, self.direction)
    
    ## __getitem__ OVERLOAD
    def __getitem__(self, key):
        return self.__dict__[key]


def Kurang(i, matrix):
    """
    KURANG(i) = the number of tiles numbered j such that
    j < i and tile j positioned to the right (after) of tile i
    """
    # Convert matrix to array
    array = util.matrixToArray(matrix)
    sum = 0;
    # Iterate through the array and compute Kurang(i)
    for j in array:
        if j < i and array.index(j) > array.index(i):
            sum += 1
    return sum


def isSolvable(matrix):
    """
    Checks if the puzzle is solvable based on the value of
    SUM(KURANG(i))+x
    """
    # Convert matrix to array
    array = util.matrixToArray(matrix)
    # Initialize variables
    kurang = []
    x = 0
    total = 0
    # Iterate through the array and calculate SUM(KURANG(i))
    for i in array:
        kurang_i = Kurang(i, matrix)
        total += kurang_i
        heapq.heappush(kurang, (i, kurang_i))
    # Find empty cell and calculate x
    i, j = findEmptyCellIdx(matrix)
    if (i + j) % 2 != 0:    
        x = 1
        total += x
    # Check if the puzzle is solvable
    if total % 2 == 0:
        return True, kurang, x, total
    else:
        return False, kurang, x, total


def isEmptyCell(x):
    """
    Checks if x is the empty cell
    """
    return x < 1 or x > 15


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
    The number of tiles, except the empty cell, that are 
    out of place in the current state (matrix)
    """
    # Convert matrix to array
    array = util.matrixToArray(matrix)
    count = 0
    # Iterate through the array and check if the tile is in place
    for i in range(16):
        if (not isEmptyCell(array[i])) and (array[i] != i + 1) :
            count += 1
    return count


def isSolved(matrix):
    """
    Checks if the puzzle is solved (matrix is in the goal state)
    """
    return cellNotInPlace(matrix) == 0 


def cost(matrix, depth):
    """
    Calculates the cost of a node.
    c(i) = f(i) + g(i) where:
    c(i) is the total cost of the node,
    f(i) is the cost so far to reach the node from root,
    g(i) is the cost from the node to the goal node.
    """
    return cellNotInPlace(matrix)+depth


def swap(direction, matrix):
    """
    Swap two elements in a matrix based on the direction.
    Swaps the empty cell with the tile in the direction.
    """
    # Create a copy of the matrix
    temp = util.copyMatrix(matrix)
    # Find the empty cell
    i, j = findEmptyCellIdx(temp)
    if direction == "UP":
        temp[i][j], temp[i-1][j] = temp[i-1][j], temp[i][j]
    elif direction == "DOWN":
        temp[i][j], temp[i+1][j] = temp[i+1][j], temp[i][j]
    elif direction == "LEFT":
        temp[i][j], temp[i][j-1] = temp[i][j-1], temp[i][j]
    elif direction == "RIGHT":
        temp[i][j], temp[i][j+1] = temp[i][j+1], temp[i][j]
    return temp


def inverseMove(move):
    """
    Returns the inverse direction of a move
    """
    if move == "UP":
        return "DOWN"
    elif move == "DOWN":
        return "UP"
    elif move == "LEFT":
        return "RIGHT"
    elif move == "RIGHT":
        return "LEFT"


def moveCandidate(matrix, prev_move, evaluated_matrix):
    """
    Returns a list of possible moves from the current state (matrix)
    """
    # Initial move candidates
    direction = ["UP", "RIGHT", "DOWN", "LEFT"]
    # Check if the empty cell is in the edge of the board
    i, j = findEmptyCellIdx(matrix)
    if (i == 0):
        direction.remove("UP")
    elif (i == 3):
        direction.remove("DOWN")
    if (j == 0):
        direction.remove("LEFT")
    elif (j == 3):
        direction.remove("RIGHT")
    # Avoid move candidates that are the inverse of the previous move
    inv_prev_move = inverseMove(prev_move)
    if inv_prev_move in direction:
        direction.remove(inv_prev_move)
    # Avoid move candidates that produce matrix that have already been evaluated before
    for d in direction:
        if (util.matrixToString(swap(d, matrix)) in evaluated_matrix):
            direction.remove(d)
        """for node in evaluated_nodes:
            if (swap(d, matrix) == node.matrix):
                direction.remove(d)
                break"""
    return direction


def solveBnB(matrix):
    """
    Solves the puzzle using the Branch and Bound algorithm
    """
    # Initialize variables
    generated_nodes = []
    live_nodes = []
    evaluated_nodes = []
    evaluated_states = []

    direction = "START"
    depth = 0
    idx = 0
    current_cost = cost(matrix, depth)

    # Create the root node then add it to the live nodes and generated nodes
    root = node(current_cost, idx, depth, matrix, direction)
    heapq.heappush(live_nodes, (root))
    generated_nodes.append(root)

    # Iterate until the live nodes is empty
    while (len(live_nodes) > 0):
        # Get the node with the lowest cost
        expand_node = heapq.heappop(live_nodes)
        # Add the node to the evaluated nodes
        evaluated_nodes.append(expand_node)
        evaluated_states.append(util.matrixToString(expand_node.matrix))

        # Check if the puzzle is solved
        if (isSolved(expand_node.matrix)):
            break
        
        # Get the possible moves from the current state
        move_candidate = moveCandidate(expand_node.matrix, expand_node.direction, evaluated_states)
        depth = expand_node.depth + 1
        
        # Iterate through the possible moves
        for direction in move_candidate:
            idx += 1
            # Create a new node (children) that is the result of the move
            child_matrix = swap(direction, expand_node.matrix)
            child_cost = cost(child_matrix, depth)
            child = node(child_cost, idx, depth, child_matrix, direction, expand_node)
            # Add the child to the live nodes and generated nodes
            heapq.heappush(live_nodes, (child))
            generated_nodes.append(child)
        print("Generating nodes... " + str(idx), end='\r')
        sys.stdout.flush()
    final_node = expand_node
    return generated_nodes, evaluated_nodes, final_node


def getSolutionPath(node):
    """
    Returns the solution path from the root node to the goal node
    """
    path = []
    while (node.parent != None):
        path.insert(0, node)
        node = node.parent
    path.insert(0, node)
    return path