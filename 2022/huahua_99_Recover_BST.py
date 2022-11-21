#!/usr/bin/env python3

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        return recover_bst(root)
        
        
def recover_bst(root):
    head = root
    s = [root]
    while root.left:
        s.append(root.left)
        root = root.left

    pre = None
    p1 = p2 = None
    while s:
        n = s.pop()
        if pre and pre.val > n.val:
            if not p1:
                p1 = pre

            p2 = n
        pre = n

        if n.right:
            s.append(n.right)
            n = n.right

            while n.left:
                s.append(n.left)
                n = n.left

    p1.val, p2.val = p2.val, p1.val
