# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 13:49:33 2020

@author: Ben Walsh
"""

#%% Check column
def check_col(input_puzzle, col, options):
    
    new_options = [digit for digit in options if digit not in input_puzzle[:,col]] 
    
    return new_options

#%% Check row 
def check_row(input_puzzle, row, options):
    
#    # Long form
#    new_options = []
#    for digit in options:
#        if digit not in input_puzzle[row,:]:
#            new_options.append(digit)
    
    # Compact form
    new_options = [digit for digit in options if digit not in input_puzzle[row,:]] 
    
    return new_options

#%% Check cell
def check_cell(input_puzzle, row, col, options):
    
    row_idx_cell = row//3*3
    col_idx_cell = col//3*3
    for row in range(row_idx_cell,row_idx_cell+3):
        for col in range(col_idx_cell,col_idx_cell+3):
            # For each element in cell, if the element found was considered 
            # an options for the empty element remove from the list
            if input_puzzle[row,col] in options:
                options.remove(input_puzzle[row,col])
    
    return options

#%% Save puzzles as an example

# Could be hidden method in class
def display_sudoku_row(in_list):
    print('| {} {} {} | {} {} {} | {} {} {} |'.format(in_list[0],in_list[1],in_list[2],
                                  in_list[3],in_list[4],in_list[5],
                                  in_list[6],in_list[7],in_list[8]))
    return True

class sud_puzzle:
    
    def __init__(self,difficulty='Easy'):
        self.difficulty = difficulty
        dif_levels = ('Easy','Medium','Hard')
        default_dif = dif_levels[0]
        if difficulty not in dif_levels:
            print('Input difficulty {} not recognized. {} used as default'.format(difficulty,default_dif))
            self.difficulty = default_dif
        
        # Easy puzzle
        if self.difficulty == dif_levels[0]:
            self.puzzle = [[0,4,9,0,3,1,0,0,7], 
                             [0,3,0,0,7,0,9,8,0],
                             [8,0,7,0,4,0,0,0,3],
                             [0,0,6,1,5,7,8,3,2],
                             [7,5,3,2,8,4,1,0,6],
                             [0,1,0,3,0,0,7,4,5],
                             [0,8,5,7,0,3,4,0,9],
                             [0,0,2,4,0,5,3,7,8],
                             [3,7,4,0,2,0,5,0,1]]
        
        # Medium puzzle 
        if self.difficulty == dif_levels[1]:
            self.puzzle = [[0,0,0,0,5,6,0,9,0], 
                             [1,4,9,0,0,0,0,0,0],
                             [0,8,0,3,0,9,0,2,0],
                             [0,0,3,0,6,0,0,0,5],
                             [2,0,0,0,8,0,0,0,6],
                             [4,0,0,0,3,0,2,0,0],
                             [0,9,0,7,0,1,0,8,0],
                             [0,0,0,0,0,0,7,5,1],
                             [0,7,0,5,4,0,0,0,0]]
        
        # Hard puzzle (placeholder, still easy for now)
        if self.difficulty == dif_levels[2]:
            self.puzzle = [[0,0,8,0,0,9,5,0,0], 
                             [5,0,0,4,0,3,0,0,9],
                             [0,0,0,0,0,0,0,0,7],
                             [7,8,0,0,0,0,2,0,0],
                             [0,9,2,0,6,0,8,1,0],
                             [0,0,4,0,0,0,0,9,5],
                             [0,7,0,0,0,0,0,0,0],
                             [9,0,0,1,0,6,0,0,7],
                             [0,0,1,2,0,0,3,0,0]]
    
    def display(self):
        print('-------------------------')
        display_sudoku_row(self.puzzle[0][:])
        display_sudoku_row(self.puzzle[1][:])
        display_sudoku_row(self.puzzle[2][:])
        print('-------------------------')
        display_sudoku_row(self.puzzle[3][:])
        display_sudoku_row(self.puzzle[4][:])
        display_sudoku_row(self.puzzle[5][:])
        print('-------------------------')
        display_sudoku_row(self.puzzle[6][:])
        display_sudoku_row(self.puzzle[7][:])
        display_sudoku_row(self.puzzle[8][:])
        print('-------------------------')
