#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        stack = []
        for c in s:
            if stack and ((c == ')' and stack[-1] == '(')
                          or (c == ']' and stack[-1] == '[')
                          or (c == '}' and stack[-1] == '{')):
                stack = stack[:-1]
            else:
                stack.append(c)

        return not stack


if __name__ == '__main__':
    s = Solution()
    a = '()'
    print s.isValid(a)

    a = '()[]{}'
    print s.isValid(a)

    a = '(]'
    print s.isValid(a)

    a = '([)]'
    print s.isValid(a)

    a = ']'
    print s.isValid(a)
