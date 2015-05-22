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
    # @return {integer}
    def minDepth(self, root):
        if not root:
            return 0

        ld = self.minDepth(root.left)
        rd = self.minDepth(root.right)
        return min(ld, rd)+1 if ld != 0 and rd != 0 else ld+rd+1


if __name__ == '__main__':
    s = Solution()

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)

    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right = n5
    n4.left = n6

    print s.minDepth(n1)
