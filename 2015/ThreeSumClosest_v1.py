#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        r = sum(nums[:3])
        lenn = len(nums)
        nums.sort()
        for i, n in enumerate(nums):
            b = i + 1
            e = lenn - 1
            while b < e:
                t = n + nums[b] + nums[e]
                if abs(r - target) > abs(t - target):
                    r = t

                if t > target:
                    e -= 1
                elif t < target:
                    b += 1
                else:
                    return t

        return r


if __name__ == '__main__':
    a = [-1, 2, 1, -4]
    s = Solution()
    r = s.threeSumClosest(a, 1)
    print r
