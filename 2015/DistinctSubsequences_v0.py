#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        lens = len(s)
        lent = len(t)
        if lent > lens:
            return 0

        li = [0] * (lens+1)
        d = [li[:] for i in range(lent+1)]

        for i in range(lens+1):
            d[0][i] = 1

        for j in range(1, lent+1):
            for i in range(1, lens+1):
                if s[i-1] == t[j-1]:
                    d[j][i] = d[j][i-1] + d[j-1][i-1]
                else:
                    d[j][i] = d[j][i-1]

        return d[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print s.numDistinct('rabbbit', 'rabbit')
    print s.numDistinct('rabbbit', '')
    print s.numDistinct('', '')
    print s.numDistinct('', 'aaa')
    print s.numDistinct('aabb', 'ab')
