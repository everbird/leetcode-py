#!/usr/bin/env python
# encoding: utf-8


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return

        n = postorder.pop()
        t = TreeNode(n)
        k = inorder.index(n)
        t.right = self.buildTree(inorder[k+1:], postorder)
        t.left = self.buildTree(inorder[:k], postorder)
        return t

    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)
        print root.val
        self.inorder(root.right)

    def postorder(self, root):
        if not root:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print root.val

    def preorder(self, root):
        if not root:
            return

        print root.val
        self.preorder(root.left)
        self.preorder(root.right)


if __name__ == '__main__':
    s = Solution()
    h = s.buildTree([2,1,4,3,5], [2,4,5,3,1])
    s.preorder(h)
    print '-' * 6
    s.inorder(h)
    print '-' * 6
    s.postorder(h)
