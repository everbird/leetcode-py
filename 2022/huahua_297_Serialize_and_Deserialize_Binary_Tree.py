#!/usr/bin/env python3

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        rs = []
        serialize(root, rs)
        return '#'.join(map(str, rs))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        items = data.split('#')
        return deserialize(items)


def serialize(node, rs):
    if not node:
        rs.append('')
        return
    rs.append(node.val)
    serialize(node.left, rs)
    serialize(node.right, rs)


def deserialize(items):
    v = items.pop(0)
    if not v:
        return

    n = TreeNode(int(v))
    n.left = deserialize(items)
    n.right = deserialize(items)

    return n
