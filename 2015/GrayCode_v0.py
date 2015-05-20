#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        if n == 0:
            return [0]

        if n == 1:
            return [0, 1]

        r = []
        items = self.grayCode(n - 1)
        r = items[:]

        k = 1 << (n - 1)
        for i in items[::-1]:
            r.append(k+i)

        return r

if __name__ == '__main__':
    s = Solution()
    print s.grayCode(2)
    print s.grayCode(3)
    print s.grayCode(4)
