#!/usr/bin/env python3

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return _max_depth(root, 0)

def _max_depth(node: TreeNode, lvl: int) -> int:
    if not node:
        return lvl
    left_depth = _max_depth(node.left, lvl+1)
    right_depth = _max_depth(node.right, lvl+1)
    return max(left_depth, right_depth)
