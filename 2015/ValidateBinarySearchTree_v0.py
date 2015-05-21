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
    # @return {boolean}
    def isValidBST(self, root):
        r = True
        if not root:
            return True

        if root.left:
            max_n = self.get_max(root.left)
            if max_n.val >= root.val:
                return False

            r = r and self.isValidBST(root.left)

        if root.right:
            min_n = self.get_min(root.right)
            if min_n.val <= root.val:
                return False

            r = r and self.isValidBST(root.right)

        return r

    def get_min(self, root):
        if not root:
            return

        ln = root
        rn = root
        n = self.get_min(root.left)
        if n and root.val > n.val:
            ln = n

        n = self.get_min(root.right)
        if n and root.val > n.val:
            rn = n

        if not ln:
            return rn
        if not rn:
            return ln

        return ln if ln.val < rn.val else rn

    def get_max(self, root):
        if not root:
            return

        ln = root
        rn = root
        n = self.get_max(root.left)
        if n and root.val < n.val:
            ln = n

        n = self.get_max(root.right)
        if n and root.val < n.val:
            rn = n

        if not ln:
            return rn
        if not rn:
            return ln

        return ln if ln.val > rn.val else rn


if __name__ == '__main__':
    s = Solution()

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    root = n1
    n1.right = n2
    n2.left = n3

    print s.isValidBST(root)
