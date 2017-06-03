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
    if k == 2:
        r = []
        d = {}
        pre = None
        for num in nums:
            if pre == num:
                continue
            expect = target - num
            if d.get(expect):
                r.append([expect, num])
                pre = num
            d[num] = True

        return r

    r = []
    pre = None
    for i, n in enumerate(nums[:-k+1]):
        if pre == n:
            continue

        rs = kSum(nums[i+1:], target - n, k - 1)
        for result in rs:
            r.append([n] + result)
        pre = n
    return r


if __name__ == '__main__':
    #a = [1, 0, -1, 0, -2, 2]
    #a = [5,5,3,5,1,-5,1,-2]
    a = [0,0,0,0]
    s = Solution()
    r = s.fourSum(a, 0)
    print r

    a = [0,0,0]
    r = kSum(a, 0, 3)
    print r
