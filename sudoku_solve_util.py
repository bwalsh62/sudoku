# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 13:49:33 2020

@author: benja
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