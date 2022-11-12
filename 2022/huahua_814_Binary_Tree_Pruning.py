#!/usr/bin/env python3

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        def _has_one(node):
            if not node:
                return False

            left_has_one = _has_one(node.left)
            right_has_one = _has_one(node.right)

            if not left_has_one:
                node.left = None

            if not right_has_one:
                node.right = None

            if not left_has_one and not right_has_one and node.val != 1:
                return False

            return True

        if not _has_one(root):
            return None

        return root
