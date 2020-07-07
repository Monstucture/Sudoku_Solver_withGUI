import random


def random_board():
    grid = [[0 for x in range(9)] for y in range(9)]

    for i in range(9):
        for j in range(9):
            grid[i][j] = 0

    for i in range(30):
        # choose random numbers
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1, 10)
        while not CheckValid(grid, row, col, num) or grid[row][col] != 0:  # if taken or not valid reroll
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1, 10)
        grid[row][col] = num
    return grid


def CheckValid(grid, row, col, num):
    # check if in row
    valid = True
    # check row and collumn
    for x in range(9):
        if grid[x][col] == num:
            valid = False
    for y in range(9):
        if grid[row][y] == num:
            valid = False
    rowsection = row // 3
    colsection = col // 3
    for x in range(3):
        for y in range(3):
            # check if section is valid
            if grid[rowsection * 3 + x][colsection * 3 + y] == num:
                valid = False
    return valid
