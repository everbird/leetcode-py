#!/usr/bin/env python3

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        new_target = targetSum - root.val
        if not root.left and not root.right:
            return new_target == 0

        return self.hasPathSum(root.left, new_target) or self.hasPathSum(root.right, new_target)
