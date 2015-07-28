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

    def sumNumbers(self, root):
        return sum(map(self.convert, self.find(root)))

    def find(self, root):
        if not root:
            return []

        if not root.left and not root.right:
            return [[root.val]]

        r = []
        left = self.find(root.left)
        right = self.find(root.right)
        for li in left:
            r.append([root.val]+li)

        for ri in right:
            r.append([root.val]+ri)

        return r

    def convert(self, array):
        lenn = len(array)
        s = 0
        count = 0
        for i in range(lenn-1, -1, -1):
            n = array[i]
            s += n*(10**count)
            count += 1

        return s


if __name__ == '__main__':
    s = Solution()

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    root = n1
    n1.left = n2
    n1.right = n3

    print s.sumNumbers(root)

    n1 = TreeNode(1)
    n2 = TreeNode(0)
    root = n1
    n1.left = n2

    print s.sumNumbers(root)

    print s.sumNumbers(None)

    n1 = TreeNode(4)
    n2 = TreeNode(9)
    n3 = TreeNode(0)
    n4 = TreeNode(1)
    root = n1
    n1.left = n2
    n1.right = n3
    n2.right = n4

    print s.sumNumbers(root)

    n1 = TreeNode(8)
    n2 = TreeNode(3)
    n3 = TreeNode(5)
    n4 = TreeNode(9)
    n5 = TreeNode(9)
    n6 = TreeNode(5)
    root = n1
    n1.left = n2
    n1.right = n3
    n2.right = n4
    n4.left = n5
    n4.right = n6

    print s.sumNumbers(root)

    n1 = TreeNode(5)
    n2 = TreeNode(3)
    n3 = TreeNode(2)
    n4 = TreeNode(7)
    n5 = TreeNode(0)
    n6 = TreeNode(6)
    n7 = TreeNode(0)
    root = n1
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n5.left = n7

    print s.sumNumbers(root)
