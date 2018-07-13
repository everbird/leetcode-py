#!/usr/bin/eni python
# encoding: utf-8


from operator import itemgetter


class Solution(object):
    def carFleet(self, target, position, speed):
        if not position or not speed:
            return 0

        cars = sorted(zip(position, speed), key=itemgetter(0), reverse=True)
        times_to_target = [(target - p)/float(s) for p, s in cars]
        t = times_to_target[0]
        fleet = 1
        for i, _t in enumerate(times_to_target[1:], 1):
            if _t > t:
                fleet += 1
                t = _t

        return fleet



# 10,8,0,5,3
# 2,4,1,1,3
# 0 3 5 8 10
# 1 3 1 4 2
# 0 3 5 7 8 10
# 1 3 1 3 4 2
# 0 3 5 7 8 10
# 1 3 1 5 4 2


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
                12,
                [10,8,0,5,3],
                [2,4,1,1,3]
            ),
            3
        ),
    ]
    for input_args, expected in tests:
        r = s.carFleet(*input_args)
        result = r == expected
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(result, input_args, r, expected)
