#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def printTree(self, root):
        if not root:
            return [['']]

        if not root.left and not root.right:
            return [[str(root.val)]]

        left = self.printTree(root.left)
        right = self.printTree(root.right)
        left_n = len(left)
        right_n = len(right)
        height = max(left_n, right_n)
        r = [[''] * len(left[0]) + [str(root.val)] + [''] * len(right[0])]
        for i in range(height):
            width = max(len(left[0]), len(right[0]))
            if i < left_n:
                left_line = left[i]
            else:
                left_line = [''] * width

            if i < right_n:
                right_line = right[i]
            else:
                right_line = [''] * width

            print left_line, right_line, '>>>', root
            r.append(left_line + [''] + right_line)
        return r


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
            list_to_binary_tree([1, 2]),
            [
                ['', '1', ''],
                ['2', '', ''],
            ]
        ),
        (
            list_to_binary_tree([1, 2, 3, None, 4]),
            [
                ["", "", "", "1", "", "", ""],
                ["", "2", "", "", "", "3", ""],
                ["", "", "4", "", "", "", ""]
            ]
        ),
        (
            list_to_binary_tree([1, 2, 5, 3, None, None, None, 4]),
            [
                ["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""],
                ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""],
                ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""],
                ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
            ]
        ),
    ]
    for input_args, expected in tests:
        r = s.printTree(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
