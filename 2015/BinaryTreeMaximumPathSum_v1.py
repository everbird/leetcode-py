#!/usr/bin/env python
# encoding: utf-8


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


d = {}


def cache(f):
    def _(inst, root):
        ids = id(root)
        rs = d.get(ids)
        if rs is None:
            rs = f(inst, root)
            d[ids] = rs

        return rs

    return _


class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
        d = {}
        if not root:
            return 0

        queue = [root]
        maxl = -2**31

        while queue:
            p = queue.pop()

            ld = rd = 0
            if p.left:
                ld = self.get_max_length(p.left)
                queue = [p.left] + queue

            if p.right:
                rd = self.get_max_length(p.right)
                queue = [p.right] + queue

            v = max(ld, 0) + max(rd, 0) + p.val
            if maxl < v:
                maxl = v

        return maxl

    @cache
    def get_max_length(self, root):
        if not root:
            return 0

        l = self.get_max_length(root.left)
        r = self.get_max_length(root.right)
        return max(l, r, 0)+root.val


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
    print s.get_max_length(r.left)
