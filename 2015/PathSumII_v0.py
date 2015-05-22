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
    def pathSum(self, root, sum):
        if not root:
            return []

        return self._pathSum(root, sum)

    def _pathSum(self, root, sum):
        r = []
        if not root:
            return []

        if not root.left and not root.right and root.val == sum:
            return [[root.val]]

        for li in self._pathSum(root.left, sum-root.val):
            r.append([root.val] + li)

        for ri in self._pathSum(root.right, sum-root.val):
            r.append([root.val] + ri)

        return r


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
    nn5 = TreeNode(5)

    root = n5
    n5.left = n4
    n5.right = n8
    n4.left = n11
    n11.left = n7
    n11.right = n2
    n8.left = n13
    n8.right = nn4
    nn4.right = n1
    nn4.left = nn5

    print s.pathSum(root, 22)

    print s.pathSum(None, 0)
    print s.pathSum(None, 1)

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    root = n1
    n1.left = n2

    print s.pathSum(root, 3)
