#!/usr/bin/env python3

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        rs = []
        def dfs(node, path):
            if not node:
                return

            path.append(node.val)
            if not node.left and not node.right:
                rs.append('->'.join(map(str, path)))

            if node.left:
                dfs(node.left, path)

            if node.right:
                dfs(node.right, path)

            path.pop()

        dfs(root, [])
        return rs
