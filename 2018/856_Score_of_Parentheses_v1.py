#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def scoreOfParentheses(self, S):
        score = depth = 0
        for i, c in enumerate(S):
            if c == '(':
                depth += 1
            else:
                depth -= 1
                if S[i-1] == '(':
                    score += 2 ** depth
        return score


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
