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
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        if not root:
            return []

        r = []
        cur = [root]
        while cur:
            row = []
            next = []
            for n in cur:
                row.append(n.val)

                if n.left:
                    next.append(n.left)

                if n.right:
                    next.append(n.right)

            r = [row] + r
            cur = next

        return r


if __name__ == '__main__':
    s = Solution()

    n3 = TreeNode(3)
    n9 = TreeNode(9)
    n20 = TreeNode(20)
    n15 = TreeNode(15)
    n7 = TreeNode(7)

    root = n3
    n3.left = n9
    n3.right = n20
    n20.left = n15
    n20.right = n7

    print s.levelOrderBottom(root)
