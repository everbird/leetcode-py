#!/usr/bin/env python
# encoding: utf-8

from collections import Counter

class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        len_y = len(board)
        len_x = len(board[0])
        for j in range(len_y):
            if not validate(board[j]):
                return False

        for i in range(len_x):
            items = [x[i] for x in board]
            if not validate(items):
                return False

        for _j in range(0, len_y, 3):
            for _i in range(0, len_x, 3):
                items = [board[j+_j][i+_i] for j in range(3) for i in range(3)]
                if not validate(items):
                    return False

        return True


def validate(items):
    c = Counter(items)
    for n, cnt in c.iteritems():
        if n == '.':
            continue
        if cnt > 1:
            return False

    return True


if __name__ == '__main__':
    s = Solution()
    a = [
        "..4...63.",
        ".........",
        "5......9.",
        "...56....",
        "4.3.....1",
        "...7.....",
        "...5.....",
        ".........",
        "........."
    ]
    print s.isValidSudoku(a)

    a = [
        "....5..1.",
        ".4.3.....",
        ".....3..1",
        "8......2.",
        "..2.7....",
        ".15......",
        ".....2...",
        ".2.9.....",
        "..4......"
    ]
    print s.isValidSudoku(a)
