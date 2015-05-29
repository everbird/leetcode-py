#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        if not board:
            return

        lenh = len(board)
        lenw = len(board[0])
        self.get_safe_os(board)
        for j in range(lenh):
            for i in range(lenw):
                if board[j][i] == 'O':
                    board[j][i] = 'X'
                elif board[j][i] == 'B':
                    board[j][i] = 'O'

    def get_safe_os(self, board):
        lenh = len(board)
        lenw = len(board[0])
        for j in range(lenh):
            if board[j][0] == 'O':
                board[j][0] = 'B'
                self.expand(board, [(j, 0)])

            if board[j][lenw-1] == 'O':
                board[j][lenw-1] = 'B'
                self.expand(board, [(j, lenw-1)])

        for i in range(lenw):
            if board[0][i] == 'O':
                board[0][i] = 'B'
                self.expand(board, [(0, i)])

            if board[lenh-1][i] == 'O':
                board[lenh-1][i] = 'B'
                self.expand(board, [(lenh-1, i)])

    def expand(self, board, safes):
        lenh = len(board)
        lenw = len(board[0])
        while safes:
            y, x = safes.pop()
            if y+1 < lenh and board[y+1][x] == 'O':
                board[y+1][x] = 'B'
                safes = [(y+1, x)] + safes

            if y-1 >= 0 and board[y-1][x] == 'O':
                board[y-1][x] = 'B'
                safes = [(y-1, x)] + safes

            if x+1 < lenw and board[y][x+1] == 'O':
                board[y][x+1] = 'B'
                safes = [(y, x+1)] + safes

            if x-1 >= 0 and board[y][x-1] == 'O':
                board[y][x-1] = 'B'
                safes = [(y, x-1)] + safes


if __name__ == '__main__':
    s = Solution()
    b = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X'],
    ]
    s.solve(b)
    print b
