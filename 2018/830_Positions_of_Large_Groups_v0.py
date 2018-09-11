#!/usr/bin/eni python
# encoding: utf-8

class Solution(object):
    def largeGroupPositions(self, S):
        pre = None
        cnt = 1
        r = []
        for i, ch in enumerate(S):
            if ch == pre:
                cnt += 1
            else:
                if cnt > 2:
                    r.append([i-cnt, i-1])
                cnt = 1

            pre = ch

        if cnt > 2:
            r.append([i-cnt+1, i])

        return r


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            "abbxxxxzzy",
            [[3,6]]
        ),
        (
            "abc",
            []
        ),
        (
            "abcdddeeeeaabbbcd",
            [[3,5],[6,9],[12,14]]
        ),
    ]
    f = s.largeGroupPositions
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
