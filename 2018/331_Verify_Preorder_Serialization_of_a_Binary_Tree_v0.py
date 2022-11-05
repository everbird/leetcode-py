#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):

    def isValidSerialization(self, preorder):
        items = preorder.split(',')
        length = len(items)
        stack = [items[0]]
        i = 1
        while stack:
            n = stack.pop()
            if n != '#':
                a = b = None
                if i+2 <= length:
                    a, b = items[i:i+2]
                elif i+1 <= length:
                    a = items[i]

                if not a or not b:
                    return False

                if b != '#':
                    stack.append(b)
                if a != '#':
                    stack.append(a)

                i += 2

        return i == length



if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            "9,3,4,#,#,1,#,#,2,#,6,#,#",
            True
        ),
        (
            "1,#",
            False
        ),
        (
            "9,#,#,1",
            False
        ),
        (
            "#",
            True
        ),
        (
            "#,#,#",
            False
        ),
    ]
    f = s.isValidSerialization
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
