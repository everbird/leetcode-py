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
    def maxPathSum(self, root):
        self.r = -2**31
        self.get_max_length(root)
        return self.r

    def get_max_length(self, root):
        if not root:
            return 0

        l = max(0, self.get_max_length(root.left))
        r = max(0, self.get_max_length(root.right))
        self.r = max(self.r, root.val+l+r)
        return max(l, r)+root.val


if __name__ == '__main__':
    s = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    r = n1
    n1.left = n2
    n1.right = n3

    #print s.get_max_length(r)
    print s.maxPathSum(r)

    r = TreeNode(-3)
    print s.maxPathSum(r)

    n1 = TreeNode(2)
    n2 = TreeNode(-1)
    r = n1
    n1.left = n2

    print s.maxPathSum(r)

    n1 = TreeNode(0)
    n2 = TreeNode(1)
    n3 = TreeNode(1)
    r = n1
    n1.left = n2
    n1.right = n3

    print s.maxPathSum(r)
