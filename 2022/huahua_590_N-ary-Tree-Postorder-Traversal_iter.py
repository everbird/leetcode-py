#!/usr/bin/env python3

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        s = [root]
        rs = []
        while s:
            n = s.pop()
            rs.insert(0, n.val)

            for c in n.children:
                s.append(c)

        return rs
