#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        if not board:
            return False

        for li in board:
            if not is_unique(li):
                return False

        for i in range(9):
            t = [x[i] for x in board]
            if not is_unique(t):
                return False

        for i in range(3):
            for j in range(3):
                nums = []
                for m in range(3):
                    for n in range(3):
                        nums.append(board[i * 3 + m][j * 3 + n])

                if not is_unique(nums):
                    return False

        return True


def is_unique(nums):
    d = {}
    for c in nums:
        if c != '.' and d.get(c):
            return False

        d[c] = True

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
