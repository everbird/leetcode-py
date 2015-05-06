#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        p = nums[0]
        count = 1
        for n in nums[1:]:
            if p != n:
                nums[count] = n
                count += 1
            p = n

        return count


if __name__ == '__main__':
    a = [1,1,2]
    s = Solution()
    r = s.removeDuplicates(a)
    print r, a
