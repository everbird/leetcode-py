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


stack = []
found_flag = False

def searh_path(head, path_sum):
    global found_flag
    pre_order(head, path_sum)
    return found_flag


def pre_order(node, path_sum):
    global stack
    global found_flag

    if not node:
        return

    stack.append(node.value)

    if not node.left and not node.right:
        if sum(stack) == path_sum:
            found_flag = True
        stack.pop()
        return

    if node.left:
        pre_order(node.left, path_sum)

    if node.right:
        pre_order(node.right, path_sum)

    stack.pop()


def run():
    global stack
    global found_flag

    # Case 1
    stack = []
    found_flag = False
    a = Node(7)
    b = Node(2)
    c = Node(11, left=a, right=b)
    d = Node(4, left=c)
    e = Node(13)
    f = Node(1)
    g = Node(4, right=f)
    h = Node(8, left=e, right=g)
    i = Node(5, left=d, right=h)
    head = i

    r = searh_path(head, 22)

    assert r, 'Should be True but False'

    # Case 2: {1,2}, 3
    stack = []
    found_flag = False
    a = Node(2)
    b = Node(1, left=a)
    head = b

    r = searh_path(head, 3)

    assert r, 'Should be True but False'

    # Case 3: {-2,#,-3}, -5
    stack = []
    found_flag = False
    a = Node(-3)
    b = Node(-2, right=a)
    head = b

    r = searh_path(head, -5)

    assert r, 'Should be True but False'

    # Case 4: {1,-2,3}, -1
    stack = []
    found_flag = False
    a = Node(3)
    b = Node(-2)
    c = Node(1, left=b, right=a)
    head = c

    r = searh_path(head, -1)

    assert r, 'Should be True but False'

    # Case 5: {1,-2,-3,1,3,-2,#,-1}, 3
    stack = []
    found_flag = False
    a = Node(-1)
    b = Node(1, left=a)
    c = Node(3)
    d = Node(-2, left=b, right=c)
    e = Node(-2)
    f = Node(-3, left=e)
    g = Node(1, left=d, right=f)
    head = g

    r = searh_path(head, 3)

    assert not r, 'Should be False but True'


def main():
    run()


if __name__ == '__main__':
    main()
