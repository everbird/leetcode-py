#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)
        if len1 > len2:
            return self.minDistance(word2, word1)

        if len1 == 0:
            return len2

        li = [0] * (len1+1)
        d = [li[:] for i in range(len2+1)]

        for i in range(len1+1):
            d[0][i] = i

        for j in range(len2+1):
            d[j][0] = j

        for i in range(1, len1+1):
            for j in range(1, len2+1):
                r1 = 1 + d[j][i - 1]
                r2 = 1 + d[j - 1][i]
                cost = int(word1[i-1] != word2[j-1])
                r3 = cost + d[j - 1][i - 1]
                d[j][i] = min(r1, r2, r3)

        return d[len2][len1]


def printm(m):
    for li in m:
        print li


if __name__ == '__main__':
    s = Solution()
    print s.minDistance('abc', 'efg')
    print s.minDistance('', 'efg')
    print s.minDistance('ba', 'ab')
    print s.minDistance('sea', 'ate')
    print s.minDistance('sea', 'eat')
    print s.minDistance("zoologicoarchaeologist", "zoogeologist")
    print s.minDistance("zoologicoarcha", "zoog")
    print s.minDistance("ogloi", "oo")
