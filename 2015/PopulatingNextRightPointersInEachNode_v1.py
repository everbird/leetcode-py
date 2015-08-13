#!/usr/bin/env python
# encoding: utf-8


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        return '<{}>'.format(self.val)


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        self.dfs(root)

    def dfs(self, root):
        if not root:
            return

        if root.left:
            root.left.next = root.right

        if root.next and root.right:
            root.right.next = root.next.left

        self.dfs(root.left)
        self.dfs(root.right)

    def levelorder(self, root):
        queue = [root]
        while queue:
            n = queue.pop()
            print n, n.val, n.next, '<<<'
            if n.left:
                queue = [n.left] + queue

            if n.right:
                queue = [n.right] + queue


if __name__ == '__main__':
    s = Solution()

    n1 = TreeLinkNode(1)
    n2 = TreeLinkNode(2)
    n3 = TreeLinkNode(3)
    n4 = TreeLinkNode(4)
    n5 = TreeLinkNode(5)
    n6 = TreeLinkNode(6)
    n7 = TreeLinkNode(7)

    root = n1
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    s.connect(root)
    s.levelorder(root)
