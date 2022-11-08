#!/usr/bin/env python3

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        q = [(root, 0)]
        rs = []
        while q:
            n, lvl = q.pop(0)
            if len(rs) == lvl:
                rs.append([])

            rs[lvl].append(n.val)
            for c in n.children:
                q.append((c, lvl+1))

        return rs
