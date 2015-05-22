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
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        if not root:
            return

        r = []
        self.preorder(root, r)
        for i in range(len(r)-1):
            r[i].right = r[i+1]
            r[i].left = None

        r[len(r)-1].right = None
        r[len(r)-1].left = None

    def preorder(self, root, result):
        if not root:
            return

        result.append(root)
        self.preorder(root.left, result)
        self.preorder(root.right, result)

    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)
        print root.val
        self.inorder(root.right)


if __name__ == '__main__':
    s = Solution()

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)

    root = n1
    n1.left = n2
    n2.left = n3
    n2.right = n4
    n1.right = n5
    n5.right = n6

    s.inorder(root)
    print '-' * 6
    s.flatten(root)
    s.inorder(root)
