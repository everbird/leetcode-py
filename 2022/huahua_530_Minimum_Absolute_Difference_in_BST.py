#!/usr/bin/env python3

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # inorder
        s = [root]
        while root.left:
            s.append(root.left)
            root = root.left

        mindiff = float('inf')
        pre = None
        while s:
            n = s.pop()
            if pre:
                mindiff = min(mindiff, abs(n.val - pre.val))

            pre = n

            if n.right:
                s.append(n.right)
                n = n.right

                while n.left:
                    s.append(n.left)
                    n = n.left

            
        return mindiff
