#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def averageOfLevels(self, root):
        q = [root]
        r = []
        while q:
            v_sum = sum(n.val for n in q)
            r.append(float(v_sum) / len(q))
            q = reduce(
                lambda x,y: x+y,
                [
                    [x for x in [n.right, n.left] if x]
                    for n in q[::-1]
                ],
                []
            )
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
            list_to_binary_tree([3,9,20,None,None,15,7]),
            [3, 14.5, 11]
        ),
    ]
    for input_args, expected in tests:
        r = s.averageOfLevels(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
