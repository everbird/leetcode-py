#!/usr/bin/env python3

from collections import defaultdict, deque

class Node:
    out_degree = 0
    in_nodes = []

    def __init__(self, out_degree=0, in_nodes=None):
        self.out_degree = out_degree
        self.in_nodes = in_nodes if in_nodes else []

    def __repr__(self):
        return "<Node: out_degree={}, in_nodes={}>".format(
            self.out_degree,
            self.in_nodes
        )


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        g = defaultdict(Node)
        for i, nodes in enumerate(graph):
            for _i in nodes:
                g[_i].in_nodes.append(i)
            g[i].out_degree = len(nodes)

        rs = []
        q = deque()
        for i, node in g.items():
            if node.out_degree == 0:
                q.append(i)

        visited = set()
        while q:
            i = q.popleft()
            rs.append(i)
            visited.add(i)

            n = g[i]
            for _i in n.in_nodes:
                if _i in visited:
                    continue

                _n = g[_i]
                _n.out_degree -= 1

                if _n.out_degree == 0:
                    q.append(_i)

        return sorted(rs)
