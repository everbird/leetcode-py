#!/usr/bin/env python3

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        r = []
        maxl = 0
        s = [root]
        while root.left:
            s.append(root.left)
            root = root.left
        
        pre = None
        cnt = 0
        while s:
            n = s.pop()
            if not pre or (pre and pre.val == n.val):
                cnt += 1
            else:
                cnt = 1

            if cnt > maxl:
                r = [n.val]
                maxl = cnt
            elif cnt == maxl:
                if n.val not in r:
                    r.append(n.val)

            pre = n

            if n.right:
                s.append(n.right)
                n = n.right

                while n.left:
                    s.append(n.left)
                    n = n.left

        return r
