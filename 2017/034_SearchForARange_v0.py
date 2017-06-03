#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        return binary_search(nums, target)


def binary_search(nums, target):
    len_n = len(nums)
    b = 0
    e = len_n - 1
    while b <= e:
        mid = s_mid = e_mid = (b + e) // 2

        while e_mid + 1 <= e and nums[e_mid] == nums[e_mid+1]:
            e_mid += 1

        while s_mid - 1 >= b and nums[s_mid] == nums[s_mid-1]:
            s_mid -= 1

        if nums[mid] == target:
            return [s_mid, e_mid]
        elif nums[mid] > target:
            e = s_mid - 1
        else:
            b = e_mid + 1

    return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    a = [5, 7, 7, 8, 8, 10]
    r = s.searchRange(a, 8)
    print r

    a = [1]
    r = s.searchRange(a, 0)
    print r
