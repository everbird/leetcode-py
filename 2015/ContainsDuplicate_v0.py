#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))

    def containsDuplicate_(self, nums):
        m = {}
        for n in nums:
            if m.get(n):
                return True
            m[n] = True

        return False



if __name__ == '__main__':
    s = Solution()
    print s.containsDuplicate([1,2,3,4,5,3,7,8,9])
