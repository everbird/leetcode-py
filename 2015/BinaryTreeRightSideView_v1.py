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
    def rightSideView(self, root):
        if not root:
            return []

        result = []
        self.rightView(root, result, 0)
        return result

    def rightView(self, node, result, depth):
        if not node:
            return

        if len(result) == depth:
            result.append(node.val)

        self.rightView(node.right, result, depth+1)
        self.rightView(node.left, result, depth+1)


if __name__ == '__main__':
    s = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)

    r = n1
    n1.left = n2
    n1.right = n3
    n2.right = n5
    n3.right = n4

    print s.rightSideView(r)
