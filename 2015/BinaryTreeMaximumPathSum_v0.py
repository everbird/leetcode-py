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
        if not root:
            return 0

        queue = [root]
        maxl = 0

        while queue:
            p = queue.pop()

            ld = rd = 0
            if p.left:
                ld = self.get_max_length(p.left)
                queue = [p.left] + queue

            if p.right:
                rd = self.get_max_length(p.right)
                queue = [p.right] + queue

            v = ld + rd + p.val
            if maxl < v:
                maxl = v

        return maxl

    def get_max_length(self, root):
        if not root:
            return 0

        l = self.get_max_length(root.left)
        r = self.get_max_length(root.right)
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
