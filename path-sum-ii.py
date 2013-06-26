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
results = []

def searh_path(head, path_sum):
    global results
    pre_order(head, path_sum)
    return results


def pre_order(node, path_sum):
    global stack
    global results

    if not node:
        return

    stack.append(node.value)

    if not node.left and not node.right:
        if sum(stack) == path_sum:
            results.append(stack[:])
        stack.pop()
        return

    if node.left:
        pre_order(node.left, path_sum)

    if node.right:
        pre_order(node.right, path_sum)

    stack.pop()


def run():
    global stack
    global results

    # Case 1
    stack = []
    results = []
    a = Node(7)
    b = Node(2)
    c = Node(11, left=a, right=b)
    d = Node(4, left=c)
    e = Node(5)
    f = Node(1)
    g = Node(4, left=e, right=f)
    h = Node(13)
    i = Node(8, left=h, right=g)
    j = Node(5, left=d, right=i)
    head = j

    r = searh_path(head, 22)

    assert r==[
            [5,4,11,2],
            [5,8,4,5],
            ], 'Not correct: %s' % r
    print 'Case 1 pass'

    # Case 2: {1,2}, 3
    stack = []
    results = []
    a = Node(2)
    b = Node(1, left=a)
    head = b

    r = searh_path(head, 3)

    assert r==[[1,2]], 'Not correct: %s' % r
    print 'Case 2 pass'

    # Case 3: {-2,#,-3}, -5
    stack = []
    results = []
    a = Node(-3)
    b = Node(-2, right=a)
    head = b

    r = searh_path(head, -5)

    assert r==[[-2,-3]], 'Not correct: %s' % r
    print 'Case 3 pass'

    # Case 4: {1,-2,3}, -1
    stack = []
    results = []
    a = Node(3)
    b = Node(-2)
    c = Node(1, left=b, right=a)
    head = c

    r = searh_path(head, -1)

    assert r==[[1,-2]], 'Not correct: %s' % r
    print 'Case 4 pass'

    # Case 5: {1,-2,-3,1,3,-2,#,-1}, 3
    stack = []
    results = []
    a = Node(-1)
    b = Node(1, left=a)
    c = Node(3)
    d = Node(-2, left=b, right=c)
    e = Node(-2)
    f = Node(-3, left=e)
    g = Node(1, left=d, right=f)
    head = g

    r = searh_path(head, 3)

    assert r==[], 'Not correct: %s' % r
    print 'Case 5 pass'


def main():
    run()


if __name__ == '__main__':
    main()
