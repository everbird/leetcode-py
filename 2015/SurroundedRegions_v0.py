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
        safes = self.get_safe_os(board)
        safes = self.expand(board, safes)
        for j in range(lenh):
            for i in range(lenw):
                board[j][i] = 'X'

        for y, x in safes:
            board[y][x] = 'O'

    def get_safe_os(self, board):
        lenh = len(board)
        lenw = len(board[0])
        r = []
        for j in range(lenh):
            if board[j][0] == 'O':
                r.append((j, 0))

            if board[j][lenw-1] == 'O':
                r.append((j, lenw-1))

        for i in range(lenw):
            if board[0][i] == 'O':
                r.append((0, i))

            if board[lenh-1][i] == 'O':
                r.append((lenh-1, i))

        return r

    def expand(self, board, safes):
        lenh = len(board)
        lenw = len(board[0])
        r = safes[:]
        while safes:
            y, x = safes.pop()
            if y+1 < lenh and board[y+1][x] == 'O' and (y+1, x) not in r:
                r.append((y+1, x))
                safes = [(y+1, x)] + safes

            if y-1 >= 0 and board[y-1][x] == 'O' and (y-1, x) not in r:
                r.append((y-1, x))
                safes = [(y-1, x)] + safes

            if x+1 < lenw and board[y][x+1] == 'O' and (y, x+1) not in r:
                r.append((y, x+1))
                safes = [(y, x+1)] + safes

            if x-1 >= 0 and board[y][x-1] == 'O' and (y, x-1) not in r:
                r.append((y, x-1))
                safes = [(y, x-1)] + safes

        return r


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
