#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        g = []
        in_link_counts = [0] * numCourses
        for i in range(numCourses):
            g.append([])

        for c, d in prerequisites:
            in_link_counts[c] += 1
            g[d].append(c)

        return self.bfs(numCourses, g, in_link_counts)


    def bfs(self, numCourses, g, in_link_counts):
        queue = []
        path = []
        for i in range(numCourses):
            if in_link_counts[i] == 0:
                queue.append(i)

        while queue:
            n = queue.pop()
            path.append(n)
            to_links = g[n]
            for t in to_links:
                in_link_counts[t] -= 1
                if in_link_counts[t] == 0:
                    queue = [t] + queue

        return path if len(path) == numCourses else []


if __name__ == '__main__':
    s = Solution()
    print s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
    print s.findOrder(2, [[1,0]])
    print s.findOrder(2, [[1,0], [0,1]])
