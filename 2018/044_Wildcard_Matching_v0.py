#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):

    def isMatch(self, s, p):
        len_s = len(s)
        len_p = len(p)
        dp = [[False] * (len_s+1) for i in range(len_p+1)]
        dp[0][0] = True
        for y in xrange(1, len_p+1):
            for x in range(len_s+1):
                p_ch = p[y-1]
                if x == 0:
                    dp[y][x] = dp[y-1][x] and p_ch == '*'
                    continue

                ch = s[x-1]
                # print x, y, ch, p_ch, dp
                if p_ch == '?' or ch == p_ch:
                    dp[y][x] = dp[y-1][x-1]
                elif p_ch == '*':
                    dp[y][x] = dp[y-1][x] or dp[y][x-1] or dp[y-1][x-1]
                # print '>>>', s[:x], p[:y], dp[y][x]

        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                "aa",
                "a"
            ),
            False
        ),
        (
            (
                "aa",
                "*"
            ),
            True
        ),
        (
            (
                "cb",
                "?a"
            ),
            False
        ),
        (
            (
                "adceb",
                "*a*b"
            ),
            True
        ),
        (
            (
                "acdcb",
                "a*c?b"
            ),
            False
        ),
        (
            (
                "",
                "a"
            ),
            False
        )
    ]
    f = s.isMatch
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
