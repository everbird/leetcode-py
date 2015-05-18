#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        if not word:
            return False

        if not board:
            return False

        lenw = len(board[0])
        lenh = len(board)
        for j in range(lenh):
            for i in range(lenw):
                if self._exist(board, word, i, j):
                    return True

        return False

    def _exist(self, board, word, x, y):
        lenw = len(board[0])
        lenh = len(board)

        if word[0] == board[y][x]:
            if not word[1:]:
                return True
            board[y][x] = ''
            if y > 0 and self._exist(board, word[1:], x, y-1):
                return True
            elif y < (lenh-1) and self._exist(board, word[1:], x, y+1):
                return True
            elif x > 0 and self._exist(board, word[1:], x-1, y):
                return True
            elif x < (lenw-1) and self._exist(board, word[1:], x+1, y):
                return True
            board[y][x] = word[0]
            return False
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print s.exist([
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ], 'ABCCED')

    print s.exist([
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ], 'SEE')

    print s.exist([
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ], 'ABCB')

    print s.exist([
        ["A", "A"]
    ], 'AA')

    print s.exist([
        ["A",]
    ], 'A')
