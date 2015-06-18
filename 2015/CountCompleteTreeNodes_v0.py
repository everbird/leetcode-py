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
    def countNodes(self, root):
        if root is None:
            return 0

        h1 = h2 = 0
        p1 = p2 = root

        while p1:
            p1 = p1.left
            h1 += 1

        while p2:
            p2 = p2.right
            h2 += 1

        if h1 == h2:
            return 2**h1 - 1
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)


if __name__ == '__main__':
    s = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)

    root = n1
    n1.left = n2
    n1.right = n3
    n2.left = n4

    print s.countNodes(root)
