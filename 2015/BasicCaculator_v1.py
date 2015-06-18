#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        number = 0
        symbol = 1
        result = 0
        stack = []
        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)
            elif c == '+':
                result += symbol * number
                symbol = 1
                number = 0
            elif c == '-':
                result += symbol * number
                symbol = -1
                number = 0
            elif c == '(':
                stack.append(symbol)
                stack.append(result)
                symbol = 1
                result = 0
            elif c == ')':
                result += symbol * number
                _result = stack.pop()
                _symbol = stack.pop()
                result = _symbol*result + _result
                number = 0

        if number:
            result += symbol * number

        return result


if __name__ == '__main__':
    s = Solution()
    print s.calculate('1 + 1')
    print s.calculate(' 2-1 + 2 ')
    print s.calculate('(1+(4+5+2)-3)+(6+8)')
    print s.calculate('2-(5-6)')
