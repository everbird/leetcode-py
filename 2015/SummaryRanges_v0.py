#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        r = []
        if not nums:
            return r
        lenn = len(nums)
        start = end = 0
        pre = nums[0]
        for i in range(1, lenn):
            n = nums[i]
            if (pre + 1) == n:
                end += 1
            else:
                if start == end:
                    r.append('{}'.format(nums[end]))
                else:
                    r.append('{}->{}'.format(nums[start], nums[end]))
                end += 1
                start = end
            pre = n

        if end <= lenn:
            if start == end:
                r.append('{}'.format(nums[end]))
            else:
                r.append('{}->{}'.format(nums[start], nums[end]))

        return r


if __name__ == '__main__':
    s = Solution()
    print s.summaryRanges([0,1,2,4,5,7])
