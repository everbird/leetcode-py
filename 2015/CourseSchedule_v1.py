#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        g = [0] * numCourses
        d = []
        for i in range(numCourses):
            d.append([])

        for f, t in prerequisites:
            d[f].append(t)

        for i in range(numCourses):
            if not self.dfs(g, d, i):
                return False

        return True

    def dfs(self, g, d, start):
        if g[start] == -1:
            return False
        elif g[start] == 1:
            return True
        g[start] = -1
        for i in d[start]:
            if not self.dfs(g, d, i):
                return False

        g[start] = 1
        return True


if __name__ == '__main__':
    s = Solution()
    print s.canFinish(2, [[1,0]])
    print s.canFinish(2, [[1,0],[0,1]])
