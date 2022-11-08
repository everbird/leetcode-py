#!/usr/bin/env python3

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        rs = []
        _postorder(root, rs)
        return rs


def _postorder(node: 'Node', rs: List[int]) -> None:
    if not node:
        return

    for c in node.children:
        _postorder(c, rs)

    rs.append(node.val)
