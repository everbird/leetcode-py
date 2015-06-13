#!/usr/bin/env python
# encoding: utf-8


from collections import defaultdict


class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        d = defaultdict(list)
        for i in prerequisites:
            f, t = i
            d[f].append(t)

        for i in range(numCourses):
            if not self.dfs(d, i):
                return False

        return True

    def dfs(self, d, start):
        stack = [start]
        visited = set([])
        while stack:
            n = stack.pop()
            if n not in visited:
                visited.add(n)
            else:
                return False
            ts = d.get(n, [])
            for t in ts[::-1]:
                stack.append(t)

        return True


if __name__ == '__main__':
    s = Solution()
    print s.canFinish(2, [[1,0]])
    print s.canFinish(2, [[1,0],[0,1]])
