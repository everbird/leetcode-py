#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def findTarget(self, root, k):
        s = set([])
        def inorder(node):
            if not node:
                return

            left = inorder(node.left)
            if left:
                return left
            v = k - node.val
            if v in s:
                return node
            else:
                s.add(node.val)
            right = inorder(node.right)
            if right:
                return right

        return bool(inorder(root))




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
                list_to_binary_tree([5,3,6,2,4,None,7]),
                9
            ),
            True
        ),
        (
            (
                list_to_binary_tree([5,3,6,2,4,None,7]),
                28
            ),
            False
        ),
    ]
    for input_args, expected in tests:
        r = s.findTarget(*input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
