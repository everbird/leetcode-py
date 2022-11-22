#!/usr/bin/env python3

from collections import defaultdict, deque


class Node:
    in_degree = 0
    next_nodes = []

    def __init__(self, in_degree=0, next_nodes=None):
        self.in_degree = in_degree
        self.next_nodes = next_nodes if next_nodes else []

    def __repr__(self):
        return "<Node: in_degree={}, next_nodes={}>".format(
            self.in_degree,
            self.next_nodes
        )


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(Node)
        total = 0
        for u, v in prerequisites:
            g[u].in_degree += 1
            g[v].next_nodes.append(u)
            total += 1

        rs = []
        for i in range(numCourses):
            if i not in g:
                rs.append(i)

        q = deque()
        for i, node in g.items():
            if node.in_degree == 0:
                q.append(i)

        while q:
            i = q.popleft()
            rs.append(i)
            n = g[i]
            for _i in n.next_nodes:
                _n = g[_i]
                _n.in_degree -= 1
                total -= 1

                if _n.in_degree == 0:
                    q.append(_i)

        return rs if total == 0 else []
