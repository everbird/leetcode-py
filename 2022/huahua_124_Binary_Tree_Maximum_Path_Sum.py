#!/usr/bin/env python3

class Solution:
    r = -float('inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def get_max_path(node):
            if not node:
                return 0

            left = max(0, get_max_path(node.left))
            right = max(0, get_max_path(node.right))
            self.r = max(self.r, node.val + left + right)
            return node.val + max(left, right)

        get_max_path(root)
        return self.r
