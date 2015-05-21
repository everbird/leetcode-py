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
    def recoverTree(self, root):
        r = []
        self.inorder(root, r)
        p1 = p2 = None
        for i in range(len(r) - 1):
            if p1 is None and r[i].val > r[i+1].val:
                p1 = r[i]
                p2 = r[i+1]
            elif p1 and r[i].val > r[i+1].val:
                p2 = r[i+1]

        p1.val, p2.val = p2.val, p1.val

    def inorder(self, root, result):
        if not root:
            return

        self.inorder(root.left, result)
        result.append(root)
        self.inorder(root.right, result)


def print_inorder(root):
    if not root:
        return

    print_inorder(root.left)
    print root.val,
    print_inorder(root.right)


if __name__ == '__main__':
    s = Solution()

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    root = n1
    n1.right = n2
    n2.left = n3

    print_inorder(root)
    print
    print '-' * 6

    s.recoverTree(root)

    print_inorder(root)
