#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums.sort()
        r = []
        len_n = len(nums)
        pre = None
        for i, target in enumerate(nums[:-2]):
            if target == pre:
                continue

            results = self.twoSum(nums[i+1:], -target)

            if results:
                for x in reversed(results):
                    r.append((target, x[0], x[1]))

            pre = target

        return r

    def twoSum(self, nums, target):
        r = []
        d = {}
        for i, n in enumerate(nums):
            expect =  target - n
            if d.get(expect):
                if (expect, n) not in r:
                    r.append((expect, n))

            d[n] = True

        return r


if __name__ == '__main__':
    a = [1,2,3,7,5,9,-1,-8,-3, 10]
    #a = [0,0,0]
    #a = [0,0,0,0]
    s = Solution()
    r = s.threeSum(a)
    print r
