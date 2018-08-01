#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def countSubstrings(self, s):
        _s = '#'.join('^{}$'.format(s))
        n = len(_s)
        dp = [0] * n
        C = R = 0
        for i in range(1, n-1):
            _i = C - (i - C)
            dp[i] = 0 if i > R else min(dp[_i], R-i)
            # while (i+dp[i]+1 < n) and (i-dp[i]-1>=0) and _s[i + dp[i] + 1] == _s[i - dp[i] - 1]:
            while _s[i + dp[i] + 1] == _s[i - dp[i] - 1]:
                dp[i] += 1

            if dp[i] + i > R:
                C = i
                R = dp[i] + i

        cnt = 0
        for i in range(n):
            if _s[i] == '#':
                cnt += (dp[i] + 1) // 2
            else:
                cnt += dp[i] // 2
        return cnt + len(s)


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            'abc',
            3
        ),
        (
            'aaa',
            6
        ),
        (
            "dnncbwoneinoplypwgbwktmvkoimcooyiwirgbxlcttgteqthcvyoueyftiwgwwxvxvg",
            77
        )
    ]
    f = s.countSubstrings
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
