#!/usr/bin/env python3

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = 0
        e = n - 1
        rs = [0] * n
        while s <= e:
            if abs(nums[s]) > abs(nums[e]):
                rs[n-1] = nums[s]*nums[s]
                s += 1
            else:
                rs[n-1] = nums[e]*nums[e]
                e -= 1
            n -= 1

        return rs
