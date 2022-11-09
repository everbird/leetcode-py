#!/usr/bin/env python3

class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        r = float(inf)
        s = [(root, 1)]
        while s:
            n, lvl = s.pop()

            if not n.left and not n.right:
                r = min(r, lvl)

            if n.left:
                s.append((n.left, lvl+1))

            if n.right:
                s.append((n.right, lvl+1))

        return r
