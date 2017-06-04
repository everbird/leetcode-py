#!/usr/bin/env python
# encoding: utf-8


"""
My idea is for an array:

Start from its last element, traverse backward to find the first one with index i that satisfy num[i-1] < num[i]. So, elements from num[i] to num[n-1] is reversely sorted.
To find the next permutation, we have to swap some numbers at different positions, to minimize the increased amount, we have to make the highest changed position as high as possible. Notice that index larger than or equal to i is not possible as num[i,n-1] is reversely sorted. So, we want to increase the number at index i-1, clearly, swap it with the smallest number between num[i,n-1] that is larger than num[i-1]. For example, original number is 121543321, we want to swap the '1' at position 2 with '2' at position 7.
The last step is to make the remaining higher position part as small as possible, we just have to reversely sort the num[i,n-1]

REF: https://leetcode.com/discuss/8472/share-my-o-n-time-solution
"""

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        len_n = len(nums)
        index = len_n - 1
        while index > 0 and nums[index - 1] >= nums[index]:
            index -= 1

        if index == 0:
            nums.reverse()
            return

        peak = index
        for i in range(len_n - 1, peak - 1, -1):
            if nums[i] > nums[peak - 1]:
                nums[i], nums[peak - 1] = nums[peak - 1], nums[i]
                break

        inplace_reverse(nums, peak, len_n - 1)


def inplace_reverse(nums, b, e):
    while b < e:
        nums[b], nums[e] = nums[e], nums[b]
        b += 1
        e -= 1


if __name__ == '__main__':
    s = Solution()

    a = [1,2,3]
    s.nextPermutation(a)
    print a

    a = [3,2,1]
    s.nextPermutation(a)
    print a

    a = [1,1,5]
    s.nextPermutation(a)
    print a

    a = [5,1,1]
    s.nextPermutation(a)
    print a
