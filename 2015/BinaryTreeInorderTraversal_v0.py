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
    # @return {integer[]}
    def inorderTraversal(self, root):
        if not root:
            return []

        r = [root.val]
        lefts = self.inorderTraversal(root.left)
        rights = self.inorderTraversal(root.right)
        return lefts + r + rights


if __name__ == '__main__':
    s = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    root = n1
    n1.right = n2
    n2.left = n3

    print s.inorderTraversal(root)
