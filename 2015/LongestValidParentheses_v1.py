#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        stack = []
        max_l = 0
        last = -1
        current_length = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        current_length = i - stack[-1]
                    else:
                        current_length = i - last

                    max_l = max(max_l, current_length)
                else:
                    last = i

        return max_l


if __name__ == '__main__':
    s = Solution()
    print s.longestValidParentheses(')()())')
    print s.longestValidParentheses('()()')
    print s.longestValidParentheses('(()')
    print s.longestValidParentheses('()(()')
    print s.longestValidParentheses('))))())()()(()')
    print s.longestValidParentheses('((()))')
