#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def widthOfBinaryTree(self, root):
        q = [(root, 1)]
        width = 0
        while q:
            width = max(width, q[-1][1] - q[0][1] + 1)
            _q = []
            for node, index in q:
                for i, _next in enumerate([node.left, node.right], 2*index):
                    if _next:
                        _q.append((_next, i))
            q = _q
        return width


def binary_tree_to_list(root):
    r = []
    q = [root]
    target_length = length = 0
    while q:
        n = q.pop()
        length += 1
        if n:
            r.append(n.val)
            target_length = length
        else:
            r.append(None)

        if n:
            q = [n.right, n.left] + q

    return r[:target_length]


def list_to_binary_tree(values):
    len_n = len(values)
    root = TreeNode(values[0])
    q = [root]
    for i in range(1, len_n, 2):
        n = q.pop()
        v = values[i]
        left = TreeNode(v) if v else None
        n.left = left
        if left:
            q = [left] + q
        if i+1 < len_n:
            v = values[i+1]
            right = TreeNode(v) if v else None
            n.right = right
            if right:
                q = [right] + q
    return root


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode(val={})>'.format(self.val)


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            list_to_binary_tree([1, 3, 2, 5, 3, None, 9]),
            4
        ),
        (
            list_to_binary_tree([1, 3, None, 5, 3]),
            2
        ),
        (
            list_to_binary_tree([1, 3, 2, 5]),
            2
        ),
        (
            list_to_binary_tree([1, 3, 2, 5, None, None, 9, 6, None, None, 7]),
            8
        ),
        (
            list_to_binary_tree([1,1,1,1,1,1,1,None,None,None,1,None,None,None,None,2,2,2,2,2,2,2,None,2,None,None,2,None,2]),
            8
        )
    ]
    for input_args, expected in tests:
        r = s.widthOfBinaryTree(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)

    r = list_to_binary_tree([1, 3, 2, 5, None, None, 9, 6, None, None, 7])
    x = binary_tree_to_list(r)
    print x

    r = list_to_binary_tree([1,1,1,1,1,1,1,None,None,None,1,None,None,None,None,2,2,2,2,2,2,2,None,2,None,None,2,None,2])
    x = binary_tree_to_list(r)
    print x
