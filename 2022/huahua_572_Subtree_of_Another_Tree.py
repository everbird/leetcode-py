#!/usr/bin/env python3

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        r1 = []
        preorder(subRoot, r1)

        if not root:
            return len(r1) == 0

        s = [root]
        while s:
            n = s.pop()
            r2 = []
            preorder(n, r2)
            if r1 == r2:
                return True

            if n.right:
                s.append(n.right)

            if n.left:
                s.append(n.left)

        return False


def preorder(node, rs):
    if not node:
        rs.append(None)
        return

    rs.append(node.val)
    inorder(node.left, rs)
    inorder(node.right, rs)
