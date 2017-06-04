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
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []

        return self.dfs(str(root.val), root)

    def dfs(self, prefix, pnode):
        if pnode.left is None and pnode.right is None:
            return [prefix]

        r = []
        if pnode.left:
            r += self.dfs('{}->{}'.format(prefix, pnode.left.val), pnode.left)

        if pnode.right:
            r += self.dfs('{}->{}'.format(prefix, pnode.right.val), pnode.right)

        return r


def main():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    n2.right = n5
    s = Solution()
    print s.binaryTreePaths(n1)

if __name__ == '__main__':
    main()
