#!/usr/bin/env python
# encoding: utf-8


from collections import defaultdict


class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums, m=2):
        lenn = len(nums)
        d = defaultdict(int)
        for n in nums:
            if n in d or len(d) < m:
                d[n] += 1
            else:
                for k, v in d.items():
                    if v == 0:
                        d.pop(k)
                    else:
                        d[k] -= 1

        for k in d:
            d[k] = 0
        for n in nums:
            if n in d:
                d[n] += 1

        r = []
        for k, v in d.iteritems():
            if v > lenn // m:
                r.append(k)

        return r[0] if m == 2 else r


if __name__ == '__main__':
    s = Solution()
    print s.majorityElement([2,1,2,1,3,1,1], 2)
