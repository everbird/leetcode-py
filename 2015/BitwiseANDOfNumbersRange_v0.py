#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        r = 0
        flag = False
        for i in range(31, -1, -1):
            bm = (1<<i) & m
            bn = (1<<i) & n
            if flag:
                r = r<<1
            elif bn == bm:
                r = r<<1 | bool(bn)
            else:
                flag = True
                r = r<<1

        return r


if __name__ == '__main__':
    s = Solution()
    print s.rangeBitwiseAnd(5, 7)
