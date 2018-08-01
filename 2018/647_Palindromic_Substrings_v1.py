#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def countSubstrings(self, s):
        _s = '#'.join(s)
        n = len(_s)
        cnt = 0
        for j in range(n):
            for i in range(j+1):
                if j-i < 0 or j+i >= n or _s[j-i] != _s[j+i]:
                    break
                elif _s[j-i] == '#':
                    continue
                else:
                    cnt += 1

        return cnt


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
    ]
    f = s.countSubstrings
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
