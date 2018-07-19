#!/usr/bin/eni python
# encoding: utf-8


from collections import defaultdict


class Solution(object):
    def firstUniqChar(self, s):
        d_index = {}
        d_cnt = defaultdict(int)
        for i, x in enumerate(s):
            d_index[i] = x
            d_cnt[x] += 1
        for i in range(len(s)):
            if d_cnt[d_index[i]] == 1:
                return i

        return -1



if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            'leetcode',
            0
        ),
        (
            'loveleetcode',
            2
        ),
    ]
    f = s.firstUniqChar
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
