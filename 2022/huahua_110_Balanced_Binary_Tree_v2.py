#!/usr/bin/env python3

class Solution:
    balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def depth(node):
            # Shortcut the latter visit once found a not balanced one
            # Modified based on get max depth
            if not node or not self.balanced:
                return -1

            ld = depth(node.left)
            rd = depth(node.right)

            if abs(ld - rd) > 1:
                self.balanced = False
                return -1

            return max(ld, rd) + 1

        depth(root)
        return self.balanced
