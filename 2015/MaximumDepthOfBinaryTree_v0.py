#!/usr/bin/env python
# encoding: utf-8


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if not root:
            return 0

        ld = self.maxDepth(root.left)
        rd = self.maxDepth(root.right)
        return max(ld, rd) + 1


if __name__ == '__main__':
    s = Solution()
    root = n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n1.left = n2
    n2.right = n3
    n1.right = n4

    print s.maxDepth(root)
