#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def findSecondMinimumValue(self, root):
        min1 = root.val
        r = {'min2': float('inf')}
        dfs(root, min1, r)
        r = r['min2']
        return r if r < float('inf') else -1


def dfs(node, min1, d):
    if not node:
        return

    if node.val == min1:
        dfs(node.left, min1, d)
        dfs(node.right, min1, d)
    elif min1 < node.val < d['min2']:
        d['min2'] = node.val



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
            list_to_binary_tree([2,2,5,None,None,5,7]),
            5
        ),
        (
            list_to_binary_tree([2,2,2]),
            -1
        ),
    ]
    for input_args, expected in tests:
        r = s.findSecondMinimumValue(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
