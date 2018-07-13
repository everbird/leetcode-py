#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def deleteNode(self, root, key):
        if not root:
            return

        _root = root
        parent = None
        while root and root.val != key:
            if key < root.val:
                parent = root
                root = root.left
            elif key > root.val:
                parent = root
                root = root.right

        if not root:
            return _root

        if not root.left and not root.right:
            new_root = None
        elif not root.left:
            new_root = root.right
        elif not root.right:
            new_root = root.left
        else:
            right_min = root.right
            p = root
            while right_min.left:
                p = right_min
                right_min = right_min.left

            right_min.left = root.left
            if right_min != root.right:
                p.left = right_min.right
                right_min.right = root.right
            new_root = right_min

        if not parent:
            return new_root

        if parent.left == root:
            parent.left = new_root
        else:
            parent.right = new_root
        return _root





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
                3
            ),
            [5,4,6,2,None,None,7],
        ),
        (
            (
                list_to_binary_tree([5,3,6,2,4,None,7]),
                0
            ),
            [5,3,6,2,4,None,7],
        ),
    ]
    for input_args, expected in tests:
        r = s.deleteNode(*input_args)
        _r = binary_tree_to_list(r)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(_r == expected, input_args, _r, expected)
