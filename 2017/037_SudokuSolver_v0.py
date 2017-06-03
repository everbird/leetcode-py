#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        solve(board)


def solve(board):
    if is_solved(board):
        return True

    x, y = find_unassigned(board)
    for n in range(1, 10):
        ch = str(n)
        board[y][x] = ch
        if check_row(board, y, ch) and check_column(board, x, ch) and check_square(board, x, y, ch) and solve(board):
            return True

        board[y][x] = '.'
    return False

def is_solved(board):
    for row in board:
        if '.' in row:
            return False
    return True

def find_unassigned(board):
    len_y = len(board)
    len_x = len(board[0])
    for y in range(len_y):
        for x in range(len_x):
            if board[y][x] == '.':
                return x, y
    return -1, -1

def check_items(items, ch):
    d = {}
    for item in items:
        if item != '.' and d.get(item):
            return False
        d[item] = True
    return True

def check_row(board, y, ch):
    row = board[y]
    return check_items(row, ch)

def check_column(board, x, ch):
    items = [row[x] for row in board]
    return check_items(items, ch)

def check_square(board, x, y, ch):
    items = []
    base_x = x // 3
    base_y = y // 3
    for j in range(3):
        _j = j + base_y*3
        for i in range(3):
            _i = i + base_x*3
            items.append(board[_j][_i])
    return check_items(items, ch)


if __name__ == '__main__':
    a = [
        [".", ".", "9", "7", "4", "8", ".", ".", "."],
        ["7", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "2", ".", "1", ".", "9", ".", ".", "."],
        [".", ".", "7", ".", ".", ".", "2", "4", "."],
        [".", "6", "4", ".", "1", ".", "5", "9", "."],
        [".", "9", "8", ".", ".", ".", "3", ".", "."],
        [".", ".", ".", "8", ".", "3", ".", "2", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "6"],
        [".", ".", ".", "2", "7", "5", "9", ".", "."]
    ]
    #a = [
        #['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        #['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        #['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        #['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        #['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        #['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        #['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        #['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        #['.', '.', '.', '.', '8', '.', '.', '7', '9']
    #]
    s = Solution()
    s.solveSudoku(a)
    print a
