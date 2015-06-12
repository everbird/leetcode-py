#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def compare(a, b):
            if a+b > b+a:
                return 1
            elif a+b < b+a:
                return -1
            else:
                return 0

        nums = map(str, nums)
        nums.sort(cmp=compare, reverse=True)
        while nums[0] == '0' and len(nums) > 1:
            nums = nums[1:]

        return ''.join(nums)


if __name__ == '__main__':
    s = Solution()
    print s.largestNumber([3, 30, 34, 5, 9])
    print s.largestNumber([0, 0])
