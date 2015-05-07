#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        stack = []
        max_l = count = 0
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                    count += 2
                    if count > max_l:
                        max_l = count
                else:
                    count = 0


        return max_l


if __name__ == '__main__':
    s = Solution()
    print s.longestValidParentheses(')()())')
    print s.longestValidParentheses('()()')
    print s.longestValidParentheses('(()')
    print s.longestValidParentheses('()(()')
    print s.longestValidParentheses('))))())()()(()')
