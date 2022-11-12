#!/usr/bin/env python3

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.longestUnivaluePath(root.left)
        right = self.longestUnivaluePath(root.right)

        v = 0
        if root.left and root.left.val == root.val:
            v += (_univalue_path_from_root(root.left) + 1)

        if root.right and root.right.val == root.val:
            v += (_univalue_path_from_root(root.right) + 1)
        return max(left, right, v)


def _univalue_path_from_root(node):
    if not node:
        return 0

    v = node.val
    s = [(node, 0)]
    r = 0
    while s:
        n, lvl = s.pop()

        if n.val == v:
            r = max(r, lvl)

            if n.left:
                s.append((n.left, lvl+1))

            if n.right:
                s.append((n.right, lvl+1))

    return r
