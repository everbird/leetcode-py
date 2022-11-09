#!/usr/bin/env python3

class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        elif not root.left:
            return self.minDepth(root.right) + 1
        elif not root.right:
            return self.minDepth(root.left) + 1

        return 1
