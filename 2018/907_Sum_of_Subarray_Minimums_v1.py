#!/usr/bin/eni python
# encoding: utf-8

class Solution(object):
    def sumSubarrayMins(self, A):
        r = 0
        stack = []
        array = [float('-inf')] + A + [float('-inf')]
        for i, n in enumerate(array):
            while stack and array[stack[-1]] > n:
                current = stack.pop()
                right = i
                left = stack[-1]
                r += array[current] * (right - current) * (current - left)

            stack.append(i)

        return r % (10**9 + 7)


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [3,1,2,4],
            17
        ),
        (
            range(1, 5000),
            833332360
        )
    ]
    f = s.sumSubarrayMins
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)

        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
