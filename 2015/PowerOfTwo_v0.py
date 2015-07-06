#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if not n:
            return False
        return not ((n - 1) & n)


if __name__ == '__main__':
    s = Solution()
    print s.isPowerOfTwo(8)
    print s.isPowerOfTwo(9)
    print s.isPowerOfTwo(0)
    print s.isPowerOfTwo(1)
