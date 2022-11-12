#!/usr/bin/env python3

class Solution:
    cache = {}

    def __init__(self):
        self.cache = {}

    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        v = self.cache.get(id(root))
        if v is not None:
            return v

        a = root.val
        if root.left:
            a += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            a += self.rob(root.right.left) + self.rob(root.right.right)

        b = self.rob(root.left) + self.rob(root.right)

        r = max(a, b)
        self.cache[id(root)] = r
        return r
