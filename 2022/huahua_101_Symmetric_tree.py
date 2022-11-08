#!/usr/bin/env python3

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if not root.left and not root.right:
            return True

        s = [root.left]
        ss = [root.right]
        while s:
            n = s.pop()
            p = ss.pop()
            if not p or not n or n.val != p.val:
                return False

            if n.right:
                s.append(n.right)
                ss.append(p.left)
            elif p.left:
                return False

            if n.left:
                s.append(n.left)
                ss.append(p.right)
            elif p.right:
                return False

        return len(ss) == 0
