#!/usr/bin/env python3

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        s = [root]
        v = root.val
        while s:
            n = s.pop()
            if v != n.val:
                return False

            if n.right:
                s.append(n.right)

            if n.left:
                s.append(n.left)

        return True
