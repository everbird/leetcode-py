#!/usr/bin/env python
# encoding: utf-8


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<{}>'.format(self.val)


class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        self.rs = [root] if root else []
        self.h = root
        self.visited = set([])

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return bool(self.rs)

    # @return an integer, the next smallest number
    def next(self):
        if not self.rs:
            return

        self.h = self.rs.pop()

        while self.h.left and self.h.left not in self.visited:
            if self.h.right and self.h.right not in self.visited:
                self.rs.append(self.h.right)
                self.visited.add(self.h.right)

            self.rs.append(self.h)

            self.h = self.h.left

        if self.h.right and self.h.right not in self.visited:
            self.rs.append(self.h.right)
            self.visited.add(self.h.right)

        self.visited.add(self.h)
        return self.h


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)

    r = n3
    n3.left = n1
    n1.right = n2
    n3.right = n5
    n5.left = n4
    s = BSTIterator(r)
    v = []
    while s.hasNext():
        v.append(s.next())
        print v
    print v

    s = BSTIterator(None)
    v = []
    while s.hasNext():
        v.append(s.next())
        print v
    print v
