#!/usr/bin/env python
# encoding: utf-8


from collections import defaultdict


class Solution(object):

    def loudAndRich(self, richer, quiet):
        len_n = len(quiet)
        r = defaultdict(list)
        result = [None] * len_n
        for rich, poor in richer:
            r[poor].append(rich)

        for i in range(len_n):
            dfs(i, r, quiet, result)

        return result


def dfs(n, r, quiet, result):
    x = result[n]
    if x:
        return quiet[x], x

    len_n = len(quiet)
    r_index = n
    r_min_q = quiet[n]

    for _next in r.get(n, []):
        min_q, index = dfs(_next, r, quiet, result)
        if min_q < r_min_q:
            r_min_q = min_q
            r_index = index
    result[n] = r_index
    return r_min_q, r_index


def main():
    s = Solution()
    tests = [
        (
            (
                [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]],
                [3,2,5,4,6,1,7,0]
            ),
            [5,5,2,5,4,5,6,7]
        ),
    ]
    for input_args, expected in tests:
        r = s.loudAndRich(*input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)

if __name__ == '__main__':
    main()
