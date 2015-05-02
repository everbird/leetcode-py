#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def twoSum(self, nums, target):
        for i, a in enumerate(nums):
            if a > target:
                break

            b = target - a
            j = self.binary_search(nums[i+1:], b)
            if j > 0:
                return i+1, i+j+2

        return 0, 0

    def binary_search(self, data, target):
        length = len(data)
        mid = length / 2
        n = data[mid]
        if n == target:
            return mid
        elif n > target:
            return self.binary_search(data[:mid], target)
        elif n < target:
            return mid + 1 + self.binary_search(data[mid+1:], target)


if __name__ == '__main__':
    input_nums = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72]
    target = 32
    s = Solution()
    x, y = s.twoSum(input_nums, target)
    print x, y
