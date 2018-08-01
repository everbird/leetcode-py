#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def canPartition(self, nums):
        s = sum(nums)
        if s % 2:
            return False

        target = s // 2
        return find_sum(nums, target)


def find_sum(nums, target):
    n = len(nums)
    dp = [[False] * (target+1) for i in range(n+1)]
    dp[0][0] = True
    for i in range(n+1):
        for j in range(target+1):
            if 0 < (j+nums[i-1]) <= target:
                dp[i][j+nums[i-1]] |= dp[i-1][j]
            dp[i][j] |= dp[i-1][j]

    return dp[n][target]




if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [1, 5, 11, 5],
            True
        ),
        (
            [1, 2, 3, 5],
            False
        )
    ]
    f = s.canPartition
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
