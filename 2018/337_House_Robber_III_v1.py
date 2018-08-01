#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    cache = {}
    def rob(self, root):
        self.cache = {}
        return max(
            self._rob(root, selected=False),
            self._rob(root, selected=True),
        )


    def _rob(self, node, selected=False):
        if not node:
            return 0

        if (node, selected) in self.cache:
            return self.cache[(node, selected)]
        if selected:
            return node.val + self._rob(node.left, selected=False) + self._rob(node.right, selected=False)

        left_v = max(
            self._rob(node.left, selected=False),
            self._rob(node.left, selected=True),
        )
        right_v = max(
            self._rob(node.right, selected=False),
            self._rob(node.right, selected=True),
        )
        r = left_v + right_v
        self.cache[(node, selected)] = r
        return  r


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
            list_to_binary_tree([3,2,3,None,3,None,1]),
            7
        ),
        (
            list_to_binary_tree([3,4,5,1,3,None,1]),
            9
        ),
    ]
    for input_args, expected in tests:
        r = s.rob(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
