#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def stoneGame(self, piles):
        n = len(piles)
        cache = {}
        def alex_pick(lo, hi):
            if (lo, hi) in cache:
                return cache[(lo, hi)]
            if lo > hi:
                return 0
            if lo == hi:
                return piles[lo]
            r = max(piles[lo] + min(alex_pick(lo+1, hi-1), alex_pick(lo+2, hi)), piles[hi] + min(alex_pick(lo+1, hi-1), alex_pick(lo, hi-2)))
            cache[(lo, hi)] = r
            return r
        alex = alex_pick(0, n-1)
        lee = sum(piles) - alex
        return alex > lee



if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [5,3,4,5],
            True
        ),
    ]
    f = s.stoneGame
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
