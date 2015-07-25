#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        nums.sort()
        r = [[]]
        lenn = len(nums)
        i = 0
        while i < lenn:
            n = nums[i]
            count = 1
            while i+1 < lenn and n == nums[i+1]:
                i += 1
                count += 1

            lenr = len(r)
            for j in range(lenr):
                item = r[j][:]
                for k in range(count):
                    item.append(n)
                    r.append(item[:])

            i += 1

        return r


if __name__ == '__main__':
    s = Solution()
    print s.subsetsWithDup([1,2,2])
    print s.subsetsWithDup([0])
