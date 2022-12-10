#!/usr/bin/env python3

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}

        def dfs(node):
            if not node:
                return 0

            _id = id(node)
            if _id in cache:
                return cache[_id]

            r = node.val
            if node.left:
                r += dfs(node.left.left) + dfs(node.left.right)

            if node.right:
                r += dfs(node.right.left) + dfs(node.right.right)

            ans = max(r, dfs(node.left)+dfs(node.right))
            cache[_id] = ans
            return ans

        return dfs(root)

# cache + dfs
