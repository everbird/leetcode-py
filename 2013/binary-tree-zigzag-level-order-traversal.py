#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node(object):
    left = None
    right = None
    value = 0

    def __init__(self, value, left=None, right=None):
        self.value = value;
        self.left = left
        self.right = right


def zigzag_level_order(head):
    if not head:
        return []

    result = [[head.value],]

    queue = [head]
    order_flag = False
    while queue:
        next_line = []
        for i in range(len(queue)):
            node = queue.pop(0)

            if node.left:
                next_line.append(node.left)

            if node.right:
                next_line.append(node.right)

        queue = next_line
        if not order_flag:
            queue.reverse()

        if queue:
            result.append([n.value for n in queue])

        order_flag = not order_flag

    return result


def run():
    a = Node(15)
    b = Node(7)
    c = Node(20, left=a, right=b)
    d = Node(9)
    e = Node(3, left=d, right=c)
    head = e

    r = zigzag_level_order(head)
    print r


if __name__ == '__main__':
    run()
