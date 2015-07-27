#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        deque = []
        result = []
        lenn = len(nums)
        if lenn < k:
            return [max(nums)]

        for i in range(lenn):
            n = nums[i]
            r = []
            for x in deque:
                if nums[x] >= n and x > i-k:
                    r.append(x)
            r.append(i)
            deque = r
            if i >= (k - 1):
                result.append(nums[deque[0]])
        return result


if __name__ == '__main__':
    s = Solution()
    print s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
    print s.maxSlidingWindow([1,3], 3)
    print s.maxSlidingWindow([1,-1], 1)
