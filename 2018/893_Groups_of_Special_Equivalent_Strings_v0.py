#!/usr/bin/eni python
# encoding: utf-8


from collections import Counter


class Solution(object):
    def numSpecialEquivGroups(self, A):
        r = set([])
        for s in A:
            uuid = get_uuid(s)
            if uuid not in r:
                r.add(uuid)

        return len(r)


def get_uuid(S):
    size = len(S)
    c1 = Counter(S[::2])
    c2 = Counter(S[1::2])
    return (
        get_uuid_from_counter(c1),
        get_uuid_from_counter(c2),
    )


def get_uuid_from_counter(c):
    return tuple(sorted(c.items()))



if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            ["a","b","c","a","c","c"],
            3
        ),
        (
            ["aa","bb","ab","ba"],
            4
        ),
        (
            ["abc","acb","bac","bca","cab","cba"],
            3
        ),
        (
            ["abcd","cdab","adcb","cbad"],
            1
        ),
    ]
    f = s.numSpecialEquivGroups
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
