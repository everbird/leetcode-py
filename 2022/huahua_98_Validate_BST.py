#!/usr/bin/env python3

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inorder
        s = [root]
        while root.left:
            s.append(root.left)
            root = root.left

        pre = None
        while s:
            n = s.pop()

            if pre and pre.val >= n.val:
                return False
            
            pre = n

            if n.right:
                s.append(n.right)
                n = n.right

                while n.left:
                    s.append(n.left)
                    n = n.left

        return True
