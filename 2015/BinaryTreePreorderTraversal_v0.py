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
    # @return {integer[]}
    def preorderTraversal(self, root):
        if not root:
            return []

        a = []
        s = []
        p = root
        while p or s:
            a.append(p.val)
            if p.right:
                s.append(p.right)

            if p.left:
                p = p.left
            else:
                if s:
                    p = s.pop()
                else:
                    break

        return a

    def preorderTraversal_recursion(self, root):
        if not root:
            return []

        r1 = self.preorderTraversal(root.left)
        r2 = self.preorderTraversal(root.right)
        return [root.val] + r1 + r2


if __name__ == '__main__':
    s = Solution()

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    head = n1
    n1.right = n2
    n2.left = n3

    print s.preorderTraversal(head)

    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n1 = TreeNode(1)
    n4 = TreeNode(4)
    n2 = TreeNode(2)
    head = n3
    n3.left = n5
    n3.right = n1
    n5.left = n4
    n5.right = n2

    print s.preorderTraversal(head)
