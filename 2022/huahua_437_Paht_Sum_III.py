#!/usr/bin/env python3

class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        return path_number_from(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)



def path_number_from(node, target):
    if not node:
        return 0

    cnt = 0
    if node.val == target:
        cnt += 1

    cnt += path_number_from(node.left, target - node.val)
    cnt += path_number_from(node.right, target - node.val)
    return cnt
