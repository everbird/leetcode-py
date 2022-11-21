#!/usr/bin/env python3

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        pre = None
        head = root
        while root:
            pre = root

            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            
        if val < pre.val:
            pre.left = TreeNode(val)
        else:
            pre.right = TreeNode(val)

        return head
