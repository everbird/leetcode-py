#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        stack = []
        d = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for c in s:
            if c in '([{':
                stack.append(c)
            elif c in ')]}':
                if not stack or stack[-1] != d.get(c):
                    return False
                stack = stack[:-1]
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
