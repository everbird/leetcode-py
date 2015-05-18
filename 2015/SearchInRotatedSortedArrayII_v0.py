#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):
        lenn = len(nums)
        pivot = 0
        for i in range(lenn - 1):
            if nums[i] > nums[i + 1]:
                pivot = i + 1
                break

        r = binary_search(nums[:pivot], target)
        if r != -1:
            return True

        r = binary_search(nums[pivot:], target)
        r = pivot + r if r != -1 else -1
        return r != -1


def binary_search(nums, target):
    b = 0
    e = len(nums) - 1
    while b <= e:
        mid = (b + e) // 2
        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            e = mid - 1
        else:
            b = mid + 1

    return -1


if __name__ == '__main__':
    s = Solution()
    print s.search([4, 5, 6, 6, 7, 0, 1, 2, 2], 6)
    print s.search([4, 5, 6, 6, 7, 0, 1, 2, 2], 7)
    print s.search([4, 5, 6, 6, 7, 0, 1, 2, 2], 9)
    print s.search([3, 1], 1)
