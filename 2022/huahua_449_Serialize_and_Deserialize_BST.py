#!/usr/bin/env python3

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''

        vals = []
        def _preorder(node):
            if not node:
                vals.append('')
                return
            vals.append(node.val)
            _preorder(node.left)
            _preorder(node.right)

        _preorder(root)
        return '#'.join(map(str, vals))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        vals = data.split('#')

        def _deseralized():
            val = vals.pop(0)
            if not val:
                return None

            n = TreeNode(int(val))

            left = _deseralized()
            right = _deseralized()
            n.left = left
            n.right = right

            return n

        return _deseralized()
