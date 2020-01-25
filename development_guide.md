# Sudoku
Solve an input Sudoku puzzle

## Prompt

You are on a team tasked with developing a [Sudoku](https://en.wikipedia.org/wiki/Sudoku) application. You are leading one feature of the application: an automatic Sudoku Solver.

**Input**: Sudoku puzzle

**Output**: Solved Sudoku puzzle

## Project Planning

Where to begin? Before even writing code, lay out your plan for the project. This will help shape the structure of your project: the algorithms, main functions, and supporting utilities.

Sudoku is a puzzle where a 9x9 grid (see picture below) is partially filled with the digits 1, 2, ... up to 9. The grid also shows 9 individual 3x3 grids which comprise the overall grid. 

![](\easy_sudoku.PNG)

Three rules apply to a completed puzzle:
1. Each column must have exactly one instance of each digit 1-9
2. Each row must have exactly one instance of each digit 1-9
3. Each 3x3 cell (distinctly shown, non-overlapping) must have exactly one instance of each digit 1-9

By applying these rules to an empty cell, you can deduce which possible digits can fit in a cell. If there is only one option, then that digit must be the answer.

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
    if only one option:
        fill in cell with option
```

What does the ```for each cell``` look like? A puzzle is a 9x9 grid. Denoting a row as ```i``` and a column as ```j```, then for a puzzle ```P```, every element can represented as ```P[i][j]```.

The algorithm only applies to unsolved elements of ```P[i][j]```, so before applying each rule, check if the cell is empty.

```
for row in 1...9:
    for col in 1...9:
        if P[i][j] is empty:
            options = [1,2,3,4,5,6,7,8,9]
            options = column_check(options)
            options = row_check(options)
            options = cell_check(options)
            if length(option) == 1:
                P[i][j] = option
```

After looping through each cell, some cells should be filled in. Now what? Most likely, the puzzle will not be solved in a single round. However a cell that previously had 2 or more options may now be solvable if one of the options was filled in later in the loop.

As long as progress as being made, the solve cycle should continue. 

```
while making_progress
    for row in 1...9:
        for col in 1...9:
            if P[i][j] is empty:
                options = [1,2,3,4,5,6,7,8,9]
                options = column_check(options)
                options = row_check(options)
                options = cell_check(options)
                if length(option) == 1:
                    P[i][j] = option
```

How to quantify making progress? If the number of empty elements is less after executing the loops, progress was made.

```
making_progress = True
while making_progress
    num_unsolved = sum(P==empty)
    for row in 1...9:
        for col in 1...9:
            if P[i][j] is empty:
                options = [1,2,3,4,5,6,7,8,9]
                options = column_check(options)
                options = row_check(options)
                options = cell_check(options)
                if length(option) == 1:
                    P[i][j] = option
    if sum(P==empty) == num_unsolved:
        making_progress = False

```

## Function / class methods

### column_check

In column_check, you are given an input list of potential digits that could fit in a cell, and want to return the subset of those options based on what already exists in the column. In pseudocode:

```
def column_check(options):
    loop through elements in column:
        if element in options found, remove from options list

```

By default we had only ***options*** as an input parameter, but to loop through elements in the column, we'll need to know those elements. The input could be simply the list of elements to check, but to be more intuitive with the name, the inputs would be the entire puzzle, then the column index to check.

```
def column_check(puzzle, column_index, options):
    for element in puzzle[:,column_index]:
        if element in options:
            options.remove(element)
    return options

```

If you are familiar with list comprehension, you can condense the lines of code. The below example builds the possible list of options up instead of removing the found options:

```
def check_col(puzzle, col_idx, options):
    
    new_options = [digit for digit in options if digit not in puzzle[:,col_idx]] 
    
    return new_options
```

### row_check

### cell_check

Loop through all elements

Loop through until not making progress

### Error handling

### Debugging

## Describing

### Readme/GitHub

### LinkedIn/Resume

### Interview
