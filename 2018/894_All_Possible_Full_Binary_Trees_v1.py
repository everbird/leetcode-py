#!/usr/bin/env python
# encoding: utf-8



class Solution(object):

    def allPossibleFBT(self, N):
        if N == 0:
            return []
        elif N == 1:
            return [TreeNode(0)]

        r = []
        children_cnt = N - 1
        for left_cnt in xrange(1, min(20, children_cnt), 2):
            right_cnt = children_cnt - left_cnt
            for left in self.allPossibleFBT(left_cnt):
                for right in self.allPossibleFBT(right_cnt):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    r.append(root)

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
