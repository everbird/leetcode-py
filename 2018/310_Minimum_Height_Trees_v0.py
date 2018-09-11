#!/usr/bin/eni python
# encoding: utf-8


from collections import defaultdict


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        d = defaultdict(list)
        for a, b in edges:
            d[a].append(b)
            d[b].append(a)

        min_h = float('inf')
        r = []
        for i in xrange(n):
            h = dfs(i, d)
            if h < min_h:
                min_h = h
                r = [i]
            elif h == min_h:
                r.append(i)

        return r


def dfs(root, d):
    visited = set([root])
    max_h = 0
    q = [(root, 0)]
    while q:
        n, h = q.pop()
        nodes = d[n]
        for node in nodes:
            if node in visited:
                continue

            if len(d[node]) == 1:
                max_h = max(max_h, h+1)
            visited.add(node)
            q.append((node, h+1))
    return max_h


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
    ]
    f = s.findMinHeightTrees
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
