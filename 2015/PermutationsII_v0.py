#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        nums.sort()
        return permute(nums)


def permute(nums):
    lenn = len(nums)

    if lenn == 1:
        return [nums]

    pre = None
    r = []
    for i in range(lenn):
        if pre != nums[i]:
            items = permute(nums[:i] + nums[i+1:])
            for item in items:
                t = [nums[i]] + item
                r.append(t)

        pre = nums[i]

    return r


if __name__ == '__main__':
    s = Solution()
    print s.permuteUnique([1,1,2])
    print s.permuteUnique([1,2])
    #print s.permuteUnique([3,3,0,0,2,3,2])
