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

pre = None

def conver(head):
    pre_order(head)
    return head

def pre_order(node):
    global pre

    if not node:
        return

    left_node = node.left
    right_node = node.right

    if pre:
        pre.right = node
    #node.left = pre # This for double end linked list
    node.left = None
    pre = node

    if left_node:
        pre_order(left_node)

    if right_node:
        pre_order(right_node)


def run():
    a = Node(3)
    b = Node(4)
    c = Node(2, left=a, right=b)
    d = Node(6)
    e = Node(5, right=d)
    f = Node(1, left=c, right=e)
    head = f

    head = conver(head)

    while head:
        print head.value
        head = head.right


def main():
    run()

if __name__ == '__main__':
    main()
