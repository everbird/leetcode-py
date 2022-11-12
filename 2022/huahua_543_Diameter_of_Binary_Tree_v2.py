#!/usr/bin/env python3

class Solution(object):
    r = 0
    def diameterOfBinaryTree(self, root):
        self.r = 1

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            self.r = max(self.r, left+right+1)
            return max(left, right) + 1

        dfs(root)
        return self.r - 1
