#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        inorder(root, result)
        return result

def inorder(node: TreeNode, result: List[int]) -> None:
    if not node:
        return
    inorder(node.left, result)
    result.append(node.val)
    inorder(node.right, result)
