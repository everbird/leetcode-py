#!/usr/bin/env python3

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        rs = []
        path = []
        preorder(root, targetSum, path, rs)
        return rs

def preorder(node, target, path, rs):
    if not node:
        return

    path.append(node.val)
    new_target = target - node.val
    if not node.left and not node.right and new_target == 0:
        rs.append(path[:])

    preorder(node.left, new_target, path, rs)
    preorder(node.right, new_target, path, rs)
    path.pop()
