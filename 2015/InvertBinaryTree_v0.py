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
    # @return {TreeNode}
    def invertTree(self, root):
        if not root:
            return

        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left

        return root


def print_level(n):
    if not n:
        return []

    r = []
    q = [(0, n)]
    while q:
        level, x = q.pop()
        if len(r) == level:
            r.append([])
        r[level].append(x)
        if x.left:
            q = [(level+1, x.left)] + q

        if x.right:
            q = [(level+1, x.right)] + q

    for i in r:
        print i


if __name__ == '__main__':
    s = Solution()
    n4 = TreeNode(4)
    n2 = TreeNode(2)
    n7 = TreeNode(7)
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n6 = TreeNode(6)
    n9 = TreeNode(9)

    head = n4
    n4.left = n2
    n4.right = n7
    n2.left = n1
    n2.right = n3
    n7.left = n6
    n7.right = n9

    print_level(head)
    h = s.invertTree(head)
    print '-' * 6
    print_level(h)
