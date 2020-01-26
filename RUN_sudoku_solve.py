# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 13:50:04 2020

@author: Ben Walsh

https://sudoku.com/easy/

"""

#%% Import libraries

import numpy as np

# Custom library for sudoku solving algorithm
from sudoku_solve_util import check_col, check_row, check_cell, sud_puzzle

#%% Test Sudoku

# define emptyKey as 0
emptyKey = 0

dif_level = 'Medium'

sud_puzzle_obj = sud_puzzle(dif_level)

puzzle = np.array(sud_puzzle_obj.puzzle)

#%% Function to check standard rules and fill in elements

def checkPuzzle(in_puzzle, print_steps = True, emptyKey = 0):
    
    cycle_num = 1
    
    out_puzzle = in_puzzle
    
    # Continue as long as making progress
    while True:
        
        # Re-initialize starting number of empty elemnts
        num_empty_elem = (out_puzzle==emptyKey).sum()
        
        for row in range(9):
            for col in range(9):
                if out_puzzle[row,col] == emptyKey:
                    options = [1,2,3,4,5,6,7,8,9]
                    options = check_col(out_puzzle,col,options)
                    options = check_row(out_puzzle,row,options)
                    options = check_cell(out_puzzle, row, col, options)
                    if len(options) == 1:
                        out_puzzle[row,col] = options[0]
        
        # Check to see how many empty elements there are now                
        new_num_empty_elem = (out_puzzle==emptyKey).sum() 
        
        # Break loop if no progress was made        
        if new_num_empty_elem==num_empty_elem:
            # If no progress was made, then no obvious options. Find a cell where there
            # are three options and make a guess.
            for row in range(9):
                for col in range(9):
                    if in_puzzle[row,col] == emptyKey:
                        options = [1,2,3,4,5,6,7,8,9]
                        options = check_col(out_puzzle,col,options)
                        options = check_row(out_puzzle,row,options)
                        options = check_cell(out_puzzle, row, col, options)
                        if len(options) == 2:
                            # Try first option
                            out_puzzle[row,col] = options[0]
                            solved_puzzle = checkPuzzle(out_puzzle, print_steps = True)
                            # If unsolved, then try other option
                            if (solved_puzzle==emptyKey).sum() >0:
                                out_puzzle[row,col] = options[1]
                                solved_puzzle = checkPuzzle(out_puzzle, print_steps = True)
            break
        else:
            if print_steps:
                print('Round {}: number of empty elements = {}'.format(cycle_num, new_num_empty_elem))
            cycle_num = cycle_num+1
    
    return out_puzzle

#%% Test high-level solver

num_empty_elem = (puzzle==emptyKey).sum()
new_num_empty_elem = num_empty_elem

print('Number of empty elements = {}'.format(num_empty_elem))
# Initialize loop counter
cycle_num = 1

solved_puzzle = checkPuzzle(puzzle, print_steps = True)

## Continue as long as making progress
#while True:
#    
#    # Re-initialize starting number of empty elemnts
#    num_empty_elem = (puzzle==emptyKey).sum()
#    
#    for row in range(9):
#        for col in range(9):
#            if puzzle[row,col] == emptyKey:
#                options = [1,2,3,4,5,6,7,8,9]
#                options = check_col(puzzle,col,options)
#                options = check_row(puzzle,row,options)
#                options = check_cell(puzzle, row, col, options)
#                if len(options) == 1:
#                    puzzle[row,col] = options[0]
#    
#    # Check to see how many empty elements there are now                
#    new_num_empty_elem = (puzzle==emptyKey).sum() 
#    
#    # Break loop if no progress was made        
#    if new_num_empty_elem==num_empty_elem:
#        break
#    else:
#        print('Round {}: number of empty elements = {}'.format(cycle_num, new_num_empty_elem))
#        cycle_num = cycle_num+1


