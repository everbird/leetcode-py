#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        d = {}
        for i in range(len(nums)):
            n = nums[i]
            d[n] = True

        max_c = 0
        for i in range(len(nums)):
            count = 0
            n = nums[i]
            while d.get(n):
                d.pop(n)
                n -= 1
                count += 1

            m = nums[i]+1
            while d.get(m):
                d.pop(m)
                m += 1
                count += 1

            if max_c < count:
                max_c = count

        return max_c


if __name__ == '__main__':
    s = Solution()
    print s.longestConsecutive([100, 4, 200, 1, 3, 2])
    print s.longestConsecutive([-1,1,0])
