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
        if not root:
            return

        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)

        if p.val <= root.val <= q.val:
            return root

        if q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)


if __name__ == '__main__':
    s = Solution()
    n6 = TreeNode(6)
    n2 = TreeNode(2)
    n8 = TreeNode(8)
    n0 = TreeNode(0)
    n4 = TreeNode(4)
    n7 = TreeNode(7)
    n9 = TreeNode(9)
    n3 = TreeNode(3)
    n5 = TreeNode(5)

    root = n6
    n6.left = n2
    n6.right = n8
    n2.left = n0
    n2.right = n4
    n8.left = n7
    n8.right = n9
    n4.left = n3
    n4.right = n5

    print s.lowestCommonAncestor(root, n2, n8)
    print s.lowestCommonAncestor(root, n2, n4)
