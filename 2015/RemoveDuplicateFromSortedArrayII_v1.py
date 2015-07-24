#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        p = nums[0]
        dup_flag = False
        count = 1
        for n in nums[1:]:
            if dup_flag and p == n:
                continue

            nums[count] = n
            count += 1

            if p != n:
                dup_flag = False
            elif not dup_flag: # duplicate flag
                dup_flag = True

            p = n

        return count


if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicates([1,1,1,2,2,3])
