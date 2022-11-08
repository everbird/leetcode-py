#!/usr/bin/env python3

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if not root:
            return reulst

        s = [root]
        while s:
            n = s.pop()
            result.append(n.val)
            if n.right:
                s.append(n.right)

            if n.left:
                s.append(n.left)

        return result
