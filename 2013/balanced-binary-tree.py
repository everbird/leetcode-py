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


result = True
def is_balanced(head):
    if not head:
        return 0

    global result
    result = True
    get_depth(head)
    return result


def get_depth(node):
    global result
    if not node:
        return 0

    left = get_depth(node.left)
    right = get_depth(node.right)
    if 1 < abs(left - right):
        result = False

    return 1 + max(left, right)


def run():
    # Case 1:
    a = Node(2)
    b = Node(1, right=a)
    head = b

    r = is_balanced(head)
    assert r, 'Failed'
    print r

    #Case 2:{3,2,#,1} should be false
    a = Node(1)
    b = Node(2, left=a)
    c = Node(3, left=b)
    head = c

    r = is_balanced(head)
    assert not r, 'Failed'
    print r

    #Case 3: {1} should be true
    a = Node(1)
    head =a

    r = is_balanced(head)
    assert r, 'Failed'
    print r

    #Case 4: {1,2,2,3,#,#,3,4,#,#,4} should be false
    a = Node(4)
    b = Node(4)
    c = Node(3, left=a)
    d = Node(3, right=b)
    e = Node(2, left=c)
    f = Node(2, right=d)
    g = Node(1, left=e, right=f)
    head = g

    r = is_balanced(head)
    assert not r, 'Failed'
    print r


if __name__ == '__main__':
    run()
