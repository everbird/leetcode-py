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
    total = 0

    def sumNumbers(self, root):
        if not root:
            return 0

        self.total = 0
        self.dfs(root, 0)
        return self.total

    def dfs(self, root, s):
        s += root.val
        if not root.left and not root.right:
            self.total += s

        s *= 10
        if root.left:
            self.dfs(root.left, s)

        if root.right:
            self.dfs(root.right, s)


if __name__ == '__main__':
    s = Solution()

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    root = n1
    n1.left = n2
    n1.right = n3

    print s.sumNumbers(root)

    n1 = TreeNode(1)
    n2 = TreeNode(0)
    root = n1
    n1.left = n2

    print s.sumNumbers(root)

    print s.sumNumbers(None)

    n1 = TreeNode(4)
    n2 = TreeNode(9)
    n3 = TreeNode(0)
    n4 = TreeNode(1)
    root = n1
    n1.left = n2
    n1.right = n3
    n2.right = n4

    print s.sumNumbers(root)

    n1 = TreeNode(8)
    n2 = TreeNode(3)
    n3 = TreeNode(5)
    n4 = TreeNode(9)
    n5 = TreeNode(9)
    n6 = TreeNode(5)
    root = n1
    n1.left = n2
    n1.right = n3
    n2.right = n4
    n4.left = n5
    n4.right = n6

    print s.sumNumbers(root)

    n1 = TreeNode(5)
    n2 = TreeNode(3)
    n3 = TreeNode(2)
    n4 = TreeNode(7)
    n5 = TreeNode(0)
    n6 = TreeNode(6)
    n7 = TreeNode(0)
    root = n1
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n5.left = n7

    print s.sumNumbers(root)
