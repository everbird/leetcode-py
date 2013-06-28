#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ListNode(object):
    next = None
    value = 0

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TreeNode(object):
    left = None
    right = None
    value = 0
    depth = 0

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_bst(node, start, end):
    if start > end:
        return None, node

    mid = (start + end) / 2
    left, node = build_bst(node, start, mid-1)
    parent = TreeNode(node.value, left=left)
    node = node.next
    parent.right, node = build_bst(node, mid+1, end)
    return parent, node


def get_list_length(head):
    length = 0
    node = head
    while node:
        node = node.next
        length += 1

    return length


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


def run():
    a = ListNode(3)
    b = ListNode(2, next=a)
    c = ListNode(1, next=b)
    head = c

    length = get_list_length(head)
    tree_head, _ = build_bst(head, 0, length - 1)

    print print_bst(tree_head)


if __name__ == '__main__':
    run()
