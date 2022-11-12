#!/usr/bin/env python3

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)
        return max(left, right, max_depth(root.left)+max_depth(root.right))


def max_depth(node):
    if not node:
        return 0

    r = 1
    s = [(node, 1)]
    while s:
        n, lvl = s.pop()
        r = max(r, lvl)

        if n.left:
            s.append((n.left, lvl+1))

        if n.right:
            s.append((n.right, lvl+1))

    return r
