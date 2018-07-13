#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def longestUnivaluePath(self, root):
        r = {'max': 0}

        def update_max(v, d):
            if v > d['max']:
                d['max'] = v

        def traverse(root, d):
            if not root:
                return 0

            left_p = traverse(root.left, d)
            left_same = root.left and root.left.val == root.val
            left_p = left_p + 1 if left_same else 0

            right_p = traverse(root.right, d)
            right_same = root.right and root.right.val == root.val
            right_p = right_p + 1 if right_same else 0

            update_max(left_p+right_p, d)

            return max(left_p, right_p)

        traverse(root, r)
        return r['max']



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
            list_to_binary_tree([5,4,5,1,1,None,5]),
            2
        ),
        (
            list_to_binary_tree([1,4,5,4,4,None,5]),
            2
        ),
        (
            list_to_binary_tree([1]),
            0
        ),
    ]
    for input_args, expected in tests:
        r = s.longestUnivaluePath(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
