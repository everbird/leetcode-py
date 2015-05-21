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
    def isValidBST(self, root):
        if not root:
            return True

        r = []
        self.inorder(root, r)
        for i in range(len(r) - 1):
            if r[i] >= r[i+1]:
                return False

        return True

    def inorder(self, root, result):
        if not root:
            return

        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)


if __name__ == '__main__':
    s = Solution()

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    root = n1
    n1.right = n2
    n2.left = n3

    print s.isValidBST(root)
