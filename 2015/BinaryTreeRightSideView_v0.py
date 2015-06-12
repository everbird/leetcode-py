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

        queue = [(root, 0)]
        r = []
        while queue:
            n, level = queue.pop()
            if len(r) <= level:
                r.append([])

            r[level].append(n)

            if n.left:
                queue = [(n.left, level+1)] + queue

            if n.right:
                queue = [(n.right, level+1)] + queue

        return [x[-1].val for x in r]



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
