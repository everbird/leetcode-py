#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param A, a list of integers
    # @return an integer
    # 6:57
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum


if __name__ == '__main__':
    s = Solution()
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print s.maxSubArray(a)

    a = [-2, -1]
    print s.maxSubArray(a)
