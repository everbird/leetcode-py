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
        nums = self._get_numbers(root)
        return sum(map(int, nums))

    def _get_numbers(self, root):
        if not root:
            return []

        r = []
        v = root.val
        lns = self._get_numbers(root.left)
        rns = self._get_numbers(root.right)
        if not lns and not rns:
            return [str(v)]

        for ln in lns:
            r.append(str(v)+ln)

        for rn in rns:
            r.append(str(v)+rn)

        return r


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
