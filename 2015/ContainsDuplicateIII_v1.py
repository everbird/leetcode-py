#!/usr/bin/env python
# encoding: utf-8


from collections import OrderedDict


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if not k:
            return False

        d = OrderedDict()
        for n in nums:
            key = n if t == 0 else n // t # Hash n to key, if n' has the same key, diff between n' and n won't be greater than t, for key+1, key-1, it might be. So key+1, key-1 need to check
            for m in (d.get(key-1), d.get(key), d.get(key+1)):
                if m is not None and abs(m - n) <= t:
                    return True

            if len(d) == k:
                d.popitem(False) # Remove head of OrderedDict

            d[key] = n

        return False


if __name__ == '__main__':
    s = Solution()
    print s.containsNearbyAlmostDuplicate([1,5,8,9,16], 1, 1)
    print s.containsNearbyAlmostDuplicate([1,5,8,16], 1, 3)
    print s.containsNearbyAlmostDuplicate([0,2147483647], 1, 2147483647)
    print s.containsNearbyAlmostDuplicate([-3,3], 2, 4)
    print s.containsNearbyAlmostDuplicate([4,2], 2, 1)
    print s.containsNearbyAlmostDuplicate([0], 0, 0)
