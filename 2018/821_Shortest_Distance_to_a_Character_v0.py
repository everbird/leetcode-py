#!/usr/bin/eni python
# encoding: utf-8

class Solution(object):
    def shortestToChar(self, S, C):
        size = len(S)
        r = [float('inf')]  * size
        pre_c_index = None
        for i in xrange(size):
            if S[i] == C:
                pre_c_index = i
                r[pre_c_index] = 0
            elif pre_c_index is not None:
                dis = i - pre_c_index
                r[i] = min(r[i], dis)

        next_c_index = None
        for i in xrange(size-1, -1, -1):
            if S[i] == C:
                next_c_index = i
                r[next_c_index] = 0
            elif next_c_index is not None:
                dis = next_c_index - i
                r[i] = min(r[i], dis)

        return r


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                "loveleetcode",
                'e'
            ),
            [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
        ),
    ]
    f = s.shortestToChar
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
