#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    index = 0
    def convertBST(self, root):
        r = []
        inorder(root, r)

        self.index = 0
        def inorder_w(node):
            if not node:
                return
            inorder_w(node.left)
            node.val += sum(r[self.index+1:])
            self.index += 1
            inorder_w(node.right)

        inorder_w(root)
        return root


def inorder(node, r):
    if not node:
        return
    inorder(node.left, r)
    r.append(node.val)
    inorder(node.right, r)


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
            list_to_binary_tree([5,2,13]),
            [18,20,13],
        ),
    ]
    for input_args, expected in tests:
        r = s.convertBST(input_args)
        r = binary_tree_to_list(r)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
