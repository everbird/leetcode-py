#!/usr/bin/env python3

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder
        cnt = 0
        s = [root]
        while root.left:
            s.append(root.left)
            root = root.left

        while s:
            n = s.pop()
            cnt += 1
            if cnt == k:
                break

            if n.right:
                s.append(n.right)
                n = n.right

                while n.left:
                    s.append(n.left)
                    n = n.left

        return n.val
