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
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(Node)
        total_edges = 0
        for s, t in prerequisites:
            g[s].in_degree += 1
            g[t].next_nodes.append(s)
            total_edges += 1

        q = deque()
        for x, node in g.items():
            if node.in_degree == 0:
                q.append(x)
        
        while q:
            i = q.popleft()
            for _i in g[i].next_nodes:
                _n = g[_i]
                _n.in_degree -= 1
                total_edges -= 1

                if _n.in_degree == 0:
                    q.append(_i)

        return total_edges == 0
