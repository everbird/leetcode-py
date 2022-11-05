#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    pre = None

    def increasingBST(self, root):
        if not root:
            return

        nodes = []

        def inorder(n):
            if n.left:
                inorder(n.left)

            nodes.append(n)

            if n.right:
                inorder(n.right)

        inorder(root)
        self.pre = None
        for n in nodes:
            if self.pre:
                self.pre.left = None
                self.pre.right = n
            self.pre = n

        return nodes[0]




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
            list_to_binary_tree([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]),
            [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]
        ),
    ]
    for input_args, expected in tests:
        r = s.increasingBST(input_args)
        r = binary_tree_to_list(r)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
