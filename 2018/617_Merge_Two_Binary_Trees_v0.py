#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def mergeTrees(self, t1, t2):
        if not t1:
            return t2
        if not t2:
            return t1
        q1 = [(t1, None, -1)]
        q2 = [(t2, None, -1)]
        while q1:
            n1, p1, d1 = q1.pop()
            n2, p2, d2 = q2.pop()

            n2.val += n1.val

            if n1.left and n2.left:
                q1 = [(n1.left, n1, 0)] + q1
                q2 = [(n2.left, n2, 0)] + q2
            elif n1.left and not n2.left:
                n2.left = n1.left

            if n1.right and n2.right:
                q1 = [(n1.right, n1, 1)] + q1
                q2 = [(n2.right, n2, 1)] + q2
            elif n1.right and not n2.right:
                n2.right = n1.right

        return t2



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
                list_to_binary_tree([1,3,2,5]),
                list_to_binary_tree([2,1,3,None,4,None,7])
            ),
            [3,4,5,5,4,None,7]
        ),
        (
            (
                list_to_binary_tree([3,4,5,1,2]),
                list_to_binary_tree([4,1,2])
            ),
            [7,5,7,1,2]
        ),
    ]
    for input_args, expected in tests:
        r = s.mergeTrees(*input_args)
        r = binary_tree_to_list(r)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
