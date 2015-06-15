#!/usr/bin/env python
# encoding: utf-8

from collections import defaultdict


class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def __init__(self):
        self.root = TrieNode()
        self.result = []

    def insert(self, word):
        p = self.root
        for c in word:
            p = p.children[c]
        p.is_word = True

    def findWords(self, board, words):
        for word in words:
            self.insert(word)

        lenh = len(board)
        lenw = len(board[0])
        for j in range(lenh):
            for i in range(lenw):
                self.dfs(self.root, board, j, i, '')

        return self.result

    def dfs(self, node, board, y, x, word):
        lenh = len(board)
        lenw = len(board[0])

        if node.is_word:
            self.result.append(word)
            node.is_word = False

        if 0 <= y < lenh and 0 <= x < lenw:
            c = board[y][x]
            r = node.children.get(c)
            if r is not None:
                word += c
                board[y][x] = None
                self.dfs(r, board, y-1, x, word)
                self.dfs(r, board, y+1, x, word)
                self.dfs(r, board, y, x-1, word)
                self.dfs(r, board, y, x+1, word)
                board[y][x] = c


if __name__ == '__main__':
    s = Solution()
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    print s.findWords(board, ["oath","pea","eat","rain"])
