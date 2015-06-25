#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        number_stack = []
        ops_stack = []
        number = 0
        ops = False
        s = s.strip()

        for c in s:
            if c in ('+', '-', '*', '/'):
                ops = True
                number_stack.append(number)
                ops_stack.append(c)
                number = 0
            elif c.isdigit():
                number = number * 10 + ord(c) - ord('0')
                ops = False
            else:
                pass

        if number or ops or s[-1] == '0':
            number_stack.append(number)

        while '*' in ops_stack or '/' in ops_stack:
            mp = ops_stack.index('*') if '*' in ops_stack else None
            dp = ops_stack.index('/') if '/' in ops_stack else None
            index = min(mp, dp) \
                if mp is not None and dp is not None else (mp or dp or 0)
            op = ops_stack[index]
            if op == '*':
                n1 = number_stack[index]
                n2 = number_stack[index+1]
                r = n1 * n2
                number_stack = number_stack[:index] + [r] + number_stack[index+2:]
            elif op == '/':
                n1 = number_stack[index]
                n2 = number_stack[index+1]
                r = n1 // n2
                number_stack = number_stack[:index] + [r] + number_stack[index+2:]

            ops_stack = ops_stack[:index] + ops_stack[index+1:]

        while ops_stack:
            op = ops_stack.pop()
            n1 = number_stack.pop()
            n2 = number_stack.pop()
            if op == '+':
                number_stack.append(n1+n2)
            elif op == '-':
                number_stack.append(n1-n2)

        return number_stack[0]


if __name__ == '__main__':
    s = Solution()
    print s.calculate('3+2*2')
    print s.calculate(' 3/2 ')
    print s.calculate(' 3+5 / 2 ')
    print s.calculate('0')
    print s.calculate('0+0')
