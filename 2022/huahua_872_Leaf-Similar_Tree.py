#!/usr/bin/env python3

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r1 = []
        inorder(root1, r1)

        r2 = []
        inorder(root2, r2)

        return r1 == r2

def inorder(node, rs):
    if not node:
        return

    inorder(node.left, rs)
    if not node.left and not node.right:
        rs.append(node.val)
    inorder(node.right, rs)
