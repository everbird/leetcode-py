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
            p_ch = p[y-1]

            new_dp[0] = dp[0] and p_ch == '*'
            if p_ch == '*':
                for x in range(len_s):
                    new_dp[x+1] = dp[x+1] or new_dp[x] or dp[x]
            elif p_ch == '?':
                for x in range(len_s):
                    new_dp[x+1] = dp[x]
            else:
                for x in range(len_s):
                    if s[x] == p_ch:
                        new_dp[x+1] = dp[x]

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
