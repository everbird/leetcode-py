#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        result = 0
        for m in s.strip().split('+'):
            r = None
            for n in m.strip().split('-'):
                v = self.cal(n)
                if r is None:
                    r = v
                else:
                    r -= v

            result += r if r else 0

        return result

    def cal(self, s):
        numbers = []
        ops = []
        number = 0
        for c in s:
            if c.isdigit():
                number = number * 10 + ord(c) - ord('0')
            elif c == '*':
                numbers.append(number)
                ops.append('*')
                number = 0
            elif c == '/':
                numbers.append(number)
                ops.append('/')
                number = 0

        if number or s[-1] == '0':
            numbers.append(number)

        for i, op in enumerate(ops):
            if op == '*':
                numbers[i+1] = numbers[i] * numbers[i+1]
            elif op == '/':
                numbers[i+1] = numbers[i] // numbers[i+1]

        return numbers[-1]


if __name__ == '__main__':
    s = Solution()
    print s.calculate('3+2*2')
    print s.calculate(' 3/2 ')
    print s.calculate(' 3+5 / 2 ')
    print s.calculate('0')
    print s.calculate('0+0')
