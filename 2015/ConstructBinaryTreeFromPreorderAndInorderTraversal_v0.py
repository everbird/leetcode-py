#!/usr/bin/env python
# encoding: utf-8


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        if not inorder or not preorder:
            return None

        p = preorder.pop(0)
        t = TreeNode(p)
        k = inorder.index(p)
        t.left = self.buildTree(preorder, inorder[:k])
        t.right = self.buildTree(preorder, inorder[k+1:])

        return t

    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)
        print root.val
        self.inorder(root.right)

    def preorder(self, root):
        if not root:
            return

        print root.val
        self.inorder(root.left)
        self.inorder(root.right)


if __name__ == '__main__':
    s = Solution()
    h = s.buildTree([1,2,3,4,5], [2,1,4,3,5])
    s.inorder(h)
    print '-' * 6
    s.preorder(h)

    h = s.buildTree([], [])
