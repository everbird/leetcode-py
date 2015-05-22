#!/usr/bin/env python
# encoding: utf-8


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        if not nums:
            return

        lenn = len(nums)
        b = 0
        e = lenn - 1
        mid = (b+e) / 2
        n = TreeNode(nums[mid])
        n.left = self.sortedArrayToBST(nums[:mid])
        n.right = self.sortedArrayToBST(nums[mid+1:])
        return n

    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)
        print root.val
        self.inorder(root.right)


if __name__ == '__main__':
    s = Solution()
    h = s.sortedArrayToBST([1,2,3,4,5,6,7,8,9])
    s.inorder(h)
