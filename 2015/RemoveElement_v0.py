#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        count = 0
        for n in nums:
            if n != val:
                nums[count] = n
                count += 1

        return count


if __name__ == '__main__':
    a = [1,3,2,3,2]
    s = Solution()
    r = s.removeElement(a, 3)
    print r, a
