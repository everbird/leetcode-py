#!/usr/bin/env python
# encoding: utf-8


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<'+str(self.val)+'>'


class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        return self.hasPathSum(root.right, sum-root.val) or self.hasPathSum(root.left, sum-root.val)


if __name__ == '__main__':
    s = Solution()

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    n11 = TreeNode(11)
    n13 = TreeNode(13)
    nn4 = TreeNode(4)

    root = n5
    n5.left = n4
    n5.right = n8
    n4.left = n11
    n11.left = n7
    n11.right = n2
    n8.left = n13
    n8.right = nn4
    nn4.right = n1

    print s.hasPathSum(root, 22)

    print s.hasPathSum(None, 0)
    print s.hasPathSum(None, 1)

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    root = n1
    n1.left = n2

    print s.hasPathSum(root, 1)
