#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def printTree(self, root):
        if not root:
            return [['']]

        depth = get_depth(root)
        width = 2**depth - 1
        line = [''] * width
        m = []
        for i in range(depth):
            m.append(list(line))

        def fill(root, level, index, m):
            if not root:
                return

            m[level-1][index] = str(root.val)

            step = (width+1) // 2**(level+1)
            fill(root.left, level+1, index-step, m)
            fill(root.right, level+1, index+step, m)

        fill(root, 1, width//2, m)
        return m


def get_depth(root, current_depth=0):
    if not root:
        return current_depth

    return max(
        get_depth(root.left, current_depth+1),
        get_depth(root.right, current_depth+1)
    )


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
