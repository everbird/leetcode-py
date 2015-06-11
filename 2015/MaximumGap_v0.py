#!/usr/bin/env python
# encoding: utf-8

import math

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, nums):
        lenn = len(nums)
        if not lenn or lenn == 1:
            return 0

        imin = min(nums)
        imax = max(nums)
        bsize = int(math.ceil((imax - imin) * 1.0 / (lenn - 1)))
        bcount = ((imax - imin) / bsize) + 1
        buckets = [None] * bcount
        for i in range(len(nums)):
            n = nums[i]
            bindex = (n - imin) / bsize
            b = buckets[bindex]
            _max = max(buckets[bindex][0], n) if b else n
            _min = min(buckets[bindex][1], n) if b else n
            buckets[bindex] = (_max, _min)

        max_d = 0
        pb = None
        for i in range(bcount):
            b = buckets[i]
            if b:
                if pb:
                    d = b[1] - pb[0]
                    if max_d < d:
                        max_d = d

                pb = b

        return max_d


if __name__ == '__main__':
    s = Solution()
    print s.maximumGap([1,2,3,4,6,7])
    print s.maximumGap([])
    print s.maximumGap([1,2])
    print s.maximumGap([100,3,2,1]), 97
    print s.maximumGap([10]), 0
    print s.maximumGap([1,10000000]), 9999999
    print s.maximumGap([3,6,9,1]), 3
