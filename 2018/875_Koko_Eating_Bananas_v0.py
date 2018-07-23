#!/usr/bin/eni python
# encoding: utf-8

import math

class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        lo = 1
        hi = max(piles) + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if check(piles, H, mid):
                hi = mid
            else:
                lo = mid + 1

        return lo


def check(piles, H, k):
    for p in piles:
        H -= p // k
        if p % k:
            H -= 1
        if H < 0:
            return False
    return True


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                [3,6,7,11],
                8
            ),
            4
        ),
        (
            (
                [30,11,23,4,20],
                5
            ),
            30
        ),
        (
            (
                [30,11,23,4,20],
                6
            ),
            23
        )
    ]
    f = s.minEatingSpeed
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)


    print check([30, 11, 23, 4, 20], 5, 30), '<<<'
