#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def trimBST(self, root, L, R):
        while root.val < L:
            root = root.right

        while root.val > R:
            root = root.left

        return traverse(root, L, R)


def traverse(node, L, R):
    if not node:
        return

    if L <= node.val <= R:
        node.left = traverse(node.left, L, R)
        node.right = traverse(node.right, L, R)
        return node
    elif node.val > R:
        return traverse(node.left, L, R)
    elif node.val < L:
        return traverse(node.right, L, R)


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
            (
                list_to_binary_tree([1,0,2]),
                1,
                2
            ),
            [1,None,2]
        ),
        #(
        #    (
        #        list_to_binary_tree([3,0,4,None,2,None,None,1]),
        #        1,
        #        3
        #    ),
        #    [3,2,None,1]
        #),
    ]
    for input_args, expected in tests:
        r = s.trimBST(*input_args)
        r = binary_tree_to_list(r)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
