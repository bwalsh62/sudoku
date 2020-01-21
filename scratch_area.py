# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 21:34:14 2020

@author: Ben Walsh

https://sudoku.com/easy/

"""

#%% Import libraries

import numpy as np

#%% Test Sudoku

# define emptyKey as 0
emptyKey = 0

# Initialize test sudoku
#puzzle = np.array(
#        [[0,4,9,0,3,1,0,0,7], 
#         [0,3,0,0,7,0,9,8,0],
#         [8,0,7,0,4,0,0,0,3],
#         [0,0,6,1,5,7,8,3,2],
#         [7,5,3,2,8,4,1,0,6],
#         [0,1,0,3,0,0,7,4,5],
#         [0,8,5,7,0,3,4,0,9],
#         [0,0,2,4,0,5,3,7,0],
#         [3,7,4,0,2,0,5,0,1]])

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

#%% Test row solve

def check_row(row_list):
    
    # Loop through each element in the row
    for idx, element in enumerate(row_list):
        # If empty, see how many numbers are options
        if element == emptyKey:
            n_options = 9
            choice = 0
            for num in range(1,10):
                n_options = n_options - row_list.count(num)
                if row_list.count(num)==0:
                    choice = num
            if n_options == 1:
                row_list[idx] = choice
    
    return row_list

input_test = puzzle[4][:]
print('Input = {}'.format(input_test))
check_row(input_test)

#%% Test column solve

#%% Test box solve

#%% Check column
def check_col(input_puzzle, col, options):
    
    new_options = [digit for digit in options if digit not in input_puzzle[:,col]] 
    
    return new_options

test_row = 1
test_column = 8
options = [1,2,3,4,5,6,7,8,9]
new_options = check_col(puzzle, test_column, options)

#%% Check row for np
def check_row(input_puzzle, row, options):
    
#    # Long form
#    new_options = []
#    for digit in options:
#        if digit not in input_puzzle[row,:]:
#            new_options.append(digit)
    
    # Compact form
    new_options = [digit for digit in options if digit not in input_puzzle[row,:]] 
    
    return new_options

test_row = 4
test_column = 7
options = [1,2,3,4,5,6,7,8,9]
new_options = check_row(puzzle, test_row, options)

#%% Test high-level solver

print('Number of empty elements = {}'.format((puzzle==emptyKey).sum()))

for row in range(9):
    for col in range(9):
        if puzzle[row,col] == emptyKey:
            options = [1,2,3,4,5,6,7,8,9]
            options = check_col(puzzle,col,options)
            options = check_row(puzzle,row,options)
#            options = cell_check(options)
            if len(options) == 1:
                puzzle[row,col] = options[0]
                
print('Now, number of empty elements = {}'.format((puzzle==emptyKey).sum()))
   

