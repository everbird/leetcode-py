#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def scoreOfParentheses(self, S):
        stack = [0]

        for c in S:
            if c == '(':
                stack.append(0)
            elif c == ')':
                v = stack.pop()
                _v = 1 if v == 0 else 2*v
                stack[-1] += _v

        return stack[0]


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            "()",
            1
        ),
        (
            "(())",
            2
        ),
        (
            "()()",
            2
        ),
        (
            "(()(()))",
            6
        ),
    ]
    for input_args, expected in tests:
        r = s.scoreOfParentheses(input_args)
        result = r == expected
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(result, input_args, r, expected)
