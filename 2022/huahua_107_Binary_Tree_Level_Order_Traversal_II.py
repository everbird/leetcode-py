#!/usr/bin/env python3

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = [(root, 0)]
        rs = []
        while q:
            n, lvl = q.pop(0)
            if len(rs) == lvl:
                rs.append([])
            rs[lvl].append(n.val)

            if n.left:
                q.append((n.left, lvl+1))

            if n.right:
                q.append((n.right, lvl+1))



        return rs[::-1]
