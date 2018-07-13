#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def findDuplicateSubtrees(self, root):
        d = {}
        get_tree_id(root, d)
        return [i[1] for i in d.values() if i[0] > 1]


def get_tree_id(root, d):
    if not root:
        return None

    tree_id = (root.val, get_tree_id(root.left, d), get_tree_id(root.right, d))
    r = d.get(tree_id)
    if not r:
        d[tree_id] = (1, root)
    else:
        d[tree_id] = (r[0]+1, root)

    return tree_id


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
            list_to_binary_tree([1, 2, 3, 4, None, 2, 4, None, None, 4]),
            [
                list_to_binary_tree([2, 4]),
                list_to_binary_tree([4])
            ],
        ),
    ]
    for input_args, expected in tests:
        r = s.findDuplicateSubtrees(input_args)
        r_list = sorted([binary_tree_to_list(x) for x in r])
        e_list = sorted([binary_tree_to_list(x) for x in expected])
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r_list == e_list, input_args, r_list, e_list)
