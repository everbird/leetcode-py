#!/usr/bin/env python3

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nmap = {}
        
        if not head:
            return

        def dfs(node):
            if node in nmap:
                return nmap[node]

            _node = Node(node.val)
            nmap[node] = _node
            if node.next:
                _node.next = dfs(node.next)

            if node.random:
                _node.random = dfs(node.random)

            return _node

        return dfs(head)
