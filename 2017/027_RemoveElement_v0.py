#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        index = 0
        for n in nums:
            if n != val:
                nums[index] = n
                index += 1
        return index


if __name__ == '__main__':
    a = [1,3,2,3,2]
    s = Solution()
    r = s.removeElement(a, 3)
    print r, a
