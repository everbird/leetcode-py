#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        lena = len(a)
        lenb = len(b)
        if lena < lenb:
            return self.addBinary(b, a)

        r = ''
        carry = 0
        for i in range(1, lena+1):
            ai = ord(a[-i]) - ord('0')
            bi = ord(b[-i]) - ord('0') if i <= lenb else 0
            v = ai + bi + carry
            carry = v // 2
            r = str(v % 2) + r

        if carry:
            return str(carry) + r
        else:
            return r

if __name__ == '__main__':
    s = Solution()
    #print s.addBinary('10101011', '10001010')
    print s.addBinary('1010', '1011')
