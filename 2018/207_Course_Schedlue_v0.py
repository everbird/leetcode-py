#!/usr/bin/eni python
# encoding: utf-8


from collections import defaultdict


class Solution(object):

    def canFinish(self, numCourses, prerequisites):
        s = []
        visited = defaultdict(int)
        d = defaultdict(list)
        for u, v in prerequisites:
            d[u].append(v)

        for i in xrange(numCourses):
            # if visited[i] == 0 and has_cycle(i, d, visited):
            if visited[i] == 0 and has_cycle_iterative(i, d, visited):
                return False

        return True


def has_cycle(start, d, visited):
    visited[start] = 1
    for x in d[start]:
        if visited[x] == 1:
            return True
        elif visited[x] == 0:
            if has_cycle(x, d, visited):
                return True

    visited[start] = 2

    return False


def has_cycle_iterative(start, d, visited):
    s = [start]
    while s:
        n = s[-1]
        visited[n] = 1

        nodes = d[n]
        if not nodes or all(visited[x]==2 for x in nodes):
            t = s.pop()
            visited[t] = 2
        else:
            for x in d[n]:
                if visited[x] == 1:
                    return True
                elif visited[x] == 0:
                    s.append(x)

    return False


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                2,
                [[1,0]]
            ),
            True
        ),
        (
            (
                2,
                [[1,0],[0,1]]
            ),
            False
        ),
        (
            (
                4,
                [[0,1],[3,1],[1,3],[3,2]]
            ),
            False
        ),
        (
            (
                3,
                [[0,1],[0,2],[1,2]]
            ),
            True
        ),
    ]
    f = s.canFinish
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
