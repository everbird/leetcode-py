#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        stack = []
        max_length = 0
        current_length = 0
        last = -1
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        # last (
                        current_length = i - stack[-1]
                    else:
                        current_length = i - last

                    max_length = max(max_length, current_length)
                else:
                    # last invalid )
                    last = i

        return max_length


if __name__ == '__main__':
    s = Solution()
    print s.longestValidParentheses(')()())')
    print s.longestValidParentheses('()()')
    print s.longestValidParentheses('(()')
    print s.longestValidParentheses('()(()')
    print s.longestValidParentheses('))))())()()(()')
    print s.longestValidParentheses('((()))')
