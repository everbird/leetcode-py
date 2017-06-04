#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        cnt = 0
        pre = None
        index = 0
        for n in nums:
            if pre != n:
                cnt += 1
                pre = n
                nums[index] = n
                index += 1
        return cnt


if __name__ == '__main__':
    a = [1,1,2]
    s = Solution()
    r = s.removeDuplicates(a)
    print r, a
