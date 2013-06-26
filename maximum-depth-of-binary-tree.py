#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node(object):
    left = None
    right = None
    value = 0

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

max_value = None

def max_depth(head):
    global max_value

    if not head:
        return 0

    pre_order(head, 1)
    return max_value


def pre_order(node, depth):
    global max_value
    if not node:
        return

    if not node.left and not node.right:
        if not max_value or max_value < depth:
            max_value = depth
        return

    if node.left:
        pre_order(node.left, depth+1)

    if node.right:
        pre_order(node.right, depth+1)


def run():
    a = Node(2)
    b = Node(1, left=a)
    head = b

    r = max_depth(head)
    assert r==2, 'Failed'
    print r



if __name__ == '__main__':
    run()
