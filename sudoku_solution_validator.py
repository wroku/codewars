"""
Task:

https://www.codewars.com/kata/529bf0e9bdf7657179000008

Sudoku Background

Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
(More info at: http://en.wikipedia.org/wiki/Sudoku)
Sudoku Solution Validator

Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
"""


# Solution:

def contains_all_digits(board):
    for sector in board:
        if set(sector) != set(range(1, 10)):
            return False
    return True

def validSolution(board):

    transposed_board = [[board[j][i] for j in range(9)] for i in range(9)]
    small_squares = [[], [], [], [], [], [], [], [], []]
    for X in range(3):
        for Y in range(3):
            for x in range(3):
                for y in range(3):
                    small_squares[X*3 + Y].append(board[X*3 + x][Y*3 + y])
    return (contains_all_digits(board) and contains_all_digits(transposed_board) and contains_all_digits(small_squares))