#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0

        if sum(nums) < s:
            return 0

        lenn = len(nums)
        if sum(nums) == s:
            return lenn

        minl = lenn+1
        sums = [sum(nums[i:]) for i in range(lenn)]
        for i in range(lenn):
            if sums[i] >= s:
                _len = lenn - i
                _sums = sums[i+1:]
                target = sums[i] - s
                index = self.binary_search(_sums, target)
                if index is None:
                    minl = min(minl, _len)
                elif minl > index+1:
                    minl = index+1

        return minl


    def binary_search(self, sums, target):
        if not sums:
            return

        if target < sums[-1]:
            return

        b = 0
        e = len(sums) - 1
        while b <= e:
            mid = (b+e) // 2
            if sums[mid] <= target:
                e = mid - 1
            else:
                b = mid + 1

        return mid


if __name__ == '__main__':
    s = Solution()
    print s.minSubArrayLen(7, [2,3,1,2,4,3])
    print s.minSubArrayLen(70, [2,3,1,2,4,3])
    print s.minSubArrayLen(4, [2,3,1,2,4,3])
    print s.minSubArrayLen(15, [5,1,3 ,5,10,7,4,9,2,8])
    print s.minSubArrayLen(4, [1,4,4])
