#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def distanceK(self, root, target, K):
        rs = []
        self.dfs(root)
        self.dfs_distance(rs, target, K)
        return rs

    def dfs(self, node, parent=None, direction=-1):
        if not node:
            return

        node.parent = parent
        node.parent_dir = direction

        self.dfs(node.left, node, 0)
        self.dfs(node.right, node, 1)

    def dfs_distance(self, rs, node, K, distance=0, direction=-1):
        if not node:
            return

        if K == distance:
            rs.append(node.val)
            return

        if direction != 0:
            self.dfs_distance(rs, node.left, K, distance+1)
        if direction != 1:
            self.dfs_distance(rs, node.right, K, distance+1)

        self.dfs_distance(rs, node.parent, K, distance+1, node.parent_dir)


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

    r1 = list_to_binary_tree([3,5,1,6,2,0,8,None,None,7,4])
    tests = [
        (
            (
                r1,
                r1.left,
                2
            ),
            [7, 4, 1]
        ),
    ]
    for input_args, expected in tests:
        r = s.distanceK(*input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
