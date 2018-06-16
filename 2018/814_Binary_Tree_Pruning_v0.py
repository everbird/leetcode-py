#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def pruneTree(self, root):
        prune(root, None, None)
        return root


def prune(root, parent, side):
    if not root:
        return False

    left_r = prune(root.left, parent=root, side=0)
    right_r = prune(root.right, parent=root, side=1)

    if root.val == 0:
        if not left_r and not right_r:
            if side == 0:
                parent.left = None
            elif side == 1:
                parent.right = None
        return left_r or right_r

    return True


def binary_tree_to_list(root):
    r = []
    q = [root]
    while q:
        n = q.pop()
        if n:
            r.append(n.val)
        else:
            r.append(None)

        if n and (n.left or n.right):
            q = [n.left] + q
            q = [n.right] + q
    return r


def list_to_binary_tree(values):
    len_n = len(values)
    root = TreeNode(values[0])
    q = [root]
    for i in range(1, len_n, 2):
        n = q.pop()
        left = TreeNode(values[i])
        n.left = left
        q = [left] + q
        if i+1 < len_n:
            right = TreeNode(values[i+1])
            n.right = right
            q = [right] + q
    return root


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode(val={})>'.format(self.val)


if __name__ == '__main__':
    # Tree 1
    root = TreeNode(1)
    node1 = TreeNode(0)
    node2 = TreeNode(0)
    node3 = TreeNode(1)
    root.right = node1
    node1.left = node2
    node1.right = node3
    r = binary_tree_to_list(root)
    print r

    s = Solution()
    r = s.pruneTree(root)
    r = binary_tree_to_list(root)
    print r

    # Tree 2
    root = TreeNode(1)
    node1 = TreeNode(0)
    node2 = TreeNode(1)
    node3 = TreeNode(0)
    node4 = TreeNode(0)
    node5 = TreeNode(0)
    node6 = TreeNode(1)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6
    r = binary_tree_to_list(root)
    print r

    s = Solution()
    r = s.pruneTree(root)
    r = binary_tree_to_list(root)
    print r

    # Tree 3
    root = TreeNode(1)
    node1 = TreeNode(1)
    node2 = TreeNode(0)
    node3 = TreeNode(1)
    node4 = TreeNode(1)
    node5 = TreeNode(0)
    node6 = TreeNode(1)
    node7 = TreeNode(0)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6
    node3.left = node7
    r = binary_tree_to_list(root)
    print r

    s = Solution()
    r = s.pruneTree(root)
    r = binary_tree_to_list(root)
    print r

    l1 = [1, None, 0, 0, 1]
    r = list_to_binary_tree(l1)
    x = binary_tree_to_list(r)
    print x
