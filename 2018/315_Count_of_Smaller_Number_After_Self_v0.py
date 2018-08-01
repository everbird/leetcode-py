#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def countSmaller(self, nums):
        if not nums:
            return []
        n = len(nums)
        r = [0] * n
        root = TreeNode(nums[-1])
        for i in range(n-2, -1, -1):
            cnt = insert_bst(root, nums[i])
            r[i] = cnt

        return r


def insert_bst(root, val):
    node = root
    cnt = 0
    while node:
        if val <= node.val:
            node.count += 1
            if node.left:
                node = node.left
            else:
                node.left = TreeNode(val)
                break
        else:
            cnt += node.count
            if node.right:
                node = node.right
            else:
                node.right = TreeNode(val)
                break

    return cnt


class TreeNode(object):
    left = None
    right = None
    count = 1
    def __init__(self, val):
        self.val = val


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [5,2,6,1],
            [2,1,1,0]
        ),
    ]
    f = s.countSmaller
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
