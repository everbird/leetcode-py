#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def maxCoins(self, nums):
        _nums = [1] + [x for x in nums if x] + [1]
        n = len(_nums)
        dp = [[0] * n for i in range(n)]
        for k in range(2, n):
            for left in range(n-k):
                right = left + k
                for i in range(left+1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        _nums[left]*_nums[i]*_nums[right] + dp[left][i] + dp[i][right]
                    )

        return dp[0][n-1]


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [3,1,5,8],
            167
        ),
        (
            [35,16,83,87,84,59,48,41,20,54],
            1849648
        ),
        (
            [8,2,6,8,9,8,1,4,1,5,3,0,7,7,0,4,2,2],
            -1
        )
    ]
    f = s.maxCoins
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
