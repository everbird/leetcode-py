#!/usr/bin/env python3

from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        rs = []
        c = defaultdict(int)
        def _sum(node):
            nonlocal c
            if not node:
                return 0

            left = _sum(node.left)
            right = _sum(node.right)
            v = node.val + left + right
            c[v] += 1

            return v

        _sum(root)
        max_v = max(c.values())
        for k, v in c.items():
            if v == max_v:
                rs.append(k)

        return rs
