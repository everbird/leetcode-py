#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def twoSum(self, nums, target):
        for i, a in enumerate(nums):
            if a > target:
                break

            for j, b in enumerate(nums[i+1:]):
                if b > target:
                    break

                if (a + b) == target:
                    return i+1, i+j+2

        return 0, 0


if __name__ == '__main__':
    input_nums = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72]
    target = 32
    s = Solution()
    x, y = s.twoSum(input_nums, target)
    print x, y
