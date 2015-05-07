#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        lenn = len(nums)
        pivot = 0
        for i in range(lenn - 1):
            if nums[i] > nums[i + 1]:
                pivot = i + 1

        r = binary_search(nums[:pivot], target)
        if r != -1:
            return r

        r = binary_search(nums[pivot:], target)
        return pivot + r if r != -1 else -1


def binary_search(nums, k):
    lenn = len(nums)
    b = 0
    e = lenn - 1
    while b <= e:
        mid = (e + b) // 2

        if k == nums[mid]:
            return mid
        elif k > nums[mid]:
            b = mid + 1
        else:
            e = mid - 1

    return -1


if __name__ == '__main__':
    s = Solution()
    #a = [4,5,6,7,0,1,2,3]
    #r = s.search(a, 2)
    #print r

    a = [3,1]
    r = s.search(a, 0)
    print r
