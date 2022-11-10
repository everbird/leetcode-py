#!/usr/bin/env python3

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # postorder
        if not root:
            return

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if root.val == target and not (root.left or root.right):
            return None

        return root
