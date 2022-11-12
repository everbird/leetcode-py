#!/usr/bin/env python3

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        r = 0
        path = []
        def preorder(node):
            nonlocal r
            if not node:
                return

            path.append(node.val)
            if not node.left and not node.right:
                r += to_num(path)

            preorder(node.left)
            preorder(node.right)

            path.pop()

        preorder(root)
        return r

def to_num(path):
    if not path:
        return 0

    r = 0
    for x in path:
        r = r*10 + x

    return r
