#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        symbol = -1 if numerator*denominator < 0 else 1
        n = abs(numerator)
        d = abs(denominator)
        r = ''
        if n >= d:
            r = str(n / d)
            n = n % d
        else:
            r = '0'

        if n:
            r += '.'

        t = []
        tail = ''
        loop = False
        index = None
        while n:
            if n not in t:
                t.append(n)
                n *= 10
                x = n / d
                tail += str(x)
                n = n % d
            else:
                index = t.index(n)
                loop = True
                break


        if loop:
            recurring = tail[index:]
            rest = tail[:index]
            r = r + '{}({})'.format(rest, recurring)
        else:
            r = r + tail

        if r != '0' and symbol == -1:
            return '-' + r
        else:
            return r


if __name__ == '__main__':
    s = Solution()
    #print s.fractionToDecimal(1, 2)
    #print s.fractionToDecimal(2, 1)
    #print s.fractionToDecimal(2, 3)
    #print s.fractionToDecimal(4, 7)
    #print s.fractionToDecimal(3, 7)
    print s.fractionToDecimal(1, 6)
    print s.fractionToDecimal(-1, 12)
    print s.fractionToDecimal(-50, 8)
