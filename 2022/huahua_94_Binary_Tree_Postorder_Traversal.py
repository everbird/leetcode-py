#!/usr/bin/env python3

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        s = [root]
        while s:
            n = s.pop()
            result.insert(0, n.val)

            if n.left:
                s.append(n.left)

            if n.right:
                s.append(n.right)

        return result
