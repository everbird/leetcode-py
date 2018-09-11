#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def constructFromPrePost(self, pre, post):
        return construct(pre, post)


def construct(pre, post):
    if not pre or not post:
        return

    root = TreeNode(pre[0])

    if len(pre) > 1:
        left = pre[1]
        right = post[-2]
        if left == right:
            node = construct(pre[1:], post[:-1])
            root.left = node  # Always add to left
        else:
            i = pre.index(right)
            left_pre = pre[1:i]
            right_pre = pre[i:]

            j = post.index(left)
            left_post = post[:j+1]
            right_post = post[j+1:-1]
            left_node = construct(left_pre, left_post)
            right_node = construct(right_pre, right_post)
            root.left = left_node
            root.right = right_node

    return root


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
                [1,2,4,5,3,6,7],
                [4,5,2,6,7,3,1]
            ),
            [1,2,3,4,5,6,7]
        ),
    ]
    for input_args, expected in tests:
        r = s.constructFromPrePost(*input_args)
        r = binary_tree_to_list(r)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
