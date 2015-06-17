#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        m = {}
        for i, n in enumerate(nums):
            _i = m.get(n)
            m[n] = i
            if _i is not None:
                m[n] = i
                if (i - _i) <= k:
                    return True

        return False


if __name__ == '__main__':
    s = Solution()
    print s.containsNearbyDuplicate([1,3,4,2,5,6,3,1,9], 5)
    print s.containsNearbyDuplicate([1], 5)
    print s.containsNearbyDuplicate([], 0)
    print s.containsNearbyDuplicate([1,0,1,1], 1)
