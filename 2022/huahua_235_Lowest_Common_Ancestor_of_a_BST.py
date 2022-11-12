#!/usr/bin/env python3

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return

        low, high = (p.val, q.val) if p.val < q.val else (q.val, p.val)
        s = [root]
        while s:
            n = s.pop()
            if low <= n.val <= high:
                return n
            elif n.val < low and n.right:
                s.append(n.right)
            elif n.val > high and n.left:
                s.append(n.left)

        return
