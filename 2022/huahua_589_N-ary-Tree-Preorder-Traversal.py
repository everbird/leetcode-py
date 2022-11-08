#!/usr/bin/env python3

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        rs = []
        _preorder(root, rs)
        return rs


def _preorder(node: 'Node', rs: List[int]) -> None:
    if not node:
        return

    rs.append(node.val)
    for c in node.children:
        _preorder(c, rs)
