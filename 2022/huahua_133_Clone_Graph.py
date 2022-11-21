#!/usr/bin/env python3

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nmap = {}

        if not node:
            return

        def dfs(node):
            if node in nmap:
                return nmap[node]

            _node = Node(node.val)
            nmap[node] = _node

            _neighbors = []
            for n in node.neighbors:
                _n = dfs(n)
                _neighbors.append(_n)
            _node.neighbors = _neighbors
            
            return _node


        return dfs(node)
