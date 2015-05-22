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
    def isBalanced(self, root):
        if not root:
            return True

        lh = self.get_height(root.left)
        rh = self.get_height(root.right)
        return 0 <= abs(lh - rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_height(self, root):
        if not root:
            return 0

        lh = self.get_height(root.left)
        rh = self.get_height(root.right)
        return max(lh, rh) + 1


if __name__ == '__main__':
    s = Solution()

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n1.left = n2
    n2.right = n3

    print s.isBalanced(n1)

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n4.left = n5
    n3.right = n6
    n6.right = n7

    print s.isBalanced(n1)

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n1.left = n2
    n1.right = n3

    print s.isBalanced(n1)
