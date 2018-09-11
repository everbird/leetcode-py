#!/usr/bin/eni python
# encoding: utf-8


from collections import defaultdict


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]
        elif n == 2:
            return [0, 1]

        d = defaultdict(list)
        for a, b in edges:
            d[a].append(b)
            d[b].append(a)

        for i in xrange(n):
            if len(d) <= 2:
                break

            to_remove = [x for x, nodes in d.iteritems() if len(nodes) == 1]
            for j in to_remove:
                neighbor = d[j][0]
                d[neighbor].remove(j)
                del d[j]

        return d.keys()


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                4,
                [[1, 0], [1, 2], [1, 3]]
            ),
            [1]
        ),
        (
            (
                6,
                [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
            ),
            [3, 4]
        ),
        (
            (
                2,
                [[0, 1]]
            ),
            [0, 1]
        ),
        (
            (
                7,
                [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]]
            ),
            [1, 2]
        )
    ]
    f = s.findMinHeightTrees
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
