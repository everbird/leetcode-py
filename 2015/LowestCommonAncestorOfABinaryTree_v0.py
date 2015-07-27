#!/usr/bin/env python
# encoding: utf-8


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<{}>'.format(self.val)


class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right


if __name__ == '__main__':
    s = Solution()
    n1 = TreeNode(3)
    n2 = TreeNode(5)
    n3 = TreeNode(1)
    n4 = TreeNode(6)
    n5 = TreeNode(2)
    n6 = TreeNode(0)
    n7 = TreeNode(8)
    n8 = TreeNode(7)
    n9 = TreeNode(4)
    root = n1
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n5.left = n8
    n5.right = n9

    p = n2
    q = n9

    h = s.lowestCommonAncestor(root, p, q)
    print h

    print '-'*6

    p = n2
    q = n3

    h = s.lowestCommonAncestor(root, p, q)
    print h
