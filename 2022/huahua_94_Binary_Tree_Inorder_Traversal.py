#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s = []
        rs = []

        if not root:
            return []

        p = root
        while p:
            s.append(p)
            p = p.left

        while s:
            n = s.pop()
            rs.append(n.val)

            n = n.right
            while n:
                s.append(n)
                n = n.left

        return rs
