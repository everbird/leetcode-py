#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        lenn = len(nums)
        max_i = 0
        count = 0
        last = 0
        for i in range(lenn - 1):
            max_i = max(max_i, i+nums[i])
            if i == last:
                count += 1
                last = max_i

        return count


if __name__ == '__main__':
    s = Solution()
    print s.jump([2,3,1,1,4])
    print s.jump([0])
