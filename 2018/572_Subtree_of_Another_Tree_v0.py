#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def isSubtree(self, s, t):
        q = [s]
        while q:
            node = q.pop()
            if compare(node, t):
                print '>>', node, t
                return True
            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return False


def compare(node, target):
    q = [(target, node)]
    while q:
        n, x = q.pop()
        if n.left:
            if not x.left:
                return False
            q.append((n.left, x.left))
        if n.val != x.val:
            return False
        if n.right:
            if not x.right:
                return False
            q.append((n.right, x.right))

    return n.left = x.left and n.right == x.r


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
                list_to_binary_tree([3,4,5,1,2]),
                list_to_binary_tree([4,1,2])
            ),
            True
        ),
        (
            (
                list_to_binary_tree([3,4,5,1,2, None, None, None, None, 0]),
                list_to_binary_tree([4,1,2])
            ),
            False
        ),
    ]
    for input_args, expected in tests:
        r = s.isSubtree(*input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
