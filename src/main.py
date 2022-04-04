"""
Main Program for 15 Puzzle Solver (CLI)
"""

import os
import time
import util
import branch_and_bound

## HEADER
print()
print("++-------------------------++")
print("||    15 PUZZLE SOLVER     ||")
print("++-------------------------++")
print()

## MAIN PROGRAM
while(True):
    ## CHOOSE MENU
    choice = util.printMenu()
    
    if choice == "1":
        file = input("INPUT PATH FILE: ")
        print("Reading puzzle configuration...")
        matrix = util.fileToMatrix(file)
        if (matrix == None):
            print("File not found! Current working directory is", os.getcwd(), ".\n")
            continue
        if (not util.isMatrixValid(matrix)):
            print("Invalid matrix!\n")
            continue
    
    elif choice == "2":
        print("Generating a random puzzle configuration...\n")
        matrix = util.randomMatrix()
    
    elif choice == "3":
        print("Exiting...\n")
        break

    ## PRINT INITIAL STATE
    print("<< INITIAL STATE >>")
    util.printMatrix(matrix)
    
    ## CHECK SOLVABILITY
    start_time = time.time()
    print("<<  SOLVABILITY  >>")
    solvable = branch_and_bound.isSolvable(matrix)
    pause_time = time.time()
    
    ## PRINT SOLVABILITY INFORMATION 
    util.printIsSolvableInfo(solvable[0], solvable[1], solvable[2], solvable[3])
    
    ## SOLVE PUZZLE
    if (solvable[0]):
        ## SOLVING PUZZLE USING BRANCH AND BOUND
        resume_time = time.time()
        generated_nodes, evaluated_nodes, final_node = branch_and_bound.solveBnB(matrix)
        solution_path = branch_and_bound.getSolutionPath(final_node)
        end_time = time.time()
        
        ## PRINT MATRIX TRANSFORMATION TO SOLVE PUZZLE
        print("<< SOLUTION PATH >>")
        for node in solution_path:
            print("+------{:02d}------+".format(node.depth))
            print("|" + (node.direction).center(14) + "|")
            print("|" + ("COST = " + str(node.cost)).center(14) + "|")
            util.printMatrix(node.matrix)
        print("Puzzle succesfuly solved!")
        
        ## PRINT SOLUTION INFORMATION / STATS
        elapsed_time = end_time - resume_time + pause_time - start_time
        print("ELAPSED TIME     : {} milliseconds".format(round(elapsed_time * 1000, 3)))
        print("GENERATED NODES  : {} nodes".format(len(generated_nodes)))
        print("EVALUATED NODES  : {} nodes".format(len(evaluated_nodes)))
        print("DEPTH            : {}".format(final_node.depth))

    ipt = input("\nPress enter to continue...")
    print("\n")