#!/usr/bin/eni python
# encoding: utf-8

from collections import defaultdict


class Solution(object):
    def subarraySum(self, nums, k):
        n = len(nums)
        cnt = 0
        s = 0
        targets = defaultdict(int)
        targets[0] = 1
        for i in range(n):
            s += nums[i]
            pre_s = s - k
            cnt += targets[pre_s]
            targets[s] += 1

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
