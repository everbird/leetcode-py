#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        d = {}
        max_c = 0
        for i in range(len(nums)):
            n = nums[i]
            if d.get(n):
                continue
            d[n] = 1
            b = e = n

            if d.get(n+1):
                e = n + d.get(n+1)

            if d.get(n-1):
                b = n - d.get(n-1)

            d[b] = e - b + 1
            d[e] = e - b + 1

            max_c = max(max_c, e - b + 1)

        return max_c


if __name__ == '__main__':
    s = Solution()
    print s.longestConsecutive([100, 4, 200, 1, 3, 2])
    print s.longestConsecutive([-1,1,0])
    print s.longestConsecutive([1,2,0,1])
