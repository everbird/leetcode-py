#!/usr/bin/env python
# encoding: utf-8


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if (p and not q) or (not p and q):
            return False

        if not p and not q:
            return True

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    s = Solution()

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    t1 = n1
    n1.right = n2
    n2.left = n3

    m1 = TreeNode(1)
    m2 = TreeNode(2)
    m3 = TreeNode(4)
    t2 = m1
    m1.right = m2
    m2.left = m3

    print s.isSameTree(t1, t2)
