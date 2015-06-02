#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        return reduce(lambda x, y: x ^ y, nums, 0)


if __name__ == '__main__':
    s = Solution()
    print s.singleNumber([1,2,3,2,1])
    print s.singleNumber([4,1,4,2,3,2,1])
