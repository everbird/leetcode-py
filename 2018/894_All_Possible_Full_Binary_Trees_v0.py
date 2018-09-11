#!/usr/bin/env python
# encoding: utf-8


import copy


class Solution(object):

    def allPossibleFBT(self, N):
        if N % 2 == 0:
            return []

        root = TreeNode(0)
        q = [(root, 1)]

        while q:
            if q[-1][-1] == N:
                return [x[0] for x in q]

            root_node, n = q.pop()

            def postorder(node, n):
                if not node:
                    return

                postorder(node.left, n)
                postorder(node.right, n)

                if not node.left and not node.right:
                    node.left = TreeNode(0)
                    node.right = TreeNode(0)
                    _root = copy_tree(root_node)
                    q.insert(0, (_root, n+2))
                    node.left = None
                    node.right = None

            postorder(root_node, n)


def copy_tree(root):
    if not root:
        return

    new_root = TreeNode(0)
    new_root.left = copy_tree(root.left)
    new_root.right = copy_tree(root.right)

    return new_root


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
            7,
            [
                [0,0,0,None,None,0,0,None,None,0,0],
                [0,0,0,None,None,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,None,None,None,None,0,0],
                [0,0,0,0,0,None,None,0,0],
            ]
        ),
    ]
    for input_args, expected in tests:
        r = s.allPossibleFBT(input_args)
        r = [binary_tree_to_list(x) for x in r]
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
