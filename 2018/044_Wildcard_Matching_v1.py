#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):

    def isMatch(self, s, p):
        if not p:
            return not s

        if not s:
            return not p.replace('*', '')

        len_s = len(s)
        len_p = len(p)
        if len_s < (len_p - p.count('*')):
            return False

        if p == '*':
            return True

        dp = [False] * (len_s+1)
        dp[0] = True
        for y in xrange(1, len_p+1):
            new_dp = [False] * (len_s+1)
            for x in range(len_s+1):
                p_ch = p[y-1]
                if x == 0:
                    new_dp[x] = dp[x] and p_ch == '*'
                    continue

                ch = s[x-1]
                if p_ch == '?' or ch == p_ch:
                    new_dp[x] = dp[x-1]
                elif p_ch == '*':
                    new_dp[x] = dp[x] or new_dp[x-1] or dp[x-1]
                # print '>>>', s[:x], p[:y], dp[y][x]

            dp = new_dp

        return dp[-1]


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
        ),
        (
            (
                "",
                ""
            ),
            True
        ),
    ]
    f = s.isMatch
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
