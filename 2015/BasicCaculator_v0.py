#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        s = s.strip()
        leftp = s.rfind('(')
        rightp = s[leftp:].find(')') + leftp if leftp != -1 else len(s)
        expression = s[leftp+1:rightp]
        r = 0
        for x in expression.split('+'):
            x = x.strip()
            items = x.split('-')
            t = self.s2i(items[0].strip())
            for n in items[1:]:
                t -= self.s2i(n.strip())
            r += t

        if leftp == -1:
            return r
        else:
            return self.calculate(s[:leftp] + self.i2s(r) + s[rightp+1:])

    def s2i(self, s):
        if s[0] == '#':
            return -int(s[1:])
        return int(s)

    def i2s(self, i):
        if i < 0:
            return '#{}'.format(-i)

        return str(i)


if __name__ == '__main__':
    s = Solution()
    print s.calculate('1 + 1')
    print s.calculate(' 2-1 + 2 ')
    print s.calculate('(1+(4+5+2)-3)+(6+8)')
    print s.calculate('2-(5-6)')
