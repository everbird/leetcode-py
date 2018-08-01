#!/usr/bin/eni python
# encoding: utf-8

class Solution(object):
    def subarraySum(self, nums, k):
        n = len(nums)
        cnt = 0
        for j in range(1, n+1):
            for i in range(j):
                if sum(nums[i:j]) == k:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                [1,1,1],
                2
            ),
            2
        ),
    ]
    f = s.subarraySum
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
