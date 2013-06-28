#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TreeNode(object):
    left = None
    right = None
    value = 0
    depth = 0

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_bst(array, upper, lower):
    if upper == lower + 1:
        b = TreeNode(array[lower])
        a = TreeNode(array[upper], left=b)
        return a

    if upper == lower:
        return TreeNode(array[upper])

    mid = (upper + lower) / 2
    left = build_bst(array, mid-1, lower) if mid-1>=0 else None
    right = build_bst(array, upper, mid+1) if mid+1<len(array) else None
    middle_node = TreeNode(array[mid], left=left, right=right)
    return middle_node


def run():
    array = range(10)

    if not array:
        return

    tree_head = build_bst(array, len(array) - 1, 0)

    print print_bst(tree_head)

    #Case 2: [3,5,8]
    array = [3,5,8]
    if not array:
        return

    tree_head = build_bst(array, len(array) - 1, 0)

    print print_bst(tree_head)


def print_bst(root):
    queue = []
    queue.append(root)
    pre = -1
    while queue:
        node = queue.pop(0)

        if node.depth != pre:
            print '\n',
        print node.value,


        if node.left:
            node.left.depth = node.depth + 1
            queue.append(node.left)
        if node.right:
            node.right.depth = node.depth + 1
            queue.append(node.right)

        pre = node.depth


if __name__ == '__main__':
    run()
