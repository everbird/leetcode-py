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
    def postorderTraversal_recursion(self, root):
        if not root:
            return []

        r1 = self.postorderTraversal(root.left)
        r2 = self.postorderTraversal(root.right)
        return r1 + r2 + [root.val]

    def postorderTraversal(self, root):
        p = root
        s1 = []
        s2 = []

        p = root
        while p:
            s1.append(p.val)
            if p.left:
                s2.append(p.left)

            if p.right:
                p = p.right
            else:
                if s2:
                    p = s2.pop()
                else:
                    break

        return s1[::-1]


if __name__ == '__main__':
    s = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    head = n1
    n1.right = n2
    n2.left = n3

    print s.postorderTraversal(head)
