#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
            return 0

        lenn = len(nums)
        if lenn == 1:
            return nums[0]
        return max(
            self.rob_house(nums, 0, lenn - 2),
            self.rob_house(nums, 1, lenn - 1)
        )

    def rob_house(self, nums, b, e):
        include = 0
        exclude = 0
        for i in range(b, e+1):
            _i = include
            include = exclude + nums[i]
            exclude = max(_i, exclude)

        return max(include, exclude)


if __name__ == '__main__':
    s = Solution()
    print s.rob([1,3,4,7,9,5,3,6,8])
