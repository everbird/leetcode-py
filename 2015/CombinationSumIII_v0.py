#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        result = []
        array = []
        self.comb(k, n, array, result)
        return result

    def comb(self, k, n, array, result):
        if n == 0 and len(array) == k:
            result.append(array[:])
            return

        last = array[-1] if array else 0
        for i in range(last+1, 10):
            array.append(i)
            if n-i >= 0:
                self.comb(k, n-i, array, result)
            array.pop()


if __name__ == '__main__':
    s = Solution()
    print s.combinationSum3(3, 7)
    print '-' * 6
    print s.combinationSum3(3, 9)
