#!/usr/bin/env python
# encoding: utf-8


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    def __repr__(self):
        return '<{}>'.format(self.label)


def printg(head):
    if head:
        print id(head), head.label, '|', head.neighbors
        for n in head.neighbors:
            if n.label == head.label:
                print n.label, '*'
            else:
                printg(n)


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        return self._(node, {})

    def _(self, node, visited):
        if not node:
            return

        if node in visited:
            return visited[node]

        new_n = UndirectedGraphNode(node.label)
        visited[node] = new_n
        for n in node.neighbors:
            _new = self._(n, visited)
            new_n.neighbors.append(_new)

        return new_n


if __name__ == '__main__':
    s = Solution()
    head = n1 = UndirectedGraphNode(0)
    n2 = UndirectedGraphNode(1)
    n3 = UndirectedGraphNode(2)
    n1.neighbors = [n2, n3]
    n2.neighbors = [n3]
    n3.neighbors = [n3]
    printg(head)
    h = s.cloneGraph(head)
    printg(h)
