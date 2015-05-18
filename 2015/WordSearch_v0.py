#!/usr/bin/env python
# encoding: utf-8


import copy


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
        lens = len(word)
        if lenw * lenh < lens:
            return False

        li = [0] * lenw
        b = [li[:] for i in range(lenh)]
        d = [copy.deepcopy(b) for i in range(lens)]
        for k in range(lens):
            for j in range(lenh):
                for i in range(lenw):
                    if k == 0:
                        d[0][j][i] = int(board[j][i] == word[0])
                    else:
                        if (d[k-1][j][i] == 0
                                or (d[k-1][j][i] == k and word[k] == word[k-1])):

                            if (board[j][i] == word[k]
                                and ((j > 0 and d[k-1][j-1][i])
                                     or (j + 1 < lenh and d[k-1][j+1][i])
                                     or (i > 0 and d[k-1][j][i-1])
                                     or (i + 1 < lenw and d[k-1][j][i+1])
                                     )):
                                d[k][j][i] = k+1
                        else:
                            d[k][j][i] = d[k-1][j][i]

        #for k in range(lens):
            #for j in range(lenh):
                #print d[k][j]

            #print '----'

        for j in range(lenh):
            for i in range(lenw):
                if d[lens-1][j][i] == lens:
                    return True

        return False


if __name__ == '__main__':
    s = Solution()
    print s.exist([
        "ABCE",
        "SFCS",
        "ADEE"
    ], 'ABCCED')

    print s.exist([
        "ABCE",
        "SFCS",
        "ADEE"
    ], 'SEE')

    print s.exist([
        "ABCE",
        "SFCS",
        "ADEE"
    ], 'ABCB')

    print s.exist([
        "AA"
    ], 'AA')
