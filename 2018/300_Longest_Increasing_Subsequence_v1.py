#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        r = 0
        for i in range(n):
            seqs = lis(nums, i, n-1)
            for seq in seqs:
                r = max(r, len(seq))

        return r


def lis(nums, start, end):
    if start == end:
        return [[nums[start]]]
    elif end < start:
        return []

    r = []
    seqs = lis(nums, start, end-1)
    for seq in seqs:
        if seq[-1] < nums[end]:
            r.append(seq+[nums[end]])

        r.append(seq)

    return r


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [10,9,2,5,3,7,101,18],
            4
        ),
        (
            [10,9,2,5,3,4],
            3
        ),
    ]
    f = s.lengthOfLIS
    for input_args, expected in tests:
        s.cache = {}

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
