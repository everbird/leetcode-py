#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        if not board:
            return False

        lenh = len(board)
        lenw = len(board[0])
        if lenh*lenw < len(word):
            return False

        for j in range(lenh):
            for i in range(lenw):
                if self.nextstep(j, i, board, word, 0):
                    return True
        return False

    def nextstep(self, y, x, board, word, index):
        lens = len(word)
        lenh = len(board)
        lenw = len(board[0])

        if board[y][x] == word[index]:
            index += 1
            board[y][x] = ''
            if ( lens == index
                or ((y-1) >= 0 and self.nextstep(y-1, x, board, word, index))
                or ((y+1) < lenh and self.nextstep(y+1, x, board, word, index))
                or ((x-1) >= 0 and self.nextstep(y, x-1, board, word, index))
                or ((x+1) < lenw and self.nextstep(y, x+1, board, word, index))
            ):
                return True
            index -= 1
            board[y][x] = word[index]


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
