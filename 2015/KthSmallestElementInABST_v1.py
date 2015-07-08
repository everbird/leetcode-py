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
    # @param {integer} k
    # @return {integer}
    array = []

    def kthSmallest(self, root, k):
        self.array = []
        self.inorder(root, k)
        return self.array[k-1].val

    def inorder(self, root, k):
        if not root or len(self.array) == k:
            return

        self.inorder(root.left, k)
        self.array.append(root)
        self.inorder(root.right, k)

def print_lvl(root):
    r = []
    queue = [(0, root)]
    while queue:
        lvl, n = queue.pop()
        if len(r) >= lvl:
            r.append([])

        r[lvl].append(n)
        if n.left:
            queue = [(lvl+1, n.left)] + queue

        if n.right:
            queue = [(lvl+1, n.right)] + queue

    for li in r:
        for i in li:
            print i,
        print '\n'


if __name__ == '__main__':
    s = Solution()
    n1 = TreeNode(5)
    n2 = TreeNode(3)
    n3 = TreeNode(1)
    n4 = TreeNode(2)
    n5 = TreeNode(6)
    n1.left = n4
    n1.right = n5
    n4.left = n3
    n4.right = n2
    root = n1

    print_lvl(root)
    print '>>>', s.kthSmallest(root, 3)
    print_lvl(root)

    print '-' * 6
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n1.right = n2
    root = n1

    print_lvl(root)
    print '>>>', s.kthSmallest(root, 2)
    print_lvl(root)
