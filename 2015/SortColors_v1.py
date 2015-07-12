#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        if not nums:
            return

        lenn = len(nums)
        rp = 0
        bp = lenn - 1
        while nums[rp] == 0:
            rp += 1
            if rp == lenn:
                return

        while nums[bp] == 2:
            bp -= 1
            if bp < 0:
                return

        i = rp
        while i <= bp:
            while rp <= i <= bp and nums[i] in (0, 2):
                if nums[i] == 0:
                    nums[i], nums[rp] = nums[rp], nums[i]
                    rp += 1
                elif nums[i] == 2:
                    nums[i], nums[bp] = nums[bp], nums[i]
                    bp -= 1

            i += 1


if __name__ == '__main__':
    s = Solution()
    a = [0,1,2,1,0,2,1,2,1]
    s.sortColors(a)
    print a

    a = [1,0,1]
    s.sortColors(a)
    print a

    a = []
    s.sortColors(a)
    print a

    a = [0,0,0,0,0,0]
    s.sortColors(a)
    print a

    a = [1,1,1,1,1,1,1]
    s.sortColors(a)
    print a

    a = [2,2,2,2,2,2]
    s.sortColors(a)
    print a

    a = [1, 2, 0]
    s.sortColors(a)
    print a
