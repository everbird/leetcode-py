#!/usr/bin/env python
# encoding: utf-8

import copy

class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        r = []
        for word in words:
            pos = self.find(board, word)
            for y, x in pos:
                b = copy.deepcopy(board)
                if self.fill(b, y, x, word):
                    r.append(word)
                    break

        return r

    def find(self, board, word):
        lenh = len(board)
        lenw = len(board[0])
        for j in range(lenh):
            for i in range(lenw):
                if board[j][i] == word[0]:
                    yield j, i

        raise StopIteration

    def fill(self, b, y, x, word):
        if not word:
            return True

        if b[y][x] == '$' or b[y][x] != word[0]:
            return False

        b[y][x] = '$'
        lenh = len(b)
        lenw = len(b[0])
        if y-1 >= 0:
            if self.fill(b, y-1, x, word[1:]):
                return True

        if y+1 < lenh:
            if self.fill(b, y+1, x, word[1:]):
                return True

        if x-1 >= 0:
            if self.fill(b, y, x-1, word[1:]):
                return True

        if x+1 < lenw:
            if self.fill(b, y, x+1, word[1:]):
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    print s.findWords(board, ["oath","pea","eat","rain"])
