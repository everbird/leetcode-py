#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def increasingBST(self, root):
        if not root:
            return

        pre = None
        head = None
        for n in iterative_inorder(root):
            if not head:
                head = n

            if pre:
                pre.right = n
            n.left = None
            pre = n

        return head


def iterative_inorder(n):
    q = [n]
    while q:

        while n.left:
            q.append(n.left)
            n = n.left

        while q:
            n = q.pop()

            yield n

            if n.right:
                q.append(n.right)
                n = n.right
                break


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
        (
            list_to_binary_tree([2, 1]),
            [1, None, 2]
        ),
    ]
    for input_args, expected in tests:
        r = s.increasingBST(input_args)
        r = binary_tree_to_list(r)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
