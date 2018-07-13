#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def peakIndexInMountainArray(self, A):
        len_a = len(A)
        s, e = 0, len_a-1
        while s < e:
            i = (s + e) // 2
            if A[i-1] < A[i] > A[i+1]:
                return i
            elif A[i-1] < A[i]:
                s = i+1
            elif A[i] > A[i+1]:
                e = i-1

        return (s + e) // 2


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
            [0,1,0],
            1
        ),
        (
            [0,2,1,0],
            1
        ),
        (
            [18,29,38,59,98,100,99,98,90],
            5
        )
    ]
    for input_args, expected in tests:
        r = s.peakIndexInMountainArray(input_args)
        result = r == expected
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(result, input_args, r, expected)
