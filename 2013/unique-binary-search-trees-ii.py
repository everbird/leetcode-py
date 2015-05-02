#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

class Node(object):
    left = None
    right = None
    value = 0

    def __init__(self, value, left=None, right=None):
        self.value = value;
        self.left = left
        self.right = right


def level_order(head):
    if not head:
        return []

    result = [[head.value],]

    queue = [head]
    while queue:
        next_line = []
        for i in range(len(queue)):
            node = queue.pop(0)

            if node.left:
                next_line.append(node.left)

            if node.right:
                next_line.append(node.right)

        queue = next_line
        if queue:
            result.append([n.value for n in queue])

    return result


def genTrees(n):
    r = []

    for i in range(n):
        _r = makeTrees(i, 0, n-1)
        r.extend(_r)

    return r

def makeTrees(root, start, end):
    r = []
    if start > end:
        return r;

    if start == end:
        return [Node(root+1)]

    left_r = []
    right_r = []

    for i in range(start, root):
        left_t = makeTrees(i, start, root-1)
        for x in left_t:
            new_left_h = Node(root+1)
            new_left_h.left = x
            left_r.append(new_left_h)

    for i in range(root+1, end+1):
        right_t = makeTrees(i, root+1, end)
        for x in right_t:
            new_right_h = Node(root+1)
            new_right_h.right = x
            right_r.append(new_right_h)

    if not left_r:
        return right_r

    if not right_r:
        return left_r

    for p in left_r:
        for q in right_r:
            new_p = copy.deepcopy(p)
            new_p.right = q.right
            r.append(new_p)

    return r


def run():
    heads = genTrees(4)

    for head in heads:
        r = level_order(head)
        print r


if __name__ == '__main__':
    run()
