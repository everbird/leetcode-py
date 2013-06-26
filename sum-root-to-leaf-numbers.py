#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node(object):
    left = None
    right = None
    value = -1

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


sum_array = []
stack = []

def bfs(node):
    if not node:
        return

    stack.append(node.value)

    if not node.left and not node.right:
        _sum = int(''.join(map(str, stack)))
        sum_array.append(_sum)
        stack.pop()
        return

    if node.left:
        bfs(node.left)

    if node.right:
        bfs(node.right)

    stack.pop()


def leaf_sum(head):
    bfs(head)

    return sum(sum_array)


def run():
    n3 = Node(1)
    n2 = Node(6, right=n3)
    n1 = Node(3, right=n2)
    head = n1

    total = leaf_sum(head)

    print sum_array
    assert total==361, 'Failed, 4!=%s' % total


def main():
    run()

if __name__ == '__main__':
    main()
