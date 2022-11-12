#!/usr/bin/env python3

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        r = 0

        def dfs(node):
            nonlocal r
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            r += abs(left) + abs(right)
            return left + right + node.val - 1

        dfs(root)
        return r
