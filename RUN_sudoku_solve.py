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

#%% Test high-level solver

num_empty_elem = (puzzle==emptyKey).sum()
new_num_empty_elem = num_empty_elem

print('Number of empty elements = {}'.format(num_empty_elem))
# Initialize loop counter
cycle_num = 1

# Continue as long as making progress
while True:
    
    # Re-initialize starting number of empty elemnts
    num_empty_elem = (puzzle==emptyKey).sum()
    
    for row in range(9):
        for col in range(9):
            if puzzle[row,col] == emptyKey:
                options = [1,2,3,4,5,6,7,8,9]
                options = check_col(puzzle,col,options)
                options = check_row(puzzle,row,options)
                options = check_cell(puzzle, row, col, options)
                if len(options) == 1:
                    puzzle[row,col] = options[0]
    
    # Check to see how many empty elements there are now                
    new_num_empty_elem = (puzzle==emptyKey).sum() 
    
    # Break loop if no progress was made        
    if new_num_empty_elem==num_empty_elem:
        break
    else:
        print('Round {}: number of empty elements = {}'.format(cycle_num, new_num_empty_elem))
        cycle_num = cycle_num+1


