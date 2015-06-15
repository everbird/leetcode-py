#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    result = []

    def findOrder(self, numCourses, prerequisites):
        self.result = []
        g = []
        v = [0] * numCourses
        for i in range(numCourses):
            g.append([])

        for c, d in prerequisites:
            g[d].append(c)

        for i in range(numCourses):
            if not self.dfs(g, v, i):
                return []

        return self.result[::-1]


    def dfs(self, g, v, i):
        if v[i] == -1:
            return False

        if v[i] == 1:
            return True

        v[i] = -1
        for x in g[i]:
            if not self.dfs(g, v, x):
                return False
        v[i] = 1
        self.result.append(i)
        return True


if __name__ == '__main__':
    s = Solution()
    print s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
    print s.findOrder(2, [[1,0]])
    print s.findOrder(2, [[1,0], [0,1]])
