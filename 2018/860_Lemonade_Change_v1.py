#!/usr/bin/env python
# encoding: utf-8



class Solution(object):

    def lemonadeChange(self, bills):
        len_b = len(bills)

        def sub(index, b5=0, b10=0, b20=0):
            if index >= len_b:
                return True

            if b5 < 0 or b10 < 0 or b20 < 0:
                return False

            b = bills[index]
            if b == 5:
                return sub(index+1, b5+1, b10, b20)

            if b == 10:
                if b5 <= 0:
                    print 1
                    return False
                return sub(index+1, b5-1, b10+1, b20)

            if b5 <= 0:
                print 2
                return False
            elif b5 <= 2 and b10 <= 0:
                return False

            if b10 >= 1:
                return sub(index+1, b5-1, b10-1, b20+1)

            return sub(index+1, b5-3, b10, b20+1)

        return sub(0)



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
            [5,5,5,10,20],
            True
        ),
        (
            [5,5,10],
            True
        ),
        (
            [10,10],
            False
        ),
        (
            [5,5,10,10,20],
            False
        ),
        (
            [5,5,5,5,20,20,5,5,20,5],
            False
        )
    ]
    for input_args, expected in tests:
        r = s.lemonadeChange(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
