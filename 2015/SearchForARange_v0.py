#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        return binary_search(nums, target)


def binary_search(nums, k):
    b = 0
    lenn = len(nums)
    e = lenn - 1
    while b <= e:
        mid = (b + e) // 2
        if k == nums[mid]:
            l = r = mid
            while l >= 0 and nums[l] == k:
                l -= 1

            while r < lenn and nums[r] == k:
                r += 1

            return [l + 1, r - 1]
        elif k > nums[mid]:
            b = mid + 1
        else:
            e = mid - 1

    return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    a = [5, 7, 7, 8, 8, 10]
    r = s.searchRange(a, 8)
    print r

    a = [1]
    r = s.searchRange(a, 0)
    print r
