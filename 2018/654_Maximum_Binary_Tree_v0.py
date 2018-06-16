#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None
        max_i, max_n = find_max(nums)
        node = TreeNode(max_n)
        left_nums = nums[:max_i]
        right_nums = nums[max_i+1:]
        node.left = self.constructMaximumBinaryTree(left_nums)
        node.right = self.constructMaximumBinaryTree(right_nums)
        return node

def find_max(nums):
    max_i = 0
    max_n = nums[0]
    for i, n in enumerate(nums):
        if n > max_n:
            max_n = n
            max_i = i
    return max_i, max_n


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
            [3,2,1,6,0,5],
            [6, 3, 5, None, 2, 0, None, None, 1],
        ),
    ]
    for input_args, expected in tests:
        r = s.constructMaximumBinaryTree(input_args)
        _r = binary_tree_to_list(r)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(_r == expected, input_args, _r, expected)
