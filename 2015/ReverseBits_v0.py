#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        r = 0
        for i in range(32):
            bit = (1<<i) & n
            r = (r<<1) | bool(bit)

        return r


if __name__ == '__main__':
    s = Solution()
    print s.reverseBits(43261596)
