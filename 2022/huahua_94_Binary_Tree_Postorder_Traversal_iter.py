#!/usr/bin/env python3

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        postorder(root, result)
        return result


def postorder(root: TreeNode, result: List[int]) -> None:
    if not root:
        return

    postorder(root.left, result)
    postorder(root.right, result)
    result.append(root.val)
