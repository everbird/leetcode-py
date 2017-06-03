#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        pivot = search_pivot(nums)
        a = binary_search(nums[:pivot+1], target)
        if a != -1:
            return a
        b = binary_search(nums[pivot+1:], target)
        if b != -1:
            return pivot + b + 1

        return -1

def search_pivot(nums):
    len_n = len(nums)
    i = 0
    while i < len_n - 1 and nums[i] < nums[i+1]:
        i += 1

    return i

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
    a = [4,5,6,7,0,1,2,3]
    r = s.search(a, 6)
    print r

    a = [3,1]
    r = s.search(a, 1)
    print r

    a = [1,]
    r = s.search(a, 1)
    print r

    a = [1,3]
    r = s.search(a, 3)
    print r

    a = [4,5,6,7,8,1,2,3]
    r = s.search(a, 8)
    print r
