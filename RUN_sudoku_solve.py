# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 13:50:04 2020

@author: Ben Walsh

https://sudoku.com/easy/

"""

#%% Import libraries

import numpy as np

# Custom library for sudoku solving algorithm
from sudoku_solve_util import check_col, check_row

#%% Test Sudoku

# define emptyKey as 0
emptyKey = 0

puzzle_list = [[0,4,9,0,3,1,0,0,7], 
         [0,3,0,0,7,0,9,8,0],
         [8,0,7,0,4,0,0,0,3],
         [0,0,6,1,5,7,8,3,2],
         [7,5,3,2,8,4,1,0,6],
         [0,1,0,3,0,0,7,4,5],
         [0,8,5,7,0,3,4,0,9],
         [0,0,2,4,0,5,3,7,8],
         [3,7,4,0,2,0,5,0,1]]

puzzle = np.array(puzzle_list)

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
    #            options = cell_check(options)
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


