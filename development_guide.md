# sudoku
Solve an input Sudoku puzzle

## Prompt

You are on a team tasked with developing a Sudoku (add link to wikipedia) application. You are leading one feature of the application: an automatic Sudoku Solver.

Input: Sudoku puzzle

Output: Solved Sudoku puzzle

## Project Planning

Where to begin? Before even writing code, lay out your plan for the project. This will help shape the structure of your project, including the need to develop any custom functions.

Sudoku (add link to wikipedia) is a puzzle where a 9x9 grid (see picture below) is partially filled with the digits 1, 2, ... up to 9. The grid also shows 9 individual 3x3 grids which comprise the overall grid. 

To fill the puzzle, there are three rules:
1. Each column must have exactly one instance of each digit 1-9
2. Each row must have exactly one instance of each digit 1-9
3. Each 3x3 cell (distinctly shown, non-overlapping) must have exactly one instance of each digit 1-9

By applying these rules to an empty cell, you can deduce what possible digits can fit in a cell. If there is only one option, you know the remaining digit must be the answer.

In pseudocode:

```
for each cell:
    apply rule 1: column check
    apply rule 2: row check
    apply rule 3: cell check
    if only one option:
        fill in cell with option
```

Consider the inputs and outputs of each function. For an empty cell, you start with 9 possibilities. Rule 1: Column check excludes any digits that are found in the column. So as input, it takes the current possibilities, and as output, it should return the new list of possibilities. Each successive rule now only needs to check the new list of updated options.

```
for each cell:
    options = [1,2,3,4,5,6,7,8,9]
    options = column_check(options)
    options = row_check(options)
    options = cell_check(options)
    if only one option::
        fill in cell with option
```

High level flow diagrams

## Function / class methods

solveRow
solveColumn
solveBox

Loop through all elements

Loop through until not making progress

### Error handling

### Debugging

## Describing

### Readme/GitHub

### LinkedIn/Resume

### Interview
