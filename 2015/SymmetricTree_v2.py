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

        ql = [root.left]
        qr = [root.right]
        while ql and qr:
            nl = ql.pop()
            nr = qr.pop()

            if nl is None and nr is None:
                continue

            if nl is None or nr is None or nl.val != nr.val:
                return False

            ql = [nl.left, nl.right] + ql
            qr = [nr.right, nr.left] + qr

        return not ql and not qr


if __name__ == '__main__':
    s = Solution()

    root = n1 = TreeNode(1)
    n2 = TreeNode(2)
    m2 = TreeNode(2)
    n3 = TreeNode(3)
    m3 = TreeNode(3)
    n4 = TreeNode(4)
    m4 = TreeNode(4)

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
