#!/usr/bin/env python
# encoding: utf-8


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if not root:
            return True

        return self.is_symmetric_trees(root.left, root.right)

    def is_symmetric_trees(self, l, r):
        if not l or not r:
            return l == r

        return l.val == r.val \
            and self.is_symmetric_trees(l.left, r.right) \
            and self.is_symmetric_trees(l.right, r.left)

if __name__ == '__main__':
    s = Solution()

    root = n1 = TreeNode(1)
    n2 = TreeNode(2)
    m2 = TreeNode(2)
    n3 = TreeNode(3)
    m3 = TreeNode(3)
    n4 = TreeNode(4)
    m4 = TreeNode(5)

    n1.left = n2
    n1.right = m2
    n2.left = n3
    m2.right = m3
    n2.right = n4
    m2.left = m4

    print s.isSymmetric(root)

    root = n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(3)
    n5 = TreeNode(2)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n3.left = n5

    print s.isSymmetric(root)
