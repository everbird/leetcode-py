#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    cnt = 0
    def pathSum(self, root, sum):
        self.cnt = 0
        self.preorder(root, [sum], sum)
        return self.cnt

    def preorder(self, node, targets, s):
        if not node:
            return
        for t in targets:
            if node.val == t:
                self.cnt += 1
        for i in range(len(targets)):
            targets[i] -= node.val

        targets.append(s)
        self.preorder(node.left, targets[:], s)
        self.preorder(node.right, targets[:], s)


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
                list_to_binary_tree([10,5,-3,3,2,None,11,3,-2,None,1]),
                8
            ),
            3
        ),
        (
            (
                list_to_binary_tree([0,1,1]),
                1
            ),
            4
        ),
    ]
    for input_args, expected in tests:
        r = s.pathSum(*input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
