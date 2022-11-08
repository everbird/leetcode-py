#!/usr/bin/env python3

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        s = [(root, 0)]
        deepest = 0
        _sum = 0
        while s:
            n, lvl = s.pop()
            if lvl > deepest:
                deepest = lvl
                _sum = n.val
            elif lvl == deepest:
                _sum += n.val

            if n.right:
                s.append((n.right, lvl+1))

            if n.left:
                s.append((n.left, lvl+1))

        return _sum
