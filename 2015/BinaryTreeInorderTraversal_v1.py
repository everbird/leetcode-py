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
    # @return {integer[]}
    def inorderTraversal(self, root):
        if not root:
            return []

        s = []
        r = []
        p = root
        while s or p:

            if p.left:
                s.append(p)
                t = p.left
                p.left = None
                p = t
            else:
                r.append(p.val)
                if p.right:
                    t = p.right
                    p.right = None
                    p = t
                else:
                    p = s.pop() if s else None

        return r

if __name__ == '__main__':
    s = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    root = n1
    n1.right = n2
    n2.left = n3

    print s.inorderTraversal(root)

    print '-' * 6

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)

    root = n1
    n1.right = n3
    n1.left = n2
    n3.left = n4
    n4.right = n5

    print s.inorderTraversal(root)
