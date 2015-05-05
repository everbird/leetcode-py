#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        nums.sort()
        return kSum(nums, target, 4)


def kSum(nums, target, k):
    r = []
    if k == 2:
        b = 0
        e = len(nums) - 1
        while b < e:
            s = nums[b] + nums[e]
            if s == target:
                r.append((nums[b], nums[e]))
                b += 1
            elif s > target:
                e -= 1
            else:
                b += 1
    else:
        for i, n in enumerate(nums):
            ts = kSum(nums[i + 1:], target - n, k - 1)
            for t in ts:
                tt = (n, ) + t
                if tt not in r:
                    r.append(tt)

    return r


if __name__ == '__main__':
    a = [1, 0, -1, 0, -2, 2]
    s = Solution()
    r = s.fourSum(a, 0)
    print r
