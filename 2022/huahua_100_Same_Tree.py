#!/usr/bin/env python3

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return is_same_tree(p, q)


def is_same_tree(t1, t2):
    if not t1 and not t2:
        return True
    elif not t1 or not t2:
        return False

    if t1.val != t2.val:
        return False

    return is_same_tree(t1.left, t2.left) and is_same_tree(t1.right, t2.right)
