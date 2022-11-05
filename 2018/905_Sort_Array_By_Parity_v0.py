#!/usr/bin/eni python
# encoding: utf-8

class Solution(object):
    def sortArrayByParity(self, A):
        return list(g(A))

def g(A):
    rest = []
    for x in A:
        if x % 2 == 0:
            yield x
        else:
            rest.append(x)

    for x in rest:
        yield x


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [3,1,2,4],
            [2,4,3,1]
        ),
    ]
    f = s.sortArrayByParity
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)

        r = list(r)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
