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

longest_path_sum = None

def get_max_path(head):
    global longest_path_sum
    find_longest_startwith(head)
    return longest_path_sum


def find_longest_startwith(node):
    if not node:
        return 0

    global longest_path_sum

    items = [0]
    left_length = find_longest_startwith(node.left)
    right_length = find_longest_startwith(node.right)

    _ = max(
            node.value + left_length + right_length,
            node.value + left_length,
            node.value + right_length,
            node.value
            )
    longest_path_sum = max(longest_path_sum, _)

    if left_length > 0:
        items.append(left_length)

    if right_length > 0:
        items.append(right_length)

    return max(map(lambda x: x+node.value, items))



def run():
    global max_item
    global longest_path_sum
    # Case 1
    max_item = None
    longest_path_sum = None
    n2 = Node(2)
    n7 = Node(7)
    n11 = Node(11, left=n7, right=n2)
    n4 = Node(4, left=n11)
    n1 = Node(1)
    n13 = Node(13)
    n4_ = Node(4, right=n1)
    n8 = Node(8, left=n13, right=n4_)
    n5 = Node(5, left=n4, right=n8)
    head = n5

    max_sum_path = get_max_path(head)

    assert max_sum_path==48, 'Expected 48 but %s' % max_sum_path
    print max_sum_path

    # Case 2
    max_item = None
    longest_path_sum = None
    a = Node(-1)
    b = Node(-2, left=a)
    head = b

    max_sum_path = get_max_path(head)

    assert max_sum_path==-1, 'Expected -1 but %s' % max_sum_path
    print max_sum_path

    # Case 3
    max_item = None
    longest_path_sum = None
    a = Node(-1)
    b = Node(2, left=a)
    head = b

    max_sum_path = get_max_path(head)

    assert max_sum_path==2, 'Expected 2 but %s' % max_sum_path
    print max_sum_path

    # Case 4 {1,-2,-3,1,3,-2,#,-1} expected 3
    max_item = None
    longest_path_sum = None
    a = Node(-1)
    b = Node(1, left=a)
    c = Node(3)
    d = Node(-2, left=b, right=c)
    e = Node(-2)
    f = Node(-3, left=e)
    g = Node(1, left=d, right=f)
    head = g

    max_sum_path = get_max_path(head)

    assert max_sum_path==3, 'Expected 3 but %s' % max_sum_path
    print max_sum_path


def main():
    run()

if __name__ == '__main__':
    main()
