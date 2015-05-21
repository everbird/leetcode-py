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
    # @return {integer[][]}
    def levelOrder(self, root):
        if not root:
            return []

        r = []
        queue = [(0, root)]
        while queue:
            level, n = queue.pop()
            if len(r) < (level+1):
                r.append([])
            r[level].append(n.val)
            if n.left:
                queue = [(level+1, n.left)] + queue

            if n.right:
                queue = [(level+1, n.right)] + queue

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

    print s.levelOrder(root)
