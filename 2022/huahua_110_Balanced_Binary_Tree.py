#!/usr/bin/env python3

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        ld = _get_depth(root.left)
        rd = _get_depth(root.right)

        return abs(ld - rd) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


def _get_depth(node: TreeNode):
    if not node:
        return 0

    ld = _get_depth(node.left)
    rd = _get_depth(node.right)
    return max(ld, rd) + 1
