#!/usr/bin/env python3

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        preorder(root, result)
        return result


def preorder(root: TreeNode, result: List[int]) -> None:
    if not root:
        return

    result.append(root.val)
    preorder(root.left, result)
    preorder(root.right, result)
