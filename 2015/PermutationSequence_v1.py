#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        d = 1
        for i in range(2, n):
            d *= i

        if k > d * n:
            return

        r = ''
        nums = ''.join(map(str, range(1, n+1)))
        for i in range(n - 1):
            pos = (k-1) / d
            r += nums[pos]
            nums = nums[:pos] + nums[pos+1:]
            k %= d
            if k == 0:
                return r + nums[::-1]

            d /= (n - 1 - i)

        return r + nums[0]


if __name__ == '__main__':
    s = Solution()
    print s.getPermutation(9, 273815)
