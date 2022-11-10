#!/usr/bin/env python3

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        while root and root.val < low:
            root = root.right

        while root and root.val > high:
            root = root.left

        return inorder(root, low, high)


def inorder(node, low, high):
    if not node:
        return

    if low <= node.val <= high:
        node.left = inorder(node.left, low, high)
        node.right = inorder(node.right, low, high)
        return node
    elif node.val < low:
        return inorder(node.right, low, high)
    elif node.val > high:
        return inorder(node.left, low, high)
