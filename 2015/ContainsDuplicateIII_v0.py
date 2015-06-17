#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        for i in range(len(nums)):
            _nums = nums[i+1:i+k+1]
            n = nums[i]
            for j in range(len(_nums)):
                m = _nums[j]
                if abs(m - n) <= t:
                    return True

        return False

    def containsNearbyAlmostDuplicate_E(self, nums, k, t):
        m = {}
        for i, n in enumerate(nums):
            j = m.get(n)
            for x in range(n-t, n+t+1):
                m[x] = i

            if j is not None:
                if (i - j) <= k:
                    return True

        return False


if __name__ == '__main__':
    s = Solution()
    print s.containsNearbyAlmostDuplicate([1,5,8,9,16], 1, 1)
    print s.containsNearbyAlmostDuplicate([1,5,8,16], 1, 3)
    print s.containsNearbyAlmostDuplicate([0,2147483647], 1, 2147483647)
    print s.containsNearbyAlmostDuplicate([-3,3], 2, 4)
    print s.containsNearbyAlmostDuplicate([4,2], 2, 1)
