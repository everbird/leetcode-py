#!/usr/bin/env python3

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        s = [(root, 1)]
        r = 1
        while s:
            n, lvl = s.pop()
            r = max(r, lvl)

            if n.right:
                s.append((n.right, lvl+1))


            if n.left:
                s.append((n.left, lvl+1))

        return r
