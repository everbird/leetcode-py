#!/usr/bin/eni python
# encoding: utf-8



class Solution(object):
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        if n <= 1:
            return 0

        start = 0
        end = n-1
        i = 1
        while i < n:
            pre = i-1
            if nums[pre] > nums[i]:
                start = pre
                break

            i += 1
        if i == n:
            return 0

        i = n - 1
        while i > 0:
            pre = i-1
            if nums[pre] > nums[i]:
                end = i
                break
            i -= 1

        unsorted = nums[start:end+1]
        min_v = min(unsorted)
        max_v = max(unsorted)
        left = 0
        right = n-1

        while left < right:
            if nums[left] <= min_v:
                left += 1
            elif nums[right] >= max_v:
                right -= 1
            else:
                break

        return right - left + 1 if left != right else 0



if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [2, 6, 4, 8, 10, 9, 15],
            5
        ),
        (
            [1],
            0
        ),
        (
            [1, 1],
            0
        ),
        (
            [1, 2, 3 ,4],
            0
        )
    ]
    f = s.findUnsortedSubarray
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
